from typing import Optional

from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

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

@app.get("/")
def root():
    return {"message": "api check"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0,100000)
    my_posts.append(post_dict)
    return{"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    
    post = find_post(id)
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                        detail= f"post with id: {id} was not found")
    # below code is sloppier, above code is concise and commonly used
    # if not post: 
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"message": f"post with id: {id} was not found"}
    return {"post_detail" : post}

@app.delete("/posts/{id}")
def delete_post():
    index = find_index_post(id)
    my_posts.pop(index)
    
    return {'message':'post successfully deleted'}

