from flask import Flask, render_template, request, jsonify
import folium
from folium.plugins import AntPath
import requests
import math

app = Flask(__name__)


# Fonction pour calculer la distance Haversine entre deux points (lat, lng)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon de la Terre en km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


# Trouver la station verte la plus proche d'une station rouge/orange
def get_closest_full_station(lat_empty, lng_empty):
    # Appel à l'API JCDecaux
    url = 'https://api.jcdecaux.com/vls/v1/stations?contract=nancy&apiKey=3993633e26d5c2fef3ff02b5273e99e26ffed693'
    response = requests.get(url)

    if response.status_code == 200:
        stations_data = response.json()

        # Filtrer les stations vertes (>= 75% vélos disponibles)
        green_stations = [
            station for station in stations_data
            if (station['available_bikes'] / station['bike_stands']) * 100 >= 75
        ]

        if not green_stations:
            return None  # Pas de station verte disponible

        # Trouver la station verte la plus proche
        closest_station = None
        min_distance = float('inf')
        for station in green_stations:
            lat_full = station['position']['lat']
            lng_full = station['position']['lng']
            distance = haversine(lat_empty, lng_empty, lat_full, lng_full)

            if distance < min_distance:
                min_distance = distance
                closest_station = station

        return closest_station
    else:
        return None


# Route pour réinitialiser la carte et afficher toutes les stations en consommant directement l'API
@app.route('/reset_map', methods=['GET'])
def reset_map():
    # URL de l'API JCDecaux avec ta clé d'API
    url = 'https://api.jcdecaux.com/vls/v1/stations?contract=nancy&apiKey=3993633e26d5c2fef3ff02b5273e99e26ffed693'

    # Appel à l'API JCDecaux
    response = requests.get(url)

    if response.status_code == 200:
        stations_data = response.json()  # Récupérer les données des stations

        # Filtrer les doublons (par exemple, par le nom de la station)
        unique_stations = {station['name']: station for station in stations_data}.values()

        # Générer une nouvelle carte avec les données mises à jour
        nancy_coords = [48.6921, 6.1844]
        m = folium.Map(location=nancy_coords, zoom_start=13)

        # Ajout des stations sur la carte
        for station in unique_stations:
            name = station['name']
            lat = station['position']['lat']
            lng = station['position']['lng']
            available_bikes = station['available_bikes']
            bike_stands = station['bike_stands']

            # Calcul du pourcentage de remplissage
            percentage_filled = (available_bikes / bike_stands) * 100
            popup_text = f"<strong>{name}</strong><br>Vélos disponibles : {available_bikes}/{bike_stands} ({percentage_filled:.1f}%)"

            # Définir la couleur en fonction du pourcentage de remplissage
            if percentage_filled < 25:
                color = 'red'
            elif 25 <= percentage_filled < 75:
                color = 'orange'
            else:
                color = 'green'

            # Ajouter le marqueur sur la carte
            folium.Marker(
                location=[lat, lng],
                popup=popup_text,
                icon=folium.Icon(color=color)
            ).add_to(m)

        # Sauvegarder la carte comme fichier HTML
        m.save('static/map.html')

        return jsonify({"success": True, "stations": list(unique_stations)})
    else:
        return jsonify({"success": False, "error": "API call failed"}), 500


# Fonction pour obtenir l'itinéraire via OSRM
def get_route(lat1, lon1, lat2, lon2):
    url = f"http://router.project-osrm.org/route/v1/driving/{lon1},{lat1};{lon2},{lat2}?overview=full&geometries=geojson"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        route = data['routes'][0]['geometry']['coordinates']  # La géométrie de la route (liste des points GPS)
        return [(point[1], point[0]) for point in route]  # Inverser les coordonnées pour Folium
    return None


# Route principale pour afficher la carte et les stations
@app.route('/', methods=['GET', 'POST'])
def index():
    # Appel à l'API JCDecaux pour afficher toutes les stations
    response = requests.get(
        'https://api.jcdecaux.com/vls/v1/stations?contract=nancy&apiKey=3993633e26d5c2fef3ff02b5273e99e26ffed693')

    if response.status_code == 200:
        stations_data = response.json()

        # Générer la carte avec Folium
        nancy_coords = [48.6921, 6.1844]
        m = folium.Map(location=nancy_coords, zoom_start=13)

        for station in stations_data:
            name = station['name']
            lat = station['position']['lat']
            lng = station['position']['lng']
            available_bikes = station['available_bikes']
            bike_stands = station['bike_stands']
            percentage_filled = (available_bikes / bike_stands) * 100
            popup_text = f"<strong>{name}</strong><br>Vélos disponibles : {available_bikes}/{bike_stands} ({percentage_filled:.1f}%)"

            if percentage_filled < 25:
                color = 'red'
            elif 25 <= percentage_filled < 75:
                color = 'orange'
            else:
                color = 'green'

            folium.Marker(
                location=[lat, lng],
                popup=popup_text,
                icon=folium.Icon(color=color)
            ).add_to(m)

        m.save('static/map.html')
        return render_template('index.html', stations=stations_data)
    else:
        return "Erreur lors de la récupération des stations."


# Route pour afficher la station sélectionnée et la station verte la plus proche
@app.route('/station', methods=['GET'])
def show_station():
    lat = float(request.args.get('lat'))
    lng = float(request.args.get('lng'))
    available_bikes = int(request.args.get('available_bikes'))

    # Générer une carte centrée sur la station sélectionnée
    m = folium.Map(location=[lat, lng], zoom_start=15)

    # Si la station est rouge ou orange, trouver la station verte la plus proche
    if available_bikes <= 10:
        station_max = get_closest_full_station(lat, lng)
        if station_max:
            # Obtenir l'itinéraire via OSRM
            route = get_route(lat, lng, station_max['position']['lat'], station_max['position']['lng'])
            if route:
                folium.PolyLine(
                    locations=route,
                    color='blue',
                    weight=2.5,
                    dashArray="5,5",

                ).add_to(m)

            # Ajouter un marqueur pour la station verte (proche)
            folium.Marker(
                location=[station_max['position']['lat'], station_max['position']['lng']],
                popup=f"Station Verte (Proche) : {station_max['name']}<br>Vélos : {station_max['available_bikes']}",
                icon=folium.Icon(color='green')
            ).add_to(m)

    # Ajouter un marqueur pour la station sélectionnée
    folium.Marker(
        location=[lat, lng],
        popup=f"Station Sélectionnée<br>Vélos : {available_bikes}",
        icon=folium.Icon(color='red' if available_bikes <= 5 else 'orange')
    ).add_to(m)

    # Sauvegarder la carte comme fichier HTML
    m.save('static/map.html')
    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(debug=True)
