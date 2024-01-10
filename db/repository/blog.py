from sqlalchemy.orm import Session
from db.models.blog import Blog
from res_models.blog import CreateBlog


def list_blogs(db: Session):
    print(db.query(Blog).filter(Blog.is_acvite == True).all())
    return db.query(Blog).filter(Blog.is_acvite == True).all()


def create_new_blog(blog: CreateBlog, db: Session, author_id: int):
    blog = Blog(**blog.dict(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retreive_blog(id: int, db: Session):
    return db.query(Blog).filter(Blog.id == id).first()


def delete_a_blog(id: int, author_id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        return {"error": f"could not find a blog with id {id}"}
    if not blog.first().author_id == author_id:
        return {"error": "Only blog author can delete a blog"}
    blog.delete()
    db.commit()
    return {"msg": f"Blog with id {id} deleted successfully"}