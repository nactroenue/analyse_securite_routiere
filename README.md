# Analyse de la Sécurité Routière en France

## Objectif du Projet

L'objectif principal de ce projet est d'analyser les **accidents de la route en France** en tenant compte de divers facteurs (météorologie, types de routes, comportements des conducteurs, etc.) afin de :

1. **Comprendre les facteurs de risque** : Identifier les conditions qui augmentent le risque d'accidents graves, telles que les conditions environnementales, les profils des conducteurs, et les manœuvres effectuées avant l'accident.

2. **Prédire la gravité des accidents** : Utiliser des algorithmes de machine learning pour créer un modèle capable de prédire la **gravité des accidents** (indemne, blessé léger, blessé grave, tué) en fonction des caractéristiques d'un accident.

3. **Proposer des solutions préventives** : En utilisant les résultats de l'analyse, proposer des recommandations pour améliorer la sécurité routière et guider les campagnes de prévention.

4. **Utiliser des techniques avancées de visualisation et de modélisation** : Le projet combine des techniques d'analyse de données, de visualisation, et de machine learning pour fournir des insights visuels et prédictifs sur les accidents de la route.

---

## Données

Le projet repose sur des données provenant des accidents corporels de la circulation routière en France entre 2019 et 2022. Ces données sont cruciales pour comprendre les facteurs contribuant aux accidents et sont utilisées pour des analyses descriptives et prédictives.

### 1. Sources des données
Les données sont issues des fichiers publics disponibles sur le site officiel du gouvernement français, relatifs aux accidents de la route. Ces données incluent :

