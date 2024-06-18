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