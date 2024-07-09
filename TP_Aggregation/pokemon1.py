from pymongo import MongoClient
import random

# Connexion à la base de données et à la collection

client = MongoClient('mongodb+srv://paulinecabee:AqwPmn09!@nosqlmodule.gekwzev.mongodb.net/27017')
db = client.pokemonDB
collection = db.pokemons

# Ajout des statistiques d'attaque et de défense

for pokemon in collection.find():
    attack = random.randint(1, 100)
    defense = random.randint(1, 100)
    collection.update_one(
        {'_id': pokemon['_id']},
        {'$set': {'stats': {'attack': attack, 'defense': defense}}}
    )
