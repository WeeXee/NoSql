# TP - Exercice Avancé sur la Base de Données Pokémon GO

Cet exercice propose une série de tâches pour explorer les fonctionnalités avancées de MongoDB, en utilisant la collection Pokémon GO. Les étapes couvrent l'ajout de données, l'agrégation de statistiques, et l'analyse de documents.

## Étape 1: Ajout de Statistiques Aléatoires

- Parcourez chaque document de la collection pokemonGO.
- Générez des statistiques aléatoires pour l'attaque et la défense (valeurs entre 1 et 100).
- Mettez à jour chaque Pokémon avec ces nouvelles statistiques sous un objet stats.

J'ai donc installé python, puis pip, pour ensuite écrire des scripts pour les exercices suivants.

[Script python](/TP_Aggregation/Etape_2.py)

- Enrichir chaque document Pokémon avec des statistiques d'attaque et de défense générées aléatoirement.

![img](/TP_Aggregation/images/1.png)

## Étape 2: Agrégation des Statistiques HP et CP

[Script python](/TP_Aggregation/Etape_2.py)

- Calculez la moyenne des HP et des CP pour l'ensemble des Pokémon.

![img](/TP_Aggregation/images/2.png)

- Calculez la moyenne des HP et des CP par type.

![img](/TP_Aggregation/images/3.png)

- Déterminez le Pokémon ayant le HP et le CP les plus élevés.

![img](/TP_Aggregation/images/4.png)

## Étape 3: Lecture de Données sur les Documents

- Identifiez tous les Pokémons avec plus de 50 d'attaques.

[Script python](/TP_Aggregation/Etape_3.py)

![img](/TP_Aggregation/images/5.png)