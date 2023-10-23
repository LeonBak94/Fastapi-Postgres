from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from schemas.blog import ShowBlog, CreateBlog, UpdateBlog
from db.repository.blog import create_new_blog, retreive_blog, list_blogs, delete_blog, update_blog
from typing import List
from db.models.user import Users
from apis.v1.route_login import get_current_user

router = APIRouter()


@router.post("/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    try:
        blog = create_new_blog(blog=blog, db=db, author_id=1)
        return blog
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/blogs/{id}", response_model=ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return blog


@router.get("/blogs", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs


@router.put("/blog/{id}", response_model=ShowBlog)
def update_a_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    blog = update_blog(id=id, blog=blog, author_id=current_user.id, db=db)
    if isinstance(blog, dict):
        raise HTTPException(
            detail=blog.get("error"),
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.delete("/delete/{id}")
def delete_blog(id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    messages = delete_blog(id=id, author_id=current_user.id, db=db)
    if messages.get('error'):
        raise HTTPException(detail=messages.get('error'),
                            status_code=status.HTTP_400_BAD_REQUEST)
    return {"msg": f"Successfully deleted blog with id {id}"}
