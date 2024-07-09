from pymongo import MongoClient
import random

# Connexion à la base de données et à la collection

client = MongoClient('mongodb+srv://paulinecabee:AqwPmn09!@nosqlmodule.gekwzev.mongodb.net/27017')
db = client.pokemonDB
collection = db.pokemons

# Calcul de la moyenne des HP et des CP

average_hp_cp = collection.aggregate([
    {'$group': {
        '_id': None,
        'averageHP': {'$avg': '$HP'},
        'averageCP': {'$avg': '$CP'}
    }}
])

for result in average_hp_cp:
    print(f"Moyenne des HP: {result['averageHP']}, Moyenne des CP: {result['averageCP']}")

    average_hp_cp_by_type = collection.aggregate([
    {'$unwind': '$type'},
    {'$group': {
        '_id': '$type',
        'averageHP': {'$avg': '$HP'},
        'averageCP': {'$avg': '$CP'}
    }}
])

for result in average_hp_cp_by_type:
    print(f"Type: {result['_id']}, Moyenne des HP: {result['averageHP']}, Moyenne des CP: {result['averageCP']}")

# Moyenne des HP et des CP par type :

average_hp_cp_by_type = collection.aggregate([
    {'$unwind': '$type'},
    {'$group': {
        '_id': '$type',
        'averageHP': {'$avg': '$HP'},
        'averageCP': {'$avg': '$CP'}
    }}
])

for result in average_hp_cp_by_type:
    print(f"Type: {result['_id']}, Moyenne des HP: {result['averageHP']}, Moyenne des CP: {result['averageCP']}")


# Pokémon ayant le HP et le CP les plus élevés :

highest_hp_pokemon = collection.find().sort('HP', -1).limit(1)
highest_cp_pokemon = collection.find().sort('CP', -1).limit(1)

for pokemon in highest_hp_pokemon:
    print(f"Pokémon avec le plus haut HP: {pokemon['name']}, HP: {pokemon['HP']}")
    
for pokemon in highest_cp_pokemon:
    print(f"Pokémon avec le plus haut CP: {pokemon['name']}, CP: {pokemon['CP']}")
