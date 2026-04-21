from typing import Optional, List

from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from random import randrange
import time
from sqlalchemy.orm import Session
from . import models,schemas, utils
from .database import engine
from .database import get_db
from .schemas import PostCreate, PostBase, UserCreate
from .routers import post, user

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
        

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "api check"}

    