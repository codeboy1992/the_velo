import sqlite3
import requests
import numpy as np

# Fonction pour appeler l'API JCDecaux
def appeler_api_jcdecaux(api_key, contract_name):
    url = f"https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}"

    try:
        response = requests.get(url)
        print(f"Code de réponse : {response.status_code}")
        print(f"Contenu de la réponse : {response.text}")

        if response.status_code == 200:
            return response.json()  # Retourner les données au format JSON
        else:
            print(f"Erreur {response.status_code} : {response.text}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


# Fonction pour créer une table SQLite3
def creer_table():
    conn = sqlite3.connect('stations_velos.db')
    cursor = conn.cursor()

    # Création de la table des stations si elle n'existe pas déjà
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stations (
        number INTEGER PRIMARY KEY,
        contract_name TEXT,
        name TEXT,
        address TEXT,
        lat REAL,
        lng REAL,
        banking BOOLEAN,
        bonus BOOLEAN,
        bike_stands INTEGER,
        available_bike_stands INTEGER,
        available_bikes INTEGER,
        status TEXT,
        last_update INTEGER
    )
    ''')

    conn.commit()
    conn.close()


# Fonction pour insérer des données dans SQLite3
def inserer_donnees(data):
    conn = sqlite3.connect('stations_velos.db')
    cursor = conn.cursor()

    for station in data:
        # Insertion ou mise à jour des données
        cursor.execute('''
        INSERT INTO stations (number, contract_name, name, address, lat, lng, banking, bonus, bike_stands, available_bike_stands, available_bikes, status, last_update)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(number) DO UPDATE SET
            contract_name=excluded.contract_name,
            name=excluded.name,
            address=excluded.address,
            lat=excluded.lat,
            lng=excluded.lng,
            banking=excluded.banking,
            bonus=excluded.bonus,
            bike_stands=excluded.bike_stands,
            available_bike_stands=excluded.available_bike_stands,
            available_bikes=excluded.available_bikes,
            status=excluded.status,
            last_update=excluded.last_update
        ''', (
            station['number'],
            station['contract_name'],
            station['name'],
            station['address'],
            station['position']['lat'],
            station['position']['lng'],
            station['banking'],
            station['bonus'],
            station['bike_stands'],
            station['available_bike_stands'],
            station['available_bikes'],
            station['status'],
            station['last_update']
        ))

    conn.commit()
    conn.close()

# Coucou Patoche !
# API Key et contrat
api_key = "7967e55f58492463189c6b2d17ccb21343a559b3"
contract_name = "nancy"

# Créer la table
creer_table()

# Appeler l'API et récupérer les données
data = appeler_api_jcdecaux(api_key, contract_name)

# Insérer les données dans la base SQLite
if data:
    inserer_donnees(data)
    print("Données insérées avec succès dans la base SQLite.")
