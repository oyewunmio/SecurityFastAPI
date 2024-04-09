from fastapi import FastAPI
from routes import router
from sqlmodel import SQLModel
from db import engine
from config import settings

app = FastAPI()
app.include_router(router, prefix=settings.API_V1_STR)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
