from pymongo import MongoClient

# Connexion à la base de données et à la collection
client = MongoClient('mongodb+srv://paulinecabee:AqwPmn09!@nosqlmodule.gekwzev.mongodb.net/27017')
db = client.Data
subway = db.Subway

# Partie 1: Insertion des Données de Commandes
# Exemple d'ajout de clients et commandes (ajuster selon les besoins)
subway.insert_many([
    {
        "_id": 1,
        "nom": "Client A",
        "email": "clienta@email.com",
        "pays": "France",
        "commandes": [
            {
                "idCommande": "C001",
                "montant": 150,
                "produits": ["Produit A", "Produit B"]
            }
        ]
    },
    {
        "_id": 2,
        "nom": "Client B",
        "email": "clientb@email.com",
        "pays": "France",
        "commandes": [
            {
                "idCommande": "C002",
                "montant": 200,
                "produits": ["Produit A", "Produit C"]
            }
        ]
    }
])

# Partie 2: Agrégations Classiques

# Calcul du montant total des ventes
total_sales = subway.aggregate([
    {"$unwind": "$commandes"},
    {"$group": {"_id": None, "total_ventes": {"$sum": "$commandes.montant"}}}
])

for sale in total_sales:
    print(f"Montant total des ventes : {sale['total_ventes']}")

# Nombre moyen de produits par commande
average_products_per_order = subway.aggregate([
    {"$unwind": "$commandes"},
    {"$unwind": "$commandes.produits"},
    {"$group": {"_id": "$commandes.idCommande", "total_produits": {"$sum": 1}}},
    {"$group": {"_id": None, "produits_moyen": {"$avg": "$total_produits"}}}
])

for avg in average_products_per_order:
    print(f"Nombre moyen de produits par commande : {avg['produits_moyen']}")

# Montant maximum d'une commande
max_order_amount = subway.aggregate([
    {"$unwind": "$commandes"},
    {"$group": {"_id": None, "max_montant": {"$max": "$commandes.montant"}}}
])

for max_order in max_order_amount:
    print(f"Montant maximum d'une commande : {max_order['max_montant']}")

# Partie 3: Jointure avec la Collection Clients

# Utilisation de $lookup pour joindre les commandes avec les informations des clients
orders_with_clients = subway.aggregate([
    {"$unwind": "$commandes"},
    {"$lookup": {
        "from": "Subway",
        "localField": "_id",
        "foreignField": "_id",
        "as": "details_client"
    }},
    {"$unwind": "$details_client"},
    {"$project": {
        "idCommande": "$commandes.idCommande",
        "client_nom": "$details_client.nom",
        "montant": "$commandes.montant",
        "produits": "$commandes.produits"
    }}
])

print("Détails des commandes avec informations sur les clients :")
for order in orders_with_clients:
    print(f"Commande ID : {order['idCommande']}, Client : {order['client_nom']}, Montant : {order['montant']}, Produits : {order['produits']}")

# Partie 4: Agrégations Plus Complexes

# Montant total des commandes par client
total_sales_by_client = subway.aggregate([
    {"$unwind": "$commandes"},
    {"$group": {"_id": "$_id", "total_ventes": {"$sum": "$commandes.montant"}}},
    {"$lookup": {
        "from": "Subway",
        "localField": "_id",
        "foreignField": "_id",
        "as": "client_details"
    }},
    {"$unwind": "$client_details"},
    {"$project": {"client": "$client_details.nom", "total_ventes": 1}}
])

print("Montant total des commandes par client :")
for client in total_sales_by_client:
    print(f"Client : {client['client']}, Total des ventes : {client['total_ventes']}")

# Produit le plus vendu
most_sold_product = subway.aggregate([
    {"$unwind": "$commandes"},
    {"$unwind": "$commandes.produits"},
    {"$group": {"_id": "$commandes.produits", "total_quantite": {"$sum": 1}}},
    {"$sort": {"total_quantite": -1}},
    {"$limit": 1}
])

for product in most_sold_product:
    print(f"Produit le plus vendu : {product['_id']}, Quantité totale : {product['total_quantite']}")

# Client ayant effectué le plus grand nombre de commandes
client_most_orders = subway.aggregate([
    {"$unwind": "$commandes"},
    {"$group": {"_id": "$_id", "total_commandes": {"$sum": 1}}},
    {"$sort": {"total_commandes": -1}},
    {"$limit": 1},
    {"$lookup": {
        "from": "Subway",
        "localField": "_id",
        "foreignField": "_id",
        "as": "client_details"
    }},
    {"$unwind": "$client_details"},
    {"$project": {"client": "$client_details.nom", "total_commandes": 1}}
])

for client in client_most_orders:
    print(f"Client avec le plus grand nombre de commandes : {client['client']}, Nombre de commandes : {client['total_commandes']}")

# Client ayant commandé le plus grand nombre de produits
client_most_products = subway.aggregate([
    {"$unwind": "$commandes"},
    {"$unwind": "$commandes.produits"},
    {"$group": {"_id": "$_id", "total_produits": {"$sum": 1}}},
    {"$sort": {"total_produits": -1}},
    {"$limit": 1},
    {"$lookup": {
        "from": "Subway",
        "localField": "_id",
        "foreignField": "_id",
        "as": "client_details"
    }},
    {"$unwind": "$client_details"},
    {"$project": {"client": "$client_details.nom", "total_produits": 1}}
])

for client in client_most_products:
    print(f"Client avec le plus grand nombre de produits commandés : {client['client']}, Nombre de produits : {client['total_produits']}")
