# pip install fastapi uvicorn

from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="API de votantes",
    openapi_tags=[{
        "name": "users",
        "description": "Operaciones CRUD de usuarios"
    }]
)

app.include_router(user)

