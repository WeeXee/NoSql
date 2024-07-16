# TP - Exercice d'Agrégation Avancée avec MongoDB

Cet exercice vous guide à travers une série de tâches d'agrégation en utilisant une collection de données sur des clients et leurs commandes dans une base de données fictive ventesDB.

## Contexte

Vous disposez d'une collection clients dans MongoDB, contenant des informations sur 5 clients et leurs commandes respectives. Chaque commande comprend un montant et une liste de produits achetés.

## Tâche 1: Total des Ventes par Client
Calculez le montant total des ventes réalisées par chaque client. Ceci vous permettra de comprendre quel client a contribué le plus au chiffre d'affaires.

[Script python](/TP_Aggregation/02_agregation_avancée/Script.py)


## Tâche 2: Panier Moyen par Commande
Déterminez le panier moyen en termes de nombre de produits par commande pour l'ensemble des clients. Cette métrique vous aidera à estimer la taille moyenne des commandes passées.

[Script python](/TP_Aggregation/02_agregation_avancée/Script.py)


### Tâche 3: Commande Maxi par Client
Trouvez la commande avec le montant le plus élevé pour chaque client. Cela mettra en évidence les clients qui ont effectué au moins une grosse commande.

[Script python](/TP_Aggregation/02_agregation_avancée/Script.py)


### Tâche 4: Répartition de l’Utilisation des Produits
Identifiez le top 3 des produits les plus vendus en termes de quantité sur l'ensemble des commandes. Cette analyse vous aidera à comprendre les préférences des clients et les produits les plus populaires.

[Script python](/TP_Aggregation/02_agregation_avancée/Script.py)



