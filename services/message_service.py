from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.models import Message
from database.connect import get_db

message_router = APIRouter(
    prefix="/messages"
)

class MessageCreate(BaseModel):
    user_id: int
    content: str

@message_router.post("/")
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    if len(message.content) > 400:
        raise HTTPException(status_code=400, detail="Message exceeds 400 characters")
    new_message = Message(user_id=message.user_id, content=message.content)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return {"id": new_message.id, "content": new_message.content}

@message_router.get("/")
def get_messages(db: Session = Depends(get_db)):
    messages = db.query(Message).order_by(Message.timestamp.desc()).limit(10).all()
    return messages
