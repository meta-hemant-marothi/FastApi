from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"data" : {"name" : "Hemant"}}

@app.get("/blog")
def blog(limit = 10, published : bool = True, sort : Optional[str] = None):
    if published:
        return {"data" : f"{limit} published blogs from db."}
    else:
        return {"data" : f"{limit} blogs from db."}

@app.get("/blog/{id}")
def blog_with_id(id: int):
    return {"data" : id}


class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post("/blog")
def create_blog(request: Blog):
    return {"data" : f"Blog is Created with title {request.title}"}

@app.get("/about")
def about():
    return {"data" : "About Page"}
