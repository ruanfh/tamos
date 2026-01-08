
from fastapi import FastAPI
from src.routes import health

app = FastAPI()

app.include_router(health.router)

@app.get("/")
def read_root():
    return {"hello": "world"}
