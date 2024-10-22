# analyse_gravite_accidents.py

import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from xgboost import XGBClassifier

def main():
    # Étape 1 : Créer la connexion avec la base de données
    TYPE_BASE_DONNEES = 'postgresql'
    DBAPI = 'psycopg2'
    HOTE = 'localhost'
    UTILISATEUR = 'postgres'
    MOT_DE_PASSE = ''
    PORT = 5432
    BASE_DONNEES = 'postgres'

    moteur = create_engine(f"{TYPE_BASE_DONNEES}+{DBAPI}://{UTILISATEUR}:{MOT_DE_PASSE}@{HOTE}:{PORT}/{BASE_DONNEES}")

    # Étape 2 : Charger les données depuis la base dans un DataFrame Pandas
    requete = """
    SELECT c.Num_Acc, c.jour, c.mois, c.an, c.hrmn, c.lum, c.dep, l.catr, l.circ, l.nbv, l.surf, l.situ, l.vma, 
           v.catv, u.catu, u.grav, c.atm
    FROM caracteristiques c
    JOIN lieux l ON c.Num_Acc = l.Num_Acc
    JOIN vehicules v ON c.Num_Acc = v.Num_Acc
    JOIN usagers u ON c.Num_Acc = u.Num_Acc;
    """
    df = pd.read_sql(requete, moteur)

    # Étapes 3 à 9 : Prétraitement des données
    df.fillna(-1, inplace=True)

    def convertir_temps_en_minutes(chaine_temps):
        try:
            heure, minute = map(int, chaine_temps.split(':'))
            return heure * 60 + minute
        except ValueError:
            return -1

    df['hrmn'] = df['hrmn'].apply(convertir_temps_en_minutes)
    df.drop(columns=['dep', 'num_acc'], inplace=True)
    df = pd.get_dummies(df, columns=['lum', 'atm', 'catr', 'circ', 'surf', 'situ', 'catv', 'catu'], drop_first=True)
    df['grav'] = df['grav'].replace(-1, 0)
    assert df['grav'].min() >= 0, "La variable cible contient des valeurs négatives !"

    X = df.drop(columns=['grav'])
    y = df['grav']

    # Étapes 10 à 12 : Division des données et entraînement du modèle pondéré
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    poids_classes = {0: 8, 1: 1, 2: 3, 3: 5, 4: 4}
    modele_rf_pondere = RandomForestClassifier(n_estimators=100, random_state=42, class_weight=poids_classes)
    modele_rf_pondere.fit(X_train, y_train)

    y_pred_pondere = modele_rf_pondere.predict(X_test)
    print("Rapport de Classification avec Pondération des Classes :\n", classification_report(y_test, y_pred_pondere))
    print("Score d'Exactitude avec Pondération des Classes :", accuracy_score(y_test, y_pred_pondere))

    # Afficher la matrice de confusion
    cm = confusion_matrix(y_test, y_pred_pondere)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Matrice de Confusion pour le Modèle Forêt Aléatoire Pondéré")
    plt.xlabel("Prédictions")
    plt.ylabel("Véritables Étiquettes")
    plt.show()

    # Étapes 14 à 15 : Entraîner et évaluer le modèle XGBoost
    modele_xgb = XGBClassifier(n_estimators=100, random_state=42)
    modele_xgb.fit(X_train, y_train)

    y_pred_xgb = modele_xgb.predict(X_test)
    print("Rapport de Classification pour XGBoost :\n", classification_report(y_test, y_pred_xgb))
    print("Score d'Exactitude pour XGBoost :", accuracy_score(y_test, y_pred_xgb))

    # Étapes 16 à 19 : Optimisation des hyperparamètres avec GridSearchCV
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                               param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)

    meilleurs_params = grid_search.best_params_
    print("Meilleurs paramètres trouvés par GridSearch :", meilleurs_params)

    modele_rf_optimal = RandomForestClassifier(**meilleurs_params, random_state=42)
    modele_rf_optimal.fit(X_train, y_train)

    y_pred_optimal = modele_rf_optimal.predict(X_test)
    print("Rapport de Classification pour la Forêt Aléatoire Optimisée :\n", classification_report(y_test, y_pred_optimal))
    print("Score d'Exactitude pour la Forêt Aléatoire Optimisée :", accuracy_score(y_test, y_pred_optimal))

    cm_optimal = confusion_matrix(y_test, y_pred_optimal)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm_optimal, annot=True, fmt="d", cmap="Blues")
    plt.title("Matrice de Confusion pour le Modèle Forêt Aléatoire Optimisé")
    plt.xlabel("Prédictions")
    plt.ylabel("Véritables Étiquettes")
    plt.show()

if __name__ == "__main__":
    main()
