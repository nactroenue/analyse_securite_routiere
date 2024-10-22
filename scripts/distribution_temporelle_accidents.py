# distribution_temporelle_accidents.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

def main():
    # Étape 1 : Connexion à la base de données
    TYPE_BASE_DONNEES = 'postgresql'
    DBAPI = 'psycopg2'
    HOTE = 'localhost'
    UTILISATEUR = 'postgres'
    MOT_DE_PASSE = ''  # Remplacer par votre mot de passe
    PORT = 5432
    BASE_DONNEES = 'postgres'

    moteur = create_engine(f"{TYPE_BASE_DONNEES}+{DBAPI}://{UTILISATEUR}:{MOT_DE_PASSE}@{HOTE}:{PORT}/{BASE_DONNEES}")

    # Étapes 2 à 5 : Chargement et prétraitement des données
    requete = """
    SELECT jour, mois, hrmn, an
    FROM caracteristiques
    WHERE jour IS NOT NULL AND mois IS NOT NULL AND hrmn IS NOT NULL;
    """
    df = pd.read_sql(requete, moteur)

    def convertir_heure(hrmn_str):
        try:
            heure, minute = map(int, hrmn_str.split(':'))
            return heure + minute / 60
        except:
            return -1

    df['heure_du_jour'] = df['hrmn'].apply(convertir_heure)
    df = df[df['heure_du_jour'] != -1]

    def obtenir_saison(mois):
        if mois in [12, 1, 2]:
            return 'Hiver'
        elif mois in [3, 4, 5]:
            return 'Printemps'
        elif mois in [6, 7, 8]:
            return 'Été'
        else:
            return 'Automne'

    df['saison'] = df['mois'].apply(obtenir_saison)
    df['jour_de_la_semaine'] = (df['jour'] % 7) + 1

    # Étapes 6 à 8 : Visualisations
    plt.figure(figsize=(14, 6))
    sns.histplot(data=df, x='heure_du_jour', bins=24, kde=True)
    plt.title("Distribution des Accidents par Heure de la Journée")
    plt.xlabel("Heure de la Journée")
    plt.ylabel("Nombre d'Accidents")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='jour_de_la_semaine', palette='coolwarm')
    plt.title("Distribution des Accidents par Jour de la Semaine")
    plt.xlabel("Jour de la Semaine (1=Lundi, 7=Dimanche)")
    plt.ylabel("Nombre d'Accidents")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='saison', palette='viridis')
    plt.title("Distribution des Accidents par Saison")
    plt.xlabel("Saison")
    plt.ylabel("Nombre d'Accidents")
    plt.grid(True)
    plt.show()

    # Statistiques de synthèse
    print("Nombre d'Accidents par Heure de la Journée :")
    print(df['heure_du_jour'].value_counts().sort_index())

    print("\nNombre d'Accidents par Jour de la Semaine :")
    print(df['jour_de_la_semaine'].value_counts().sort_index())

    print("\nNombre d'Accidents par Saison :")
    print(df['saison'].value_counts().sort_index())

if __name__ == "__main__":
    main()
