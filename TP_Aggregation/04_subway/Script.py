from pymongo import MongoClient

# Connexion à la base de données
client = MongoClient('mongodb+srv://paulinecabee:AqwPmn09!@nosqlmodule.gekwzev.mongodb.net/27017')
db = client.Data
subway = db.Subway

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

    email_client = input("Entrez l'email du client : ")
    client_existant = subway.find_one({"email": email_client})

    nouvelle_commande = {
        "idCommande": f"C001",
        "montant": len(ingredients_choisis) * 2 + 1,
        "produits": ingredients_choisis + [sauce_choisie]
    }

    if client_existant:
        nouvelle_commande["idCommande"] = f"C{len(client_existant['commandes'])+1:03d}"
        subway.update_one(
            {"email": email_client},
            {"$push": {"commandes": nouvelle_commande}}
        )
        print("Commande enregistrée avec succès pour le client existant!")
    else:
        nouveau_client = {
            "nom": input("Entrez le nom du client : "),
            "email": email_client,
            "pays": input("Entrez le pays du client : "),
            "commandes": [nouvelle_commande]
        }
        subway.insert_one(nouveau_client)
        print("Client et commande enregistrés avec succès!")

# Calcul du Chiffre d'Affaires
def voir_chiffre_affaires():
    pipeline = [
        {"$unwind": "$commandes"},
        {"$group": {"_id": None, "total": {"$sum": "$commandes.montant"}}}
    ]

    total_chiffre_affaires = subway.aggregate(pipeline)

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
