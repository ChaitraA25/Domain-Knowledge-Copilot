from fastapi import FastAPI

from backend.database.db import orm_engine
from backend.database.db import Base

from backend.database.dependencies import get_db

from backend.routers.users import router as users_router

app= FastAPI()

# Create all tables when application starts
Base.metadata.create_all(bind=orm_engine)

app.include_router(users_router)

@app.get("/")
def home():
    return {"message": "Domain Knowledge Co-Pilot API"}


