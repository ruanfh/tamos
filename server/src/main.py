

from fastapi import FastAPI
from src.routes import health, submit

app = FastAPI()

app.include_router(health.router)
app.include_router(submit.router)

@app.get("/")
def read_root():
    return {"hello": "world"}
