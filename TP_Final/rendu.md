# TP: Configuration et Gestion de MongoDB avec Docker

## Étape 1: Télécharger l'image Docker de MongoDB
1. **Télécharger l'image Docker de MongoDB depuis Docker Hub:**
   ```bash
   docker pull mongo
   ```

2. **Lancer le conteneur:**

   ![img](/TP_Final/image/2.png)

3. **Vérifier l'état**
   ```bash
      docker ps
      ```
   ![img](/TP_Final//image/1.png) 
   

## Étape 2: Connexion au Conteneur MongoDB
1. **Connectez-vous au conteneur MongoDB avec votre cluster Atlas:**
   ```bash
   docker exec -it 4a309f391676 mongosh "mongodb+srv://cluster0.diuuozc.mongodb.net/" --apiVersion 1 --username pauline --password Passw0rd
   ```

   ![img](/TP_Final/image/3.png)
  

## Étape 3: Créer une Base de Données et des Collections
1. **Créer une nouvelle base de données appelée `Galaxies`:**
   ```javascript
   use Galaxies
   ```

2. **Créer une nouvelle collection appelée `Stars`:**
   ```javascript
   db.createCollection("Stars")
   ```
   ![img](/TP_Final/image/4.png)

3. **Insérer 5 nouveaux documents dans la collection `Stars`:**
   ![img](/TP_Final/image/5.png)

4. **Vérifier que les documents ont été insérés:**
   ```javascript
   db.Stars.find().pretty()
   ```
   ![img](/TP_Final/image/6.png)

5. **Créer une nouvelle collection appelée `Planets`:**
   ```javascript
   db.createCollection("Planets")
   ```

6. **Insérer 5 nouveaux documents dans la collection `Planets`:**

   ![img](/TP_Final/image/7.png)

7. **Créer des index sur le champ `Name` pour les collections `Stars` et `Planets`:**
   ```javascript
   db.Stars.createIndex({ Name: 1 })
   db.Planets.createIndex({ Name: 1 })
   ```

## Étape 4: Sauvegarde et Restauration des Données

Pour sortir de Atlas: Exit

1. **Créer une sauvegarde de la base de données `Galaxies`:**

   ```bash
   docker exec -it 4a bash
   docker exec -it 4a mongodump --db Galaxies --out /backup
   ```

2. **Supprimer la base de données `Galaxies`:**

     Se reconnecter à la db puis:

   ```javascript
   use Galaxies
   db.dropDatabase()
   ```
   ![img](/TP_Final/image/8.png)

3. **Restaurer la base de données `Galaxies` à partir de la sauvegarde et la nommer `Galaxies_Restored`:**
   ```bash
   docker exec -it 4a309f391676 mongorestore --uri "mongodb+srv://pauline:Passw0rd@cluster0.diuuozc.mongodb.net/" --db Galaxies_restore Galaxies
   ```
   ![img](/TP_Final/image/9.png)


4. **Vérifier que la base de données `Galaxies_restore` a été restaurée avec succès:**

   Se reconnecter à la db puis: 

   ```bash 
   docker exec -it 4a309f391676 mongosh "mongodb+srv://cluster0.diuuozc.mongodb.net/" --apiVersion 1 --username pauline --password Passw0rd 
   ```

   Puis vérifier:

   ```javascript
   use Galaxies_restore
   db.Stars.find().pretty()
   ```
    ![img](/TP_Final/image/10.png)


## Étape 5: Configurer le Contrôle d'Accès Basé sur les Rôles

1. **Créer un nouvel utilisateur avec le rôle `readWrite` pour la base de données `Galaxies_restore`:**

   Voici la ligne de commande mais avec l'option gratuite d'atlas on ne peut pas le faire. Alors on va aller directement sur l'interface.

   ```javascript
   use Galaxies_restore
   db.createUser({
       user: "popo",
       pwd: "Passw0rd",
       roles: [{ role: "readWrite", db: "Galaxies_restore" }]
   })
   ```
    ![img](/TP_Final/image/11.png)

2. **Se connecter à la base de données `Galaxies_restore` en utilisant les nouvelles informations d'identification utilisateur:**
   ```bash
   mongosh "mongodb://new_user:popo_Passw0rd@localhost:27017/Galaxies_restore"
   ```

3. **Insérer un nouveau document dans la collection `Stars`:**
   ```javascript
   db.Stars.insertOne({ Name: "Proxima Centauri", Type: "M-type", Distance: 4.24 })
   ```

4. **Vérifier que le document a été inséré avec succès:**
   ```javascript
   db.Stars.find().pretty()
   ```
   ![img](/TP_Final/image/12.png)

## Étape 6: Créer un Fichier Docker Compose et un Script Shell

### Fichiers anexes 

[Docker Compose](/TP_Final/docker-compose.yml)


[Script Shell](/TP_Final/setup_mongodb.sh)

Script vérifié sur git (cmd)
