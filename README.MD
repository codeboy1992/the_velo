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
    git clone https://github.com:codeboy1992/the_velo.git
    ```
2. Aller dans le répertoire du projet :
    ```bash
    cd the_velo
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

## Version Alternative

Une version alternative de ce projet est disponible sur la branche `seb`. Cette version contient des fonctionnalités supplémentaires ou des approches différentes. Pour accéder à cette version, il suffit de basculer sur la branche `seb` avec la commande suivante :

## Contributeurs

- **Patrick HEM**
- **Yohan MATEUS**
- **Romuald CROCHAT**
- **Sébastien GERARD**
```bash
git checkout seb
