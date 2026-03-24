from fastapi import APIRouter, HTTPException
from database import get_db

router = APIRouter()

#Endpoint pour creer un article
@router.post("/api/articles")
def create_article(article:dict):
    conn=get_db
    cursor = conn.cursor()

    try:
        cursor.execute("""INSERT INTO articles (id ,
            titre ,contenu, auteur, date, categorie, tags)
                       VALUES (?,?,?,?,?,?)""", (article["titre"],
                                                  article["contenu"],
                                                    article["auteur"],
                                                      article["date"],
                                                      article["tcategorie"],
                                                      article["tags"]))
        conn.commit()
        return {"message": "Article cree avec succes"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


#endpoint pour recuperer les articles
@router.get("/api/articles")
def get_articles():
    conn = get_db
    cursor = conn.cursor()
    try:
        cursor.excecute("SELECT * FROM articles")
        articles = cursor.fechtall()
        return {"data":articles}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

#endpoint pour recuperer un article par l'id
@router.get("/api/articles{id}")
def get_article(id:int):
    conn = get_db
    cursor = conn.cursor()
    try:
        cursor.excecute("SELECT * FROM articles WHERE id=?",(id,))
    
        article = cursor.fechtone()
        if article is None:
            raise HTTPException(status_code=404,detail="article non trouve")
        return {"data":article}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

#endpoint pour supprimer un article par l'id
@router.delete("/api/articles{id}")
def del_article(id:int):
    conn = get_db
    cursor = conn.cursor()
    try:
        cursor.excecute("SELECT * FROM articles WHERE id=?",(id,))
    
        article = cursor.fechtone()
        if article is None:
            raise HTTPException(status_code=404,detail="article non trouve")
        cursor.excecute(" FROM DELETE articles WHERE id=?",(id,))
        conn.commit()

        return {"Message":"article supprime avec succes"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

#endpoint pour mettre à jour un article par l'id
@router.put("/api/articles{id}")
def update_article(id:int):
    conn = get_db
    cursor = conn.cursor()
    try:
        cursor.excecute("SELECT * FROM articles WHERE id=?",(id,))
    
        article = cursor.fechtone()
        if article is None:
            raise HTTPException(status_code=404,detail="article non trouve")
        cursor.excecute("""UPDATE articles SET titre = ?, auteur = ?, date = ?, categorie = ?, tags = ?
                        WHERE id=?""",(article["titre"],
                                                  article["contenu"],
                                                    article["auteur"],
                                                      article["date"],
                                                      article["tcategorie"],
                                                      article["tags"]))
        conn.commit()
        return {"message": "Article mis à jour avec succes"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()