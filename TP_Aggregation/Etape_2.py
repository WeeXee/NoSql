from pymongo import MongoClient
import random

# Connexion à la base de données et à la collection

client = MongoClient('mongodb+srv://paulinecabee:AqwPmn09!@nosqlmodule.gekwzev.mongodb.net/27017')
db = client.pokemonDB
collection = db.pokemons

# Ajout des statistiques d'attaque et de défense

for pokemons in collection.find():
    attack = random.randint(1, 100)
    defense = random.randint(1, 100)
    collection.update_one(
        {'_id': pokemons['_id']},
        {'$set': {'stats': {'attack': attack, 'defense': defense}}}
    )

# Calcul de la moyenne des HP et des CP pour l'ensemble des Pokémon
average_stats_all = collection.aggregate([
    {
        '$group': {
            '_id': None,
            'avg_hp': {'$avg': '$Max HP'},
            'avg_cp': {'$avg': '$Max CP'}
        }
    }
])

for stats in average_stats_all:
    avg_hp_all = stats['avg_hp']
    avg_cp_all = stats['avg_cp']

print(f"Moyenne des HP pour tous les Pokémon : {avg_hp_all}")
print(f"Moyenne des CP pour tous les Pokémon : {avg_cp_all}")

# Calcul de la moyenne des HP et des CP par type de Pokémon

average_stats_by_type = collection.aggregate([
    {
        '$group': {
            '_id': '$Type 1',
            'avg_hp': {'$avg': '$Max HP'},
            'avg_cp': {'$avg': '$Max CP'}
        }
    }
])

print("Moyennes des HP et des CP par type de Pokémon :")
for stats in average_stats_by_type:
    pokemon_type = stats['_id']
    avg_hp_type = stats['avg_hp']
    avg_cp_type = stats['avg_cp']
    print(f"Type : {pokemon_type}, Moyenne HP : {avg_hp_type}, Moyenne CP : {avg_cp_type}")


# Trouver le Pokémon ayant le HP et le CP les plus élevés

pokemon_highest_stats = collection.find_one(
    sort=[('Max HP', -1), ('Max CP', -1)]
)

if pokemon_highest_stats:
    name_highest_stats = pokemon_highest_stats['Name']
    hp_highest_stats = pokemon_highest_stats['Max HP']
    cp_highest_stats = pokemon_highest_stats['Max CP']
    print(f"Pokemon avec le HP le plus élevé : {name_highest_stats}, HP : {hp_highest_stats}")
    print(f"Pokemon avec le CP le plus élevé : {name_highest_stats}, CP : {cp_highest_stats}")
else:
    print("Aucun Pokémon trouvé.")
