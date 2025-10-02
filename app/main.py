from fastapi import FastAPI
from app.routers import foods
from app.database import engine, Base

# Créer toutes les tables dans Neon (si elles n'existent pas)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ciqual API",
    description="API pour consulter les valeurs nutritionnelles des aliments selon les données du Ciqual 2020 (ANSES)",
    version="1.0.0"
)

app.include_router(foods.router)

@app.get("/")
def root():
    return {
        "message": "Bienvenue sur l'API Ciqual !",
        "documentation": "/docs"
    }