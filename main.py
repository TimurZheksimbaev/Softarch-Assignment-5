from fastapi import FastAPI
from services import message_router, user_router, like_router
from database.connect import init_db

app = FastAPI()
app.include_router(message_router)
app.include_router(user_router)
app.include_router(like_router)

@app.get("/")
def read_root():
    return {"message": "This is our Twitter app"}


@app.on_event("startup")
def startup_event():
    init_db()
    print("Database initialized")


