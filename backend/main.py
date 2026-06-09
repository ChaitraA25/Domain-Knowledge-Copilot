from fastapi import FastAPI

from backend.database.db import orm_engine
from backend.database.models import Base

app= FastAPI()

# Create all tables when application starts
Base.metadata.create_all(bind=orm_engine)

@app.get("/")
def home():
    return {"message": "Domain Knowledge Co-Pilot API"}

