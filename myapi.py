from fastapi import FastAPI
from routers import router
from database import get_db
import json
from fastapi.middleware.cors import CORSMiddleware

#creation de table
def create_table():
    conn = get_db() 
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            contenu TEXT NOT NULL,
            auteur TEXT NOT NULL,
            date DATE NOT NULL, 
            categorie TEXT,
            tags TEXT
        )
    ''')
    conn.commit()
    conn.close()   
def test_data():
    conn = get_db()
    cursor = conn.cursor()
    with open("test.json", "r") as f:
        data = json.load(f)
    for article in data["articles"]:
        cursor.execute("""INSERT INTO articles ( titre ,contenu, auteur, date, categorie, tags)
                       VALUES (?,?,?,?,?,?)""",( 
                                                article["titre"],
                                                  article["contenu"],
                                                    article["auteur"],
                                                      article["date"],
                                                      article["categorie"],
                                                      json.dumps(article["tags"] )))
    conn.commit()
    conn.close()
    

app=FastAPI(title="Blog API", description="API pour la gestion d'un blog")
@app.get("/api/")
def home():
    return {"message": "Bienvenue sur mon API d'articles"}

create_table()
test_data()

#inclure les endpoints
app.include_router(router) 


   