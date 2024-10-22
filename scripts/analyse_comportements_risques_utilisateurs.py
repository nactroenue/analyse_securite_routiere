# analyse_comportements_risques_utilisateurs.py

import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Étape 1 : Créer la connexion SQLAlchemy
    TYPE_BASE_DONNEES = 'postgresql'
    DBAPI = 'psycopg2'
    HOTE = 'localhost'
    UTILISATEUR = 'postgres'
    MOT_DE_PASSE = ''
    PORT = 5432
    BASE_DONNEES = 'postgres'

    moteur = create_engine(f"{TYPE_BASE_DONNEES}+{DBAPI}://{UTILISATEUR}:{MOT_DE_PASSE}@{HOTE}:{PORT}/{BASE_DONNEES}")

    # Étapes 2 à 3 : Charger et analyser les données des utilisateurs
    requete_utilisateurs = """
    SELECT an_nais, sexe, catu 
    FROM usagers
    WHERE an_nais IS NOT NULL AND an_nais BETWEEN 1900 AND 2020;
    """
    df_utilisateurs = pd.read_sql(requete_utilisateurs, moteur)
    df_utilisateurs['age'] = 2020 - df_utilisateurs['an_nais']
    agg_utilisateurs = df_utilisateurs.groupby(['age', 'sexe']).size().reset_index(name='nombre_accidents')
    tableau_croise_utilisateurs = agg_utilisateurs.pivot_table(index='age', columns='sexe', values='nombre_accidents', fill_value=0)

    plt.figure(figsize=(14, 8))
    sns.heatmap(tableau_croise_utilisateurs, annot=False, cmap='inferno', linewidths=0.5)
    plt.title("Nombre d'Accidents par Âge et Sexe")
    plt.xlabel("Sexe (-1: Inconnu, 1: Homme, 2: Femme)")
    plt.ylabel("Âge")
    plt.show()

    # Étapes 4 à 5 : Identifier et visualiser les comportements à risque
    requete_vehicules = """
    SELECT manv 
    FROM vehicules
    WHERE manv IS NOT NULL;
    """
    df_vehicules = pd.read_sql(requete_vehicules, moteur)
    df_comportements = df_vehicules['manv'].value_counts().reset_index()
    df_comportements.columns = ['manv', 'nombre']

    plt.figure(figsize=(16, 8))
    sns.barplot(data=df_comportements, x='manv', y='nombre', palette='viridis')
    plt.title("Comportements Risqués Associés aux Accidents")
    plt.xlabel("Code de Manœuvre (manv)")
    plt.ylabel("Nombre d'Accidents")
    plt.show()

if __name__ == "__main__":
    main()
