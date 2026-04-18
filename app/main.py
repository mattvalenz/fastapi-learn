from typing import Optional

from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from random import randrange
import time
from sqlalchemy.orm import Session
from . import models,schemas
from .database import engine
from .database import get_db
from .schemas import Post

models.Base.metadata.create_all(bind=engine)


app = FastAPI()




    
    

while True:

    try:
        conn = psycopg2.connect(host = 'localhost', database='fastapi', user='postgres', password='123456', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database successfully connected.")
        break
    except Exception as error:
        print("Connecting failed")
        print("Error:", error)
        time.sleep(2)
        
my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id" : 1},
    {"title": "favorite food", "content": "chilli con carne", "id" : 2},
            ]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

#test route
@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    
    posts = db.query(models.Post).all()
    
    return{"data": posts}

@app.get("/")
def root():
    return {"message": "api check"}

@app.get("/posts")
def get_posts(db:Session= Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    
    return{"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    # cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    
    # conn.commit()
    
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return{"data": new_post}

@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s""", (str(id),))
    # post = cursor.fetchone()
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                        detail= f"post with id: {id} was not found")
     
    return {"post_detail" : post}   
    # below code is sloppier, above code is concise and commonly used
    # if not post: 
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"message": f"post with id: {id} was not found"}
   

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    
    # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    
    post = db.query(models.Post).filter(models.Post.id == id)
    
    conn.commit()
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist.")
    
    post.delete(synchronize_session=False)
    db.commit()
    
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post, db: Session = Depends(get_db)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    db_post = post_query.first()
    
    # cursor.execute("""UPDATE posts SET title =%s, content = %s, published =%s  WHERE id = %s RETURNING *""",(post.title, post.content, post.published, id) )
    # updated_post= cursor.fetchone()
    # conn.commit()
    
    if db_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist.")
    
    post_query.update(post.model_dump(), synchronize_session=False)
    
    db.commit()
   
    return {'data': post_query.first()}