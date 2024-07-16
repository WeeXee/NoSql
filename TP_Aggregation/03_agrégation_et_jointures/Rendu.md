# Exercice MongoDB : Manipulation et Agrégation de Données de Commandes
Cet exercice vous guidera à travers le processus d'insertion de données de commandes dans MongoDB, la réalisation d'agrégations pour analyser ces données, puis l'utilisation de jointures pour intégrer des informations depuis une collection de clients. Vous travaillerez avec deux collections : commandes pour les détails des commandes et clients pour les informations sur les clients.

## Objectif
L'objectif est de pratiquer l'insertion de données, les agrégations basiques et avancées, ainsi que les jointures entre collections dans MongoDB.

## Partie 1: Insertion des Données de Commandes
Créez une nouvelle collection nommée commandes.
Insérez les données des commandes fournies dans la collection commandes.

[Script python](/TP_Aggregation/03_agrégation_et_jointures/Script.py)


## Partie 2: Agrégations Classiques
Calculez le montant total des ventes.
Trouvez le nombre moyen de produits par commande.
Déterminez le montant maximum d'une commande.

[Script python](/TP_Aggregation/03_agrégation_et_jointures/Script.py)



## Partie 3: Jointure avec la Collection Clients
Utilisez l'opération $lookup pour joindre les collections commandes et clients sur le champ idClient.
Affichez le nom du client avec le détail de chaque commande.

[Script python](/TP_Aggregation/03_agrégation_et_jointures/Script.py)



## Partie 4: Agrégations Plus Complexes
Après avoir joint les collections, effectuez des agrégations plus complexes pour obtenir des insights approfondis.

[Script python](/TP_Aggregation/03_agrégation_et_jointures/Script.py)

