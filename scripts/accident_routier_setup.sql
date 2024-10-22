-- Création de la base de données accident_routier
CREATE DATABASE accident_routier;

-- Création de la table caracteristiques, qui contient les informations générales sur les accidents
CREATE TABLE caracteristiques (
    Num_Acc VARCHAR PRIMARY KEY,         -- Identifiant de l’accident
    jour INT,                            -- Jour de l'accident
    mois INT,                            -- Mois de l'accident
    an INT,                              -- Année de l'accident
    hrmn VARCHAR,                        -- Heure et minutes de l'accident
    lum INT,                             -- Conditions d’éclairage
    dep VARCHAR,                         -- Département
    com VARCHAR,                         -- Commune
    agg INT,                             -- Localisation (en ou hors agglomération)
    int INT,                             -- Type d'intersection
    atm INT,                             -- Conditions atmosphériques
    col INT,                             -- Type de collision
    adr VARCHAR,                         -- Adresse (optionnel)
    lat FLOAT,                           -- Latitude (coordonnées GPS)
    long FLOAT						     -- Longitude (coordonnées GPS)
);

-- Création de la table lieux, qui contient les informations sur les routes où se sont produits les accidents
CREATE TABLE lieux (
    Num_Acc VARCHAR PRIMARY KEY,         -- Identifiant de l’accident
    catr INT,                            -- Catégorie de route
    voie VARCHAR,                        -- Numéro de la route
    v1 VARCHAR,                          -- Indice numérique du numéro de route
    v2 VARCHAR,                          -- Lettre indice alphanumérique de la route
    circ INT,                            -- Régime de circulation
    nbv INT,                             -- Nombre total de voies de circulation
    vosp INT,                            -- Existence d’une voie réservée
    prof INT,                            -- Profil en long de la route
    pr INT,                              -- Numéro du PR de rattachement
    pr1 INT,                             -- Distance en mètres au PR
    plan INT,                            -- Tracé en plan
    larrout FLOAT,                       -- Largeur de la chaussée affectée à la circulation des véhicules en m
    surf INT,                            -- État de la surface
    infra INT,                           -- Aménagement - Infrastructure
    situ INT,                            -- Situation de l’accident
    vma INT                              -- Vitesse maximale autorisée
);

-- Création de la table vehicules, qui contient les informations sur les véhicules impliqués dans les accidents
CREATE TABLE vehicules (
    Num_Acc VARCHAR,                     -- Identifiant de l’accident (jointure avec `caracteristiques`)
    id_vehicule VARCHAR,                 -- Identifiant du véhicule
    num_veh VARCHAR,                     -- Identifiant alphanumérique du véhicule
    senc INT,                            -- Sens de circulation
    catv INT,                            -- Catégorie de véhicule
    obs INT,                             -- Obstacle fixe heurté
    obsm INT,                            -- Obstacle mobile heurté
    choc INT,                            -- Point de choc initial
    manv INT,                            -- Manoeuvre avant l’accident
    motor INT,                           -- Type de motorisation du véhicule
    PRIMARY KEY (Num_Acc, id_vehicule)   -- Clé primaire composite pour différencier les véhicules par accident
);

-- Création de la table usagers, qui contient les informations sur les usagers impliqués dans les accidents
CREATE TABLE usagers (
    Num_Acc VARCHAR,                     -- Identifiant de l’accident (jointure avec `caracteristiques`)
    id_usager VARCHAR,                   -- Identifiant unique de l’usager
    id_vehicule VARCHAR,                 -- Identifiant du véhicule associé à l’usager
    catu INT,                            -- Catégorie d’usager (conducteur, passager, piéton)
    grav INT,                            -- Gravité des blessures de l’usager
    sexe INT,                            -- Sexe de l’usager
    An_nais INT,                         -- Année de naissance de l’usager
    PRIMARY KEY (Num_Acc, id_usager)     -- Clé primaire composite pour chaque usager unique dans un accident
);

-- Importation des données dans la table caracteristiques à partir d'un fichier CSV
COPY caracteristiques FROM 'C:\Users\Public\accidentroutiere\analyse_securite_routiere\data\carcteristiques.csv' DELIMITER ',' CSV HEADER ENCODING 'LATIN1';

-- Importation des données dans la table lieux à partir d'un fichier CSV
COPY caracteristiques FROM 'C:\Users\Public\accidentroutiere\analyse_securite_routiere\data\lieux.csv' DELIMITER ',' CSV HEADER ENCODING 'LATIN1';

-- Importation des données dans la table vehicules à partir d'un fichier CSV
COPY vehicules FROM 'C:\Users\Public\accidentroutiere\analyse_securite_routiere\data\vehicules.csv' DELIMITER ',' CSV HEADER ENCODING 'LATIN1';

-- Importation des données dans la table usagers à partir d'un fichier CSV
COPY usagers FROM 'C:\Users\Public\accidentroutiere\analyse_securite_routiere\data\usagers.csv' DELIMITER ',' CSV HEADER ENCODING 'LATIN1';


