# detection_scenarios_accidents.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

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

    # Étape 2 : Charger les données depuis la base de données
    requete = """
    SELECT c.lum, c.col, l.catr, u.grav
    FROM caracteristiques c
    JOIN lieux l ON c.Num_Acc = l.Num_Acc
    JOIN usagers u ON c.Num_Acc = u.Num_Acc
    WHERE c.lum IS NOT NULL AND c.col IS NOT NULL AND l.catr IS NOT NULL AND u.grav IS NOT NULL;
    """

    df = pd.read_sql(requete, moteur)

    # Étapes 3 à 5 : Prétraitement et clustering
    encodeur = LabelEncoder()
    for colonne in ['lum', 'col', 'catr']:
        df[colonne] = encodeur.fit_transform(df[colonne])

    standardiseur = StandardScaler()
    caracteristiques_standardisees = standardiseur.fit_transform(df[['lum', 'col', 'catr']])

    kmeans = KMeans(n_clusters=5, random_state=42)
    df['cluster'] = kmeans.fit_predict(caracteristiques_standardisees)

    # Étapes 6 à 7 : Analyse et visualisation des clusters
    gravite_clusters = df.groupby('cluster')['grav'].mean().reset_index().rename(columns={'grav': 'gravite_moyenne'})
    df = df.merge(gravite_clusters, on='cluster', how='left')

    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x='lum', y='col', hue='cluster', palette='viridis')
    plt.title("Clustering des Scénarios d'Accidents par Conditions de Luminosité et Type de Collision")
    plt.xlabel("Conditions de Luminosité (encodées)")
    plt.ylabel("Type de Collision (encodé)")
    plt.show()

    for idx, ligne in gravite_clusters.iterrows():
        print(f"Cluster {ligne['cluster']}: Niveau de gravité moyen = {ligne['gravite_moyenne']:.2f}")

if __name__ == "__main__":
    main()
