from fastapi import APIRouter, Request, Depends, Form, responses, status
from fastapi.templating import Jinja2Templates
from typing import Optional
from sqlalchemy.orm import Session
from fastapi.security.utils import get_authorization_scheme_param

from db.session import get_db
from db.repository.blog import list_blogs, retreive_blog, delete_a_blog

# from db.models.blog import Blog
from res_models.blog import CreateBlog
from db.repository.blog import create_new_blog
from apis.v1.route_login import get_current_user

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/blog")
def home(request: Request, alert: Optional[str] = None, db: Session = Depends(get_db)):
    ls_blogs = list_blogs(db=db)
    return templates.TemplateResponse(
        "blog/home.html", {"request": request, "alert": alert, "blogs": ls_blogs}
    )


@router.get("/blog/create_new_blog")
def create_blog(request: Request):
    return templates.TemplateResponse("blog/create_blog.html", {"request": request})


@router.get("/blog/{id}")
def blog_detail(request: Request, id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    return templates.TemplateResponse(
        "blog/detail.html", {"request": request, "blog": blog}
    )


@router.post("/blog/create_new_blog")
def create_blog(
        request: Request,
        title: str = Form(...),
        content: str = Form(...),
        db: Session = Depends(get_db),
):
    token = request.cookies.get("access_token")
    _, token = get_authorization_scheme_param(token)
    try:
        author = get_current_user(token=token, db=db)
        blog = CreateBlog(title=title, content=content)
        blog = create_new_blog(
            blog=blog,
            db=db,
            author_id=author.id,
        )
        return responses.RedirectResponse(
            "/blog?alert=Blog Submitted For Review", status_code=status.HTTP_302_FOUND
        )
    except Exception as e:
        errors = ["Please Log in to Create New Blog"]
        return templates.TemplateResponse(
            "blog/create_blog.html",
            {"request": request, "errors": errors, "title": title, "content": content},
        )


@router.get("/blog/delete/{id}")
def delete_blog(request: Request, id: int, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    _, token = get_authorization_scheme_param(token)

    try:
        author = get_current_user(token=token, db=db)
        msg = delete_a_blog(id=id, author_id=author.id, db=db)
        alert = msg.get("msg") or msg.get("error")
        return responses.RedirectResponse(
            f"/blog?alert={alert}", status_code=status.HTTP_302_FOUND
        )
    except Exception as e:
        blog = retreive_blog(id=id, db=db)
        return templates.TemplateResponse(
            "blog/detail.html",
            {"request": request, "alert": "Please Login again", "blog": blog},
        )
