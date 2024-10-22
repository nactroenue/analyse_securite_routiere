# main.py

import analyse_gravite_accidents
import distribution_temporelle_accidents
import analyse_comportements_risques_utilisateurs
import detection_scenarios_accidents
import analyse_geographique_securite_routiere

def main():
    print("Début de l'analyse de la sécurité routière en France.")

    try:
        print("\n--- Analyse de la Gravité des Accidents ---")
        analyse_gravite_accidents.main()
    except Exception as e:
        print(f"Une erreur est survenue lors de l'analyse de la gravité des accidents : {e}")

    try:
        print("\n--- Distribution Temporelle des Accidents ---")
        distribution_temporelle_accidents.main()
    except Exception as e:
        print(f"Une erreur est survenue lors de la distribution temporelle des accidents : {e}")

    try:
        print("\n--- Analyse des Comportements à Risque des Utilisateurs ---")
        analyse_comportements_risques_utilisateurs.main()
    except Exception as e:
        print(f"Une erreur est survenue lors de l'analyse des comportements à risque : {e}")

    try:
        print("\n--- Détection des Scénarios d'Accidents ---")
        detection_scenarios_accidents.main()
    except Exception as e:
        print(f"Une erreur est survenue lors de la détection des scénarios d'accidents : {e}")

    try:
        print("\n--- Analyse Géographique de la Sécurité Routière ---")
        analyse_geographique_securite_routiere.main()
    except Exception as e:
        print(f"Une erreur est survenue lors de l'analyse géographique : {e}")

    print("\nAnalyse terminée.")

if __name__ == "__main__":
    main()
