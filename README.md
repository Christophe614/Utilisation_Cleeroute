# TAF1 Utilisation_Cleeroute

Realise par l'etudiant NGUEAGHO KRYS DE HUGO

## Description
Il s'agit d'une api backend de gestion des articles avec les operations CRUD(POST,GET, PUT, DELETE) dans le cadre de l'unite d'enseignement INF 222
Le projet utilise:
_**FastAPI** pour l'API
_**SQLite3** pour la base de donnees
_**Python3.10** pour langage cote serveur

##Structure du projet
Projet/ |_mayapi.py(entree du projet)
        |_database.py(connexion a la base de donnees)
        |_routers.py(endpoints)

##Installation
1.Cloner le projet
git clone <lien du depot>

2.Installer FastAPI et Uvicorn
pip install fastapi uvicorn

3.Lancer l'application
uvicorn myapi:app --reload

l'api sera disponible sur: http://127.0.0.1:8000
la documentation sur :http://127.0.0.1:8000/docs

##Endpoints du projet
POST/api/articles -> cree un articles avec les informations id, titre, contenu, auteur, date, categorie,tags
GET/api/articles  -> recupere la liste des articles 
GET/api/articles/{id}  ->recupere un article à partir de son id
PUT/api/articles/{id}  ->mets à jour un article à partir de son id
DELETE/api/articles/{id}  ->supprime un article à partir de son id
