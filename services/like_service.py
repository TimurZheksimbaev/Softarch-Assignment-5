from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.models import Like
from database.connect import get_db

like_router = APIRouter(
    prefix="/likes",
)

class LikeCreate(BaseModel):
    user_id: int
    message_id: int

@like_router.post("/")
def like_message(like: LikeCreate, db: Session = Depends(get_db)):
    new_like = Like(user_id=like.user_id, message_id=like.message_id)
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return {"id": new_like.id, "user_id": new_like.user_id, "message_id": new_like.message_id}
