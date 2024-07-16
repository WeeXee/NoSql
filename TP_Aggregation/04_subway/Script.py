from pymongo import MongoClient

# Connexion à la base de données
client = MongoClient('mongodb+srv://paulinecabee:AqwPmn09!@nosqlmodule.gekwzev.mongodb.net/27017')
db = client.sandwichDB
commandes = db.commandes

# Menu Principal
def afficher_menu():
    print("Menu Principal")
    print("1. Nouvelle commande")
    print("2. Voir le chiffre d'affaires")
    print("3. Quitter")

# Création de Commande
def nouvelle_commande():
    ingredients_disponibles = ["Jambon", "Fromage", "Salade", "Tomate", "Poulet"]
    sauces_disponibles = ["Mayonnaise", "Ketchup", "Moutarde", "Barbecue"]

    print("Choisissez vos ingrédients (séparés par des virgules) :")
    for idx, ingredient in enumerate(ingredients_disponibles, 1):
        print(f"{idx}. {ingredient}")

    choix_ingredients = input("Ingrédients : ")
    ingredients_choisis = [ingredients_disponibles[int(i)-1] for i in choix_ingredients.split(",")]

    print("Choisissez une sauce :")
    for idx, sauce in enumerate(sauces_disponibles, 1):
        print(f"{idx}. {sauce}")

    choix_sauce = int(input("Sauce : "))
    sauce_choisie = sauces_disponibles[choix_sauce-1]

    commande = {
        "ingredients": ingredients_choisis,
        "sauce": sauce_choisie,
        "montant": len(ingredients_choisis) * 2 + 1  # Prix arbitraire: 2 par ingrédient + 1 pour la sauce
    }

    commandes.insert_one(commande)
    print("Commande enregistrée avec succès!")

# Calcul du Chiffre d'Affaires
def voir_chiffre_affaires():
    total_chiffre_affaires = commandes.aggregate([
        {
            '$group': {
                '_id': None,
                'total': {'$sum': '$montant'}
            }
        }
    ])

    for result in total_chiffre_affaires:
        print(f"Chiffre d'affaires total : {result['total']}")

# Fonction principale pour exécuter l'application
def main():
    while True:
        afficher_menu()
        choix = int(input("Votre choix : "))

        if choix == 1:
            nouvelle_commande()
        elif choix == 2:
            voir_chiffre_affaires()
        elif choix == 3:
            print("Merci et à bientôt!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
