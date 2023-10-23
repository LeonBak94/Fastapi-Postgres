from sqlalchemy.orm import Session
from db.models.user import Users


def get_user(email: str, db: Session):
    user = db.query(Users).filter(Users.email == email).first()
    return user
