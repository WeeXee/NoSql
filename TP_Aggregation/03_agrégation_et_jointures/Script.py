from pymongo import MongoClient

# Connexion à la base de données et à la collection
client = MongoClient('mongodb+srv://paulinecabee:AqwPmn09!@nosqlmodule.gekwzev.mongodb.net/27017')
db = client.ventesDB

# Partie 1: Insertion des Données de Commandes
commandes = db.commandes
clients = db.clients

# Exemples de données à insérer (ajuster selon les besoins)
commandes.insert_many([
    {
        "idCommande": 1,
        "idClient": 1,
        "montant": 150,
        "produits": [
            {"nom": "Produit A", "quantite": 2},
            {"nom": "Produit B", "quantite": 3}
        ]
    },
    {
        "idCommande": 2,
        "idClient": 2,
        "montant": 200,
        "produits": [
            {"nom": "Produit A", "quantite": 1},
            {"nom": "Produit C", "quantite": 4}
        ]
    },
    # Ajouter d'autres commandes ici
])

# Partie 2: Agrégations Classiques

# Calcul du montant total des ventes
total_sales = commandes.aggregate([
    {
        '$group': {
            '_id': None,
            'total_ventes': {'$sum': '$montant'}
        }
    }
])

for sale in total_sales:
    print(f"Montant total des ventes : {sale['total_ventes']}")

# Nombre moyen de produits par commande
average_products_per_order = commandes.aggregate([
    {
        '$unwind': '$produits'
    },
    {
        '$group': {
            '_id': '$idCommande',
            'total_produits': {'$sum': '$produits.quantite'}
        }
    },
    {
        '$group': {
            '_id': None,
            'produits_moyen': {'$avg': '$total_produits'}
        }
    }
])

for avg in average_products_per_order:
    print(f"Nombre moyen de produits par commande : {avg['produits_moyen']}")

# Montant maximum d'une commande
max_order_amount = commandes.aggregate([
    {
        '$group': {
            '_id': None,
            'max_montant': {'$max': '$montant'}
        }
    }
])

for max_order in max_order_amount:
    print(f"Montant maximum d'une commande : {max_order['max_montant']}")

# Partie 3: Jointure avec la Collection Clients

# Utilisation de $lookup pour joindre les collections commandes et clients
orders_with_clients = commandes.aggregate([
    {
        '$lookup': {
            'from': 'clients',
            'localField': 'idClient',
            'foreignField': 'idClient',
            'as': 'details_client'
        }
    },
    {
        '$unwind': '$details_client'
    }
])

print("Détails des commandes avec informations sur les clients :")
for order in orders_with_clients:
    print(f"Commande ID : {order['idCommande']}, Client : {order['details_client']['nom']}, Montant : {order['montant']}, Produits : {order['produits']}")

# Partie 4: Agrégations Plus Complexes

# Montant total des commandes par client
total_sales_by_client = commandes.aggregate([
    {
        '$group': {
            '_id': '$idClient',
            'total_ventes': {'$sum': '$montant'}
        }
    },
    {
        '$lookup': {
            'from': 'clients',
            'localField': '_id',
            'foreignField': 'idClient',
            'as': 'client_details'
        }
    },
    {
        '$unwind': '$client_details'
    },
    {
        '$project': {
            'client': '$client_details.nom',
            'total_ventes': 1
        }
    }
])

print("Montant total des commandes par client :")
for client in total_sales_by_client:
    print(f"Client : {client['client']}, Total des ventes : {client['total_ventes']}")

# Produit le plus vendu
most_sold_product = commandes.aggregate([
    {
        '$unwind': '$produits'
    },
    {
        '$group': {
            '_id': '$produits.nom',
            'total_quantite': {'$sum': '$produits.quantite'}
        }
    },
    {
        '$sort': {'total_quantite': -1}
    },
    {
        '$limit': 1
    }
])

for product in most_sold_product:
    print(f"Produit le plus vendu : {product['_id']}, Quantité totale : {product['total_quantite']}")

# Client ayant effectué le plus grand nombre de commandes
client_most_orders = commandes.aggregate([
    {
        '$group': {
            '_id': '$idClient',
            'total_commandes': {'$sum': 1}
        }
    },
    {
        '$sort': {'total_commandes': -1}
    },
    {
        '$limit': 1
    },
    {
        '$lookup': {
            'from': 'clients',
            'localField': '_id',
            'foreignField': 'idClient',
            'as': 'client_details'
        }
    },
    {
        '$unwind': '$client_details'
    },
    {
        '$project': {
            'client': '$client_details.nom',
            'total_commandes': 1
        }
    }
])

for client in client_most_orders:
    print(f"Client avec le plus grand nombre de commandes : {client['client']}, Nombre de commandes : {client['total_commandes']}")

# Client ayant commandé le plus grand nombre de produits
client_most_products = commandes.aggregate([
    {
        '$unwind': '$produits'
    },
    {
        '$group': {
            '_id': '$idClient',
            'total_produits': {'$sum': '$produits.quantite'}
        }
    },
    {
        '$sort': {'total_produits': -1}
    },
    {
        '$limit': 1
    },
    {
        '$lookup': {
            'from': 'clients',
            'localField': '_id',
            'foreignField': 'idClient',
            'as': 'client_details'
        }
    },
    {
        '$unwind': '$client_details'
    },
    {
        '$project': {
            'client': '$client_details.nom',
            'total_produits': 1
        }
    }
])

for client in client_most_products:
    print(f"Client avec le plus grand nombre de produits commandés : {client['client']}, Nombre de produits : {client['total_produits']}")
