import sqlite3
import requests


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
        id INTEGER PRIMARY KEY,
        name TEXT,
        available_bikes INTEGER,
        available_bike_stands INTEGER
    )
    ''')

    conn.commit()
    conn.close()


# Fonction pour insérer des données dans SQLite3
def inserer_donnees(data):
    conn = sqlite3.connect('stations_velos.db')
    cursor = conn.cursor()

    for station in data:
        cursor.execute('''
        INSERT INTO stations (id, name, available_bikes, 
        ²)
        VALUES (?, ?, ?, ?)
        ''', (station['number'], station['name'], station['available_bikes'], station['available_bike_stands']))

    conn.commit()
    conn.close()


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
