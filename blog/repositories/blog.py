from .. import schemas, models
from sqlalchemy.orm import Session

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog