
# Application de Gestion des Stations de Vélos à Nancy

Ce projet est une application web interactive qui permet de visualiser en temps réel les stations de vélos de la ville de Nancy, via l'API JCDecaux. L'application permet d'identifier les stations surchargées et sous-alimentées, de calculer des itinéraires optimaux pour rééquilibrer les vélos entre ces stations et propose une carte dynamique avec plusieurs fonctionnalités.

## Fonctionnalités principales

1. **Visualisation des stations de vélos** :
   - Les stations sont affichées sur une carte interactive (Leaflet).
   - Les stations surchargées (manque de places pour stationner les vélos) et sous-alimentées (manque de vélos disponibles) sont clairement identifiées avec des marqueurs de couleur.

2. **Mise à jour en temps réel** :
   - Les données des stations sont récupérées via l'API JCDecaux à intervalles réguliers.
   - Un mécanisme de cache optimise les appels à l'API pour éviter les surcharges et améliorer les performances.
   - Un clignotement des marqueurs sur la carte alerte lorsque des vélos sont ajoutés ou retirés d'une station.

3. **Calcul d'itinéraires** :
   - L'utilisateur peut sélectionner une station surchargée et calculer l'itinéraire vers la station sous-alimentée la plus proche.
   - Le calcul d'itinéraire prend en compte le mode de déplacement choisi (vélo ou camionnette).
   - Utilisation des graphes OpenStreetMap pour calculer les itinéraires en fonction du réseau cyclable ou routier.

4. **Interface utilisateur interactive** :
   - Un menu permet de sélectionner les stations sur la carte et de zoomer directement sur celles-ci.
   - Les stations sont filtrées et listées par type (surchargées, sous-alimentées, normales).

## Technologies utilisées

- **Backend** : Flask (Python)
- **API** : JCDecaux pour récupérer les données en temps réel des stations de vélos.
- **Front-end** : HTML, CSS, JavaScript, Leaflet pour la carte interactive.
- **Graphes d'itinéraires** : OSMnx et NetworkX pour le calcul des chemins optimaux.
- **Carte** : OpenStreetMap via Leaflet.

## Structure du projet

```
.
├── app.py                  # Code principal Flask pour gérer les routes et les API
├── templates
│   └── index.html          # Fichier HTML principal pour afficher la carte et les données
├── static
│   ├── style.css           # Fichier CSS pour le style
│   └── main.js             # Script JavaScript pour l'interactivité de la carte
├── graph_cyclable.graphml  # Graphe du réseau cyclable
├── graph_drive.graphml     # Graphe du réseau routier pour camionnettes
└── README.md               # Documentation du projet
```

## Installation

1. Clonez le dépôt Git :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   ```

2. Accédez au dossier du projet :
   ```bash
   cd votre-repo
   ```

3. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```

4. Exécutez l'application :
   ```bash
   python app.py
   ```

5. Ouvrez votre navigateur et accédez à `http://127.0.0.1:5000`.

## Utilisation

- Visualisez les stations de vélos de Nancy, en fonction de leur statut (surchargées, sous-alimentées, normales).
- Cliquez sur une station pour zoomer et obtenir des informations détaillées.
- Sélectionnez une station surchargée pour calculer un itinéraire vers la station sous-alimentée la plus proche.

## Améliorations possibles

- Ajouter des notifications en temps réel lorsque des vélos sont ajoutés/retirés.
- Optimiser la gestion du cache pour de plus grandes villes ou un plus grand nombre de stations.
- Ajouter des statistiques sur les tendances des stations (heures de forte affluence, etc.).
- Intégrer des suggestions pour l'utilisateur afin de rééquilibrer les vélos entre les stations.

## Contributeurs

- **Patrick HEM**
- **Yohan MATEUS**
- **Romuald CROCHAT**
- **Sébastien GERARD**
## Contributeurs

- **Patrick HEM**
- **Yohan MATEUS**
- **Romuald CROCHAT**
- **Sébastien GERARD**
