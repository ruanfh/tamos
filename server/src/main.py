

from fastapi import FastAPI

from src.routes import health, submit, archive

app = FastAPI()

app.include_router(health.router)
app.include_router(submit.router)
app.include_router(archive.router)

@app.get("/")
def read_root():
    return {"hello": "world"}