- **Fichier des caractéristiques des accidents** : Informations sur l'emplacement, l'heure, et la nature des accidents.
- **Fichier des usagers** : Détails sur les conducteurs, passagers et piétons impliqués dans les accidents (âge, sexe, catégorie d'usager).
- **Fichier des véhicules** : Informations sur les véhicules impliqués (type de véhicule, manœuvre avant l'accident).
- **Fichier des lieux** : Informations sur les caractéristiques des routes où les accidents se sont produits.

### 2. Structure des données
Les données sont stockées dans plusieurs tables PostgreSQL pour faciliter les jointures et l'analyse croisée. Voici un aperçu des tables principales :

- **Table `caracteristiques`** : Contient des informations générales sur chaque accident, telles que la date, l'heure, et les conditions de luminosité (lum), et météorologiques (atm).
- **Table `usagers`** : Détails des usagers impliqués dans les accidents, avec des colonnes sur l'âge (an_nais), le sexe (sexe), et la gravité des blessures (grav).
- **Table `vehicules`** : Contient des informations sur les véhicules impliqués dans les accidents, comme la catégorie de véhicule (catv) et la manœuvre avant l'accident (manv).
- **Table `lieux`** : Spécifie les caractéristiques des routes (catr), comme le nombre de voies, le type de circulation, et la largeur de la chaussée.

### 3. Préparation des données
Avant de procéder à l'analyse, plusieurs étapes de nettoyage et préparation des données ont été nécessaires :

- **Traitement des valeurs manquantes** : Les valeurs manquantes ont été imputées ou ignorées en fonction de leur importance pour l'analyse.
- **Encodage des variables catégorielles** : Les variables comme lum (conditions de luminosité) et catv (type de véhicule) ont été encodées en valeurs numériques pour pouvoir être utilisées dans les modèles prédictifs.
- **Agrégation des données** : Les données ont été agrégées par région, type de route, et période temporelle (jour, heure, saison) pour analyser les tendances géographiques et temporelles des accidents.

### 4. Exemples de variables importantes
Voici quelques-unes des variables clés utilisées dans les analyses :

- **grav** : Gravité des blessures (1 : Indemne, 2 : Blessé léger, 3 : Blessé hospitalisé, 4 : Tué).
- **atm** : Conditions météorologiques (1 : Normale, 2 : Pluie légère, 3 : Pluie forte, etc.).
- **catr** : Type de route (1 : Autoroute, 2 : Route Nationale, 3 : Route Départementale, etc.).
- **hrmn** : Heure et minute de l'accident.

---

## Méthodologie

### 1. Nettoyage et Prétraitement des Données

- **Imputation des valeurs manquantes** : Certaines variables, telles que les conditions météorologiques (atm) ou les manœuvres des conducteurs (manv), contenaient des valeurs manquantes. Ces valeurs ont été imputées avec des valeurs par défaut (par exemple, conditions météorologiques normales) ou exclues de l'analyse lorsque nécessaire.
- **Encodage des variables catégorielles** : Les variables catégorielles, telles que lum (conditions de luminosité), atm (conditions météorologiques), et catr (type de route) ont été encodées sous forme numérique pour pouvoir être intégrées dans les modèles de machine learning.
- **Agrégation des données** : Les données ont été agrégées par région, type de route, et période temporelle (jour, heure, saison) afin d’analyser les tendances géographiques et temporelles des accidents. Cela permet d’identifier les zones et moments les plus accidentogènes.
- **Création de nouvelles variables** : Création de variables dérivées, comme l’âge des conducteurs (en fonction de leur année de naissance) et les périodes spécifiques de la journée (matinée, après-midi, soirée) pour affiner l’analyse temporelle.

### 2. Analyse Exploratoire des Données (EDA)

- **Visualisation de la distribution des accidents** : Des graphiques ont été utilisés pour observer la répartition des accidents selon plusieurs axes : la gravité, l'heure de la journée, la saison, le type de route, et les conditions météorologiques. Cela a permis d'identifier les moments et lieux critiques à haut risque d'accident.
- **Corrélation entre les variables** : Une matrice de corrélation a été calculée pour identifier les relations entre les différentes variables, notamment entre la gravité des accidents et des facteurs comme les conditions météorologiques, la luminosité, et le type de route.
- **Clustering des scénarios d’accidents** : Un modèle de clustering K-means a été appliqué pour regrouper les scénarios d'accidents similaires, en se basant sur les conditions de luminosité (lum) et le type de collision (col). Cela a aidé à identifier des scénarios récurrents d'accidents graves.

### 3. Visualisation des Données

- **Heatmaps** : Pour visualiser la répartition des accidents par gravité en fonction des conditions météorologiques et du type de route.
- **Histogrammes** : Pour représenter la distribution des accidents en fonction de l’heure de la journée et des saisons.
- **Barplots** : Pour montrer la fréquence des manœuvres dangereuses avant les accidents, ainsi que les comportements à risque chez différents profils d’usagers.

---

## Visualisations Clés

### 1. Gravité des Accidents par Conditions Météorologiques  
![Gravité des Accidents par Conditions Météorologiques](./images/Gravité%20des%20accidents%20par%20conditions%20météorologiques.png)

### 2. Clustering des Scénarios d'Accidents par Conditions de Luminosité et Type de Collision  
![Clustering des Scénarios d'Accidents](./images/Clustering%20des%20Scénarios%20d%27Accidents%20par%20Conditions%20de%20Luminosité%20et%20Type%20de%20Collision.png)

### 3. Comportements Risqués Associés aux Accidents  
![Comportements Risqués](./images/Comportements%20Risqués%20Associés%20aux%20Accidents.png)

### 4. Nombre d'Accidents par Âge et Sexe  
![Nombre d'Accidents par Âge et Sexe](./images/Nombre%20d'Accidents%20par%20Age%20et%20Sexe.png)

### 5. Distribution des Accidents par Heure de la Journée  
![Distribution des Accidents par Heure de la Journée](./images/Distribution%20des%20Accidents%20par%20Heure%20de%20la%20Journée.png)

### 6. Distribution des Accidents par Jours de la Semaine  
![Distribution des Accidents par Jours de la Semaine](./images/Distribution%20des%20Accidents%20par%20Jours%20de%20la%20Semaine.png)

### 7. Matrice de Corrélation des Variables et de la Gravité des Accidents  
![Matrice de corrélation des variables et de la gravité des accidents](./images/Matrice%20de%20corr%C3%A9lation%20des%20variables%20et%20de%20la%20gravit%C3%A9%20des%20accidents.png)

---

## Modèles de Machine Learning

### 1. Objectif de la Modélisation
L'objectif principal est de prédire la gravité potentielle d'un accident en fonction des caractéristiques de l'accident. Les modèles sont évalués sur leur capacité à bien distinguer les accidents graves (blessures graves et décès) des accidents mineurs.

### 2. Données utilisées pour l’entraînement
Les modèles ont été entraînés sur les données prétraitées comprenant des variables comme :

- **Variables explicatives** :
  - lum : Conditions de luminosité
  - atm : Conditions météorologiques
  - catr : Type de route
  - manv : Manœuvre effectuée avant l'accident
  - nbv : Nombre de voies de circulation

- **Variable cible** :
  - grav : Gravité de l'accident (1 : indemne, 2 : blessé léger, 3 : blessé grave, 4 : tué)

### 3. Modèles utilisés
Deux modèles principaux ont été sélectionnés pour cette tâche prédictive : **Random Forest** et **XGBoost**, deux algorithmes bien adaptés pour les données complexes et les problèmes de classification multi-classes comme celui-ci.

#### 3.1 Random Forest (Forêt Aléatoire)
Le modèle Random Forest est un algorithme d'ensemble qui crée plusieurs arbres de décision et agrège leurs résultats pour produire des prédictions robustes.

**Pourquoi Random Forest ?**

- Adapté aux données avec des variables catégorielles et continues mélangées.
- Efficace pour traiter les jeux de données déséquilibrés, important ici car les accidents graves sont moins fréquents que les accidents mineurs.
- **Pondération des Classes** : Application d'une pondération des classes pour donner plus d'importance aux accidents graves dans l'entraînement du modèle.
- **Optimisation avec GridSearchCV** : Optimisation des hyperparamètres tels que le nombre d'arbres (n_estimators), la profondeur maximale des arbres (max_depth), et les critères de division (min_samples_split, min_samples_leaf).

**Résultats :**

- **Score d'Exactitude** : 0.75
- **Précision pour les accidents graves** : 0.65

**Matrice de Confusion pour Random Forest :**
![Matrice de Confusion RF](./images/Matrice%20de%20Confusion%20pour%20le%20Modèle%20Forêt%20Aléatoire%20Pondéré.png)

#### 3.2 XGBoost
Le modèle XGBoost (eXtreme Gradient Boosting) est un algorithme d'apprentissage supervisé puissant, connu pour sa capacité à obtenir de bons résultats sur des jeux de données complexes.

**Pourquoi XGBoost ?**

- Performant pour gérer des données hétérogènes avec des variables catégorielles et continues.
- Rapide, efficace, et capable de traiter de grandes quantités de données tout en optimisant l'utilisation des ressources.
- **Optimisation avec GridSearchCV** : Ajustement des hyperparamètres tels que le taux d'apprentissage (learning_rate), le nombre de boostings (n_estimators), et la profondeur maximale des arbres (max_depth).

**Résultats :**

- **Score d'Exactitude** : 0.78
- **Précision pour les accidents graves** : 0.68

**Matrice de Confusion pour XGBoost :**

![Matrice de Confusion XGBoost](./images/Matrice%20de%20Confusion%20pour%20le%20Modèle%20Forêt%20Aléatoire%20Optimisé.png)

### 4. Évaluation des Modèles
Pour évaluer la performance des modèles, plusieurs métriques ont été utilisées :

- **Matrice de confusion** : Visualisation des prédictions correctes et incorrectes pour chaque classe de gravité.
- **Précision, Rappel et F1-score** :
  - **Précision** : Proportion de prédictions correctes pour chaque classe.
  - **Rappel** : Combien d'accidents graves ont été correctement identifiés par rapport à l'ensemble des accidents graves.
  - **F1-score** : Compromis entre la précision et le rappel.

### 5. Comparaison des Modèles

| Modèle         | Score d'Exactitude | Précision (Accidents Graves) | Rappel (Accidents Graves) | F1-Score |
|----------------|--------------------|------------------------------|---------------------------|----------|
| Random Forest  | 0.75               | 0.65                         | 0.60                      | 0.62     |
| XGBoost        | 0.78               | 0.68                         | 0.63                      | 0.65     |

**Conclusion :** Le modèle XGBoost a légèrement mieux performé que Random Forest, avec un meilleur score d'exactitude et une meilleure précision pour les accidents graves. Cependant, les deux modèles fournissent des résultats intéressants et peuvent être affinés avec des données supplémentaires et des ajustements d'hyperparamètres.

---

## Installation

### 1. Cloner le projet

Pour commencer, vous devez cloner ce projet depuis GitHub. Exécutez la commande suivante dans votre terminal :

```bash
git clone https://github.com/nactroenue/analyse_securite_routiere.git

### 2. Accéder au répertoire du projet

Une fois le projet cloné, accédez au répertoire du projet à l'aide de la commande suivante :

cd analyse_securite_routiere

### 3. Installer les dépendances
Toutes les bibliothèques nécessaires au projet sont listées dans le fichier requirements.txt. Pour installer ces dépendances, exécutez la commande suivante :

pip install -r requirements.txt

Cela installera toutes les bibliothèques requises, telles que pandas, sqlalchemy, seaborn, scikit-learn, et xgboost, entre autres.

### 4. Lancer le projet

Après avoir configuré la base de données et installé les dépendances, vous pouvez lancer les analyses et les modèles prédictifs.

Pour exécuter le projet, lancez le fichier principal main.py :

python main.py

Ce script exécutera toutes les étapes du projet, de l'analyse exploratoire des données à l'entraînement des modèles de machine learning, en passant par les visualisations.

---

## Conclusion et Perspectives

### 1. Bilan du Projet
Ce projet a permis d'explorer en profondeur les accidents de la route en France, en analysant divers facteurs comme les conditions météorologiques, le type de route, les comportements des conducteurs, et la gravité des accidents.

Grâce à une analyse descriptive et des modèles de machine learning, plusieurs points essentiels ont été identifiés :

Analyse descriptive : Les visualisations ont révélé des tendances importantes :

Les accidents graves sont plus fréquents dans des conditions météorologiques difficiles (pluie, brouillard) et en situation de faible luminosité (nuit sans éclairage).
Les jeunes conducteurs masculins sont surreprésentés dans les accidents graves.
Les heures de pointe (matin et soir) montrent une concentration plus élevée d'accidents.
Modèles prédictifs : Les modèles de machine learning, notamment Random Forest et XGBoost, ont été utilisés pour prédire la gravité des accidents. Bien que les résultats soient prometteurs (précision de 75% à 78% selon les modèles), des ajustements supplémentaires sont possibles pour améliorer encore la performance, notamment sur la prédiction des accidents graves.

Optimisation des modèles : L’utilisation de GridSearchCV a permis d'optimiser les hyperparamètres des modèles et d’améliorer leur performance. Le modèle XGBoost s'est montré légèrement plus performant que Random Forest, avec un score d'exactitude de 0.78 et une meilleure précision pour les accidents graves.

### 2. Limites du Projet
Malgré les résultats encourageants, certaines limitations existent dans ce projet :

Données déséquilibrées : Comme dans de nombreux jeux de données réels, les accidents graves (blessés graves ou décès) sont sous-représentés par rapport aux accidents mineurs. Bien que la pondération des classes ait aidé à corriger ce déséquilibre, d'autres méthodes, comme le sous-échantillonnage ou la sur-échantillonnage des classes rares, pourraient être envisagées pour améliorer la performance des modèles.

Données manquantes : Certaines variables, telles que les manœuvres des conducteurs ou les conditions météorologiques, contiennent des valeurs manquantes. Des techniques d’imputation plus sophistiquées pourraient être utilisées pour améliorer la qualité des données.

Caractéristiques supplémentaires : L'ajout de données externes, telles que les conditions de circulation en temps réel, ou d'autres variables comme le niveau de compétence des conducteurs, pourrait améliorer la précision des prédictions.

### 3. Perspectives et Améliorations Futures
Plusieurs améliorations peuvent être envisagées pour approfondir ce projet et augmenter sa pertinence :

Intégration de données en temps réel :

Intégrer des données en temps réel, comme les conditions de circulation ou météorologiques, pour améliorer les prédictions. Cela permettrait aux modèles de s'adapter dynamiquement aux changements de contexte.
Tableau de bord interactif :

Créer un tableau de bord interactif (avec Power BI, Tableau, ou Plotly Dash) permettrait aux utilisateurs (autorités locales, gestionnaires de la sécurité routière) d'explorer les données et les prédictions de manière dynamique. Cela pourrait inclure des cartes interactives des zones à risque et des visualisations des périodes critiques.
Amélioration des modèles prédictifs :

Utiliser des modèles d'apprentissage plus complexes comme les réseaux neuronaux ou des algorithmes d'apprentissage profond (deep learning) pour améliorer les prédictions.
Tester d'autres techniques de traitement des données déséquilibrées, comme le SMOTE (Synthetic Minority Over-sampling Technique), pour améliorer la prédiction des accidents graves.
Déploiement d'un système prédictif :

Déployer un système prédictif en temps réel capable de signaler les accidents à haut risque avant qu'ils ne se produisent, en utilisant des flux de données en direct et en générant des alertes pour les zones à risque.
4. Conclusion
En conclusion, ce projet montre comment les données peuvent être utilisées pour améliorer la sécurité routière. En analysant les facteurs liés aux accidents de la route et en utilisant des modèles de machine learning, il est possible d'identifier les moments, lieux et comportements les plus risqués.

Les résultats obtenus peuvent servir à guider les autorités locales dans la prise de décisions stratégiques pour réduire le nombre d'accidents et protéger les usagers de la route. Le projet ouvre également la voie à de nombreuses possibilités d'amélioration, tant sur le plan technique que pratique, pour des systèmes prédictifs encore plus performants et des analyses plus détaillées.
