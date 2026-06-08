from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home():
    return {"message": "Domain Knowledge Co-Pilot API"}

