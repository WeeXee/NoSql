# TP - MongoDB Titanic

Ces exercices avancés vous permettront de manipuler et d'analyser les données du Titanic à partir du fichier titanic.csv en utilisant MongoDB.

## Préparation
Importez les données du fichier titanic.csv dans votre base de données MongoDB avant de commencer les exercices.

## Exercice 1: Importation et Création de la Collection
Objectif : Importer les données du fichier titanic.csv dans une collection Passengers de la base de données TitanicDB.

### Instructions
Créez une base de données nommée TitanicDB.
Importez les données de titanic.csv dans une collection nommée Passengers.

![img](/TPs/images/Titanic/create.png)

## Exercice 2: Analyse des Données
Objectif : Effectuer des opérations de lecture et d'analyse sur les données.

### Instructions

* Comptez le nombre total de passagers.

![img](/TPs/images/Titanic/Nb_passagers.png)

* Trouvez combien de passagers ont survécu.

![img](/TPs/images/Titanic/survived.png)

* Trouvez le nombre de passagers femmes.

![img](/TPs/images/Titanic/female.png
)
* Trouvez le nombre de passagers avec au moins 3 enfants.

![img](/TPs/images/Titanic/enfants.png)

## Exercice 3: Mise à Jour de Données
Objectif : Corriger ou ajouter des informations à certains documents.

### Instructions

Mettez à jour les documents pour lesquels le port d'embarquement est manquant, en supposant qu'ils sont montés à bord à Southampton.

* Après verification il n'y a pas de champs vides donc nous pouvons passer à la suite

Ajoutez un champ rescued avec la valeur true pour tous les passagers qui ont survécu.

![img](/TPs/images/Titanic/resqued.png)

## Exercice 4: Requêtes Complexes
Objectif : Effectuer des requêtes plus complexes pour analyser les données.

### Instructions

Sélectionnez les noms des 10 passagers les plus jeunes.

```markdown
$match { "Age": { "$ne": null } }
$sort { "Age": 1 }
$limit 10
$project { "Name": 1, "Age": 1, "_id": 0 }
```
![img](/TPs/images/Titanic/jeunes.png)

Identifiez les passagers qui n'ont pas survécu et qui étaient dans la 2e classe.

![img](/TPs/images/Titanic/2nd.png)

```markdown
{ Survived:0 , "Pclass": 2 }
```

## Exercice 5: Suppression de Données
Objectif : Supprimer des données spécifiques de la base de données.

### Instructions

Supprimez les enregistrements des passagers qui n'ont pas survécu et dont l'âge est inconnu.

![img](/TPs/images/Titanic/delete.png)

## Exercice 6: Mise à Jour en Masse
Objectif : Augmenter l'âge de tous les passagers de 1 an.

### Instructions
Utilisez une opération de mise à jour pour augmenter la valeur du champ Age de 1 pour tous les documents.

![inc](/TPs/images/Titanic/age+1.png)

## Exercice 7: Suppression Conditionnelle
Objectif : Supprimer les enregistrements des passagers qui n'ont pas de numéro de billet (Ticket).

### Instructions
Supprimez tous les documents où le champ Ticket est absent ou vide.

* Après verification il n'y a pas de champs vides donc nous pouvons passer à la suite

## Bonus: Utiliser les REGEX
Objectif : Utiliser une regex pour trouver tous les passagers selon une condition.

### Instructions
Utiliser une regex pour trouver tous les passagers qui porte le titre de Dr.

![img](/TPs/images/Titanic/regex.png)