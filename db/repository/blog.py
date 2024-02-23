from sqlalchemy.orm import Session
from db.models.blog import Blog
from res_models.blog import CreateBlog


def list_blogs(db: Session):
    return db.query(Blog).filter(Blog.IS_ACTIVE == True).all()


def create_new_blog(blog: CreateBlog, db: Session, author_id: int):
    blog = Blog(**blog.dict(), AUTHOR_ID=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retrieve_blog(id: int, db: Session):
    return db.query(Blog).filter(Blog.ID == id).first()


def delete_a_blog(id: int, author_id: int, db: Session):
    blog = db.query(Blog).filter(Blog.ID == id)
    if not blog.first():
        return {"error": f"could not find a blog with id {id}"}
    if not blog.first().AUTHOR_ID == author_id:
        return {"error": "Only blog author can delete a blog"}
    blog.delete()
    db.commit()
    return {"msg": f"Blog with id {id} deleted successfully"}
