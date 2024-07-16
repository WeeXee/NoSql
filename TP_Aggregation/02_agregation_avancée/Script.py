from pymongo import MongoClient

# Connexion à la base de données et à la collection
client = MongoClient('mongodb+srv://paulinecabee:AqwPmn09!@nosqlmodule.gekwzev.mongodb.net/27017')
db = client.ventesDB
collection = db.clients

# Tâche 1: Total des Ventes par Client
total_sales_by_client = collection.aggregate([
    {
        '$unwind': '$commandes'
    },
    {
        '$group': {
            '_id': '$nom_client',
            'total_ventes': {'$sum': '$commandes.montant'}
        }
    }
])

print("Total des ventes par client :")
for client in total_sales_by_client:
    nom_client = client['_id']
    total_ventes = client['total_ventes']
    print(f"Client : {nom_client}, Total des ventes : {total_ventes}")

# Tâche 2: Panier Moyen par Commande
average_cart_size = collection.aggregate([
    {
        '$unwind': '$commandes'
    },
    {
        '$group': {
            '_id': None,
            'panier_moyen': {'$avg': {'$size': '$commandes.produits'}}
        }
    }
])

for panier in average_cart_size:
    panier_moyen = panier['panier_moyen']
    print(f"Panier moyen par commande : {panier_moyen}")

# Tâche 3: Commande Maxi par Client
max_order_by_client = collection.aggregate([
    {
        '$unwind': '$commandes'
    },
    {
        '$group': {
            '_id': '$nom_client',
            'commande_maxi': {'$max': '$commandes.montant'}
        }
    }
])

print("Commande la plus élevée par client :")
for client in max_order_by_client:
    nom_client = client['_id']
    commande_maxi = client['commande_maxi']
    print(f"Client : {nom_client}, Commande la plus élevée : {commande_maxi}")

# Tâche 4: Répartition de l’Utilisation des Produits
top_products = collection.aggregate([
    {
        '$unwind': '$commandes'
    },
    {
        '$unwind': '$commandes.produits'
    },
    {
        '$group': {
            '_id': '$commandes.produits.nom',
            'quantite_totale': {'$sum': '$commandes.produits.quantite'}
        }
    },
    {
        '$sort': {'quantite_totale': -1}
    },
    {
        '$limit': 3
    }
])

print("Top 3 des produits les plus vendus :")
for produit in top_products:
    nom_produit = produit['_id']
    quantite_totale = produit['quantite_totale']
    print(f"Produit : {nom_produit}, Quantité totale vendue : {quantite_totale}")
