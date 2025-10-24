from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Leer FRONTEND_ORIGINS como lista separada por comas
allowed = os.getenv("FRONTEND_ORIGINS", "")
allowed_origins = [o for o in allowed.split(",") if o] or ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def hello():
    return {"message": "Hola desde FastAPI"}