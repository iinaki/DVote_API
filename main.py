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

origins = [
    "http://localhost:5173",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)