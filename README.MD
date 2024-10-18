# Projet de Carte des Stations de Vélos

Ce projet propose une carte dynamique affichant des informations en temps réel sur les stations de vélos, y compris le nombre de vélos disponibles et le nombre total de places. Il utilise Flask pour le backend et Leaflet.js pour la carte interactive.

## Fonctionnalités

- **Carte Interactive** : Affiche les stations de vélos sur une carte avec des marqueurs.
- **Données en temps réel** : Les informations sur la disponibilité des vélos sont mises à jour toutes les 2 minutes.
- **Recherche de Stations** : Les utilisateurs peuvent rechercher des stations spécifiques par nom.
- **Tri des Stations** : Les stations sont triées en fonction du pourcentage de vélos disponibles.
- **Codage Couleur** : Les stations sont colorées en fonction de leur disponibilité :
  - Rouge : Moins de 25 % de vélos disponibles
  - Orange : Entre 25 % et 75 % de vélos disponibles
  - Vert : Plus de 75 % de vélos disponibles

## Technologies Utilisées

- **Frontend** : HTML, CSS, JavaScript (avec Leaflet.js pour le rendu de la carte)
- **Backend** : Python, Flask
- **Données de Carte** : OpenStreetMap
- **Bibliothèques** :
  - [Leaflet.js](https://leafletjs.com/) pour le rendu de la carte
  - [Bootstrap](https://getbootstrap.com/) pour le style
  - [Awesome Markers](https://github.com/lvoogdt/Leaflet.awesome-markers) pour les icônes des marqueurs

## Installation et Configuration

1. Cloner le dépôt :
    ```bash
    git clone https://github.com/ton-repo/carte-stations-velo.git
    ```
2. Aller dans le répertoire du projet :
    ```bash
    cd carte-stations-velo
    ```
3. Installer les dépendances Python nécessaires :
    ```bash
    pip install -r requirements.txt
    ```
4. Démarrer le serveur Flask :
    ```bash
    flask run
    ```

5. Ouvrir ton navigateur et aller sur `http://localhost:5000` pour voir la carte.

## Fichiers

- `index.html` : La page principale affichant la carte et la barre latérale pour la recherche et le tri des stations de vélos.
- `map.html` : Contient la logique de rendu de la carte avec Leaflet.js.
- `styles.css` : Styles pour la page, y compris le codage couleur des stations en fonction de la disponibilité des vélos.
- `velo.py` : Script backend qui gère la récupération et la mise à jour des données des stations de vélos (assure-toi que ce script est connecté à ta source de données pour les mises à jour des stations).

## Comment ça marche

- **Récupération des données** : Le backend (Flask) récupère périodiquement les données actuelles des stations de vélos.
- **Rendu de la carte** : La carte est rendue avec Leaflet.js, avec des marqueurs indiquant la localisation de chaque station.
- **Tri des stations** : Les stations sont triées en fonction du pourcentage de vélos disponibles et sont codées en couleur.

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
