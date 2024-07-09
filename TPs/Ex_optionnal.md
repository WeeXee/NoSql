# TP - Manipulation de Documents Imbriqués

## Partie 1: Préparation

![img](/TPs/images/Optionnal/1.png)

## Partie 2: Insertion de Données
Création d'une nouvelle classe

![img](/TPs/images/Optionnal/6.png)

## Partie 3: Requêtes sur Documents Imbriqués

```mongo
db.classes.aggregate([
  { $match: { "className": "Mathematics 101" } },
  { $unwind: "$students" },
  { $match: { "students.grades.final": { $gt: 85 } } }
]);
```

![img](/TPs/images/Optionnal/7.png)

```mongo
db.classes.updateOne(
  { "className": "Mathematics 101", "students.name": "Bob" },
  { $inc: { "students.$.grades.final": 5 } }
);

```

![img](/TPs/images/Optionnal/8.png)

## Partie 4: Ajout et Suppression d'Éléments Imbriqués

Ajout d'un étudiant 

```mongo
db.classes.updateOne(
  { "className": "Mathematics 101" },
  { $push: { "students": { "name": "Charlie", "age": 23, "grades": { "midterm": 82, "final": 88 } } } }
)
```

Suppression d'un étudiant
```mongo
db.classes.updateOne(
  { "className": "Mathematics 101" },
  { $pull: { "students": { "name": "Alice" } } }
)
```

![img](/TPs/images/Optionnal/alice_supp.png)

## Partie 5: Pour aller plus loin avec les Agrégations

Calcul de la moyenne
```mongo
db.classes.aggregate([
  { $match: { "className": "Mathematics 101" } },
  { $unwind: "$students" },
  { $group: {
      _id: "$className",
      averageFinalGrade: { $avg: "$students.grades.final" }
    }
  }
])
```

Trouver la note
```mongo
db.classes.aggregate([
  { $match: { "className": "Mathematics 101" } },
  { $unwind: "$students" },
  { $group: {
      _id: "$className",
      maxFinalGrade: { $max: "$students.grades.final" }
    }
  }
])
```

Validation

```mongo
db.classes.find().pretty()
``` 
