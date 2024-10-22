# analyse_geographique_securite_routiere.py

import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Étape 1 : Paramètres de connexion à la base de données
    TYPE_BASE_DONNEES = 'postgresql'
    DBAPI = 'psycopg2'
    HOTE = 'localhost'
    UTILISATEUR = 'postgres'
    MOT_DE_PASSE = ''  # Remplacez par votre mot de passe
    PORT = 5432
    BASE_DONNEES = 'postgres'

    moteur = create_engine(f"{TYPE_BASE_DONNEES}+{DBAPI}://{UTILISATEUR}:{MOT_DE_PASSE}@{HOTE}:{PORT}/{BASE_DONNEES}")

    # Étape 2 : Charger les données depuis la base de données
    requete = """
    SELECT c.Num_Acc, c.jour, c.mois, c.an, c.hrmn, c.lum, c.dep, l.catr, l.circ, l.nbv, l.surf, l.situ, l.vma, 
           v.catv, u.catu, u.grav, c.atm
    FROM caracteristiques c
    JOIN lieux l ON c.Num_Acc = l.Num_Acc
    JOIN vehicules v ON c.Num_Acc = v.Num_Acc
    JOIN usagers u ON c.Num_Acc = u.Num_Acc;
    """

    df = pd.read_sql(requete, moteur)

    # Étapes 3 à 4 : Analyse de la gravité par conditions météorologiques et type de route
    grav_par_atm = df.groupby('atm')['grav'].value_counts(normalize=True).unstack().fillna(0)
    grav_par_catr = df.groupby('catr')['grav'].value_counts(normalize=True).unstack().fillna(0)

    print("Répartition des gravités par conditions météorologiques (atm):")
    print(grav_par_atm)

    print("\nRépartition des gravités par type de route (catr):")
    print(grav_par_catr)

    # Étapes 5 à 6 : Visualisations
    plt.figure(figsize=(10, 6))
    sns.heatmap(grav_par_atm, annot=True, cmap="coolwarm")
    plt.title("Gravité des accidents par conditions météorologiques")
    plt.xlabel("Gravité")
    plt.ylabel("Conditions Météorologiques (atm)")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.heatmap(grav_par_catr, annot=True, cmap="coolwarm")
    plt.title("Gravité des accidents par type de route")
    plt.xlabel("Gravité")
    plt.ylabel("Type de Route (catr)")
    plt.show()

    # Étapes 7 à 8 : Analyse des corrélations
    variables_interet = ['lum', 'atm', 'catr', 'circ', 'nbv', 'surf', 'situ', 'vma', 'catv', 'grav']
    df_corr = df[variables_interet].copy()

    matrice_corr = df_corr.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(matrice_corr, annot=True, cmap="coolwarm", center=0)
    plt.title("Matrice de corrélation des variables et de la gravité des accidents")
    plt.show()

if __name__ == "__main__":
    main()
