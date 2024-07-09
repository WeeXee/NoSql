from pymongo import MongoClient

# Connexion à la base de données et à la collection

client = MongoClient('mongodb+srv://paulinecabee:AqwPmn09!@nosqlmodule.gekwzev.mongodb.net/27017')
db = client.pokemonDB
collection = db.pokemons

#Calculez la moyenne des statistiques d'attaque et de défense pour chaque Pokémon.

average_stats_all = collection.aggregate([
    {
        '$group': {
            '_id': None,
            'avg_attack': {'$avg': '$stats.attack'},
            'avg_defense': {'$avg': '$stats.defense'}
        }
    }
])

for stats in average_stats_all:
    avg_attack_all = stats['avg_attack']
    avg_defense_all = stats['avg_defense']

print(f"Moyenne des attaques pour tous les Pokémon : {avg_attack_all}")
print(f"Moyenne des défenses pour tous les Pokémon : {avg_defense_all}")

#Comparez les statistiques moyennes d'attaque et de défense de chaque Pokémon groupé par type.

average_stats_by_type = collection.aggregate([
    {
        '$group': {
            '_id': '$Type 1',
            'avg_attack': {'$avg': '$stats.attack'},
            'avg_defense': {'$avg': '$stats.defense'}
        }
    }
])

print("Moyennes des attaques et des défenses par type de Pokémon :")
for stats in average_stats_by_type:
    pokemon_type = stats['_id']
    avg_attack_type = stats['avg_attack']
    avg_defense_type = stats['avg_defense']
    print(f"Type : {pokemon_type}, Moyenne attaque : {avg_attack_type}, Moyenne défense : {avg_defense_type}")

    