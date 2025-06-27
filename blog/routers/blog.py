from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from .. import schemas, models, database
from sqlalchemy.orm import Session


router = APIRouter(
        prefix= "/blog",
        tags=["Blogs"]
    )

# Crete a blog
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db : Session = Depends(database.get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Get all Blogs
@router.get("/", response_model=List[schemas.Blog])
def get_all_blog(db: Session = Depends(database.get_db)):
    blogs= db.query(models.Blog).all()
    return blogs


# Get blog with id using path parameter
@router.get("/{id}")
def get_blog_with_id(id : int, db : Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog


# Delete blog with id using path parameter
@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_blog_with_id(id:int, db:Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail = 'Blog not found.')
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}


# Update blog with id using path parameter
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog_with_id(id: int, updated_blog: schemas.Blog, db:Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail = 'Blog not found.')
    blog.title = updated_blog.title
    blog.body = updated_blog.body
    db.commit()
    return blog
