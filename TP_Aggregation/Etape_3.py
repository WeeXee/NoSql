from pymongo import MongoClient
import random

# Connexion à la base de données et à la collection

client = MongoClient('mongodb+srv://paulinecabee:AqwPmn09!@nosqlmodule.gekwzev.mongodb.net/27017')
db = client.pokemonDB
collection = db.pokemons

# Identifier tous les Pokémon avec plus de 50 d'attaques et les afficher

for pokemons in collection.find():
    if pokemons['stats']['attack'] > 50:
        print(f"{pokemons['Name']} : {pokemons['stats']['attack']}")


# Calcul de la moyenne des CP pour tous les Pokémon
average_cp_result = collection.aggregate([
    {
        '$group': {
            '_id': None,
            'avg_cp': {'$avg': '$Max CP'}
        }
    }
])

# Extraire la moyenne des CP
avg_cp = None
for stats in average_cp_result:
    avg_cp = stats['avg_cp']

if avg_cp is not None:
    print(f"Moyenne des CP pour tous les Pokémon : {avg_cp}")

    # Sélection des Pokémon avec un CP supérieur à la moyenne des CP
    pokemon_high_cp = collection.find({
        'Max CP': {'$gt': avg_cp}
    })

    high_cp_pokemons_list = list(pokemon_high_cp)
    if not high_cp_pokemons_list:
        print("Aucun Pokémon trouvé avec un CP supérieur à la moyenne:")
    else:
        print("Pokémon avec un CP supérieur à la moyenne :")
        for pokemon in high_cp_pokemons_list:
            print(f"{pokemon['Name']}: {pokemon['Max CP']}")
else:
    print("Impossible de calculer la moyenne des CP.")
