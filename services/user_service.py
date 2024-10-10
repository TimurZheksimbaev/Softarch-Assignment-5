from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from database.models import User
from database.connect import get_db
from sqlalchemy.orm import Session

user_router = APIRouter(
    prefix="/users"
)
class UserCreate(BaseModel):
    username: str


@user_router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = User(username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username}

@user_router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": db_user.id, "username": db_user.username}
