from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.models import Food, FoodBase
from app.db_models import FoodDB
from app.database import get_db

router = APIRouter(
    prefix="/foods",
    tags=["foods"]
)

@router.get("/", response_model=list[Food])
def list_foods(db: Session = Depends(get_db)):
    """
    GET /foods - Récupère tous les aliments depuis Neon
    """
    foods = db.query(FoodDB).all()
    return foods

@router.get("/search/", response_model=list[Food])
def search_foods(
    q: str = Query(..., min_length=3, description="Terme de recherche (minimum 3 caractères)"),
    db: Session = Depends(get_db)
):
    """
    GET /foods/search/?q=pomme
    Recherche des aliments par nom (insensible à la casse)
    """
    # Recherche insensible à la casse avec ILIKE (PostgreSQL)
    foods = db.query(FoodDB).filter(
        FoodDB.alim_nom_fr.ilike(f"%{q}%")
    ).order_by(
        FoodDB.alim_nom_fr.ilike(f"{q}%").desc(),  # Commence par 'q' d'abord
        FoodDB.alim_nom_fr  # Puis ordre alphabétique
    ).all()
    
    return foods

@router.get("/{food_id}", response_model=Food)
def get_food(food_id: int, db: Session = Depends(get_db)):
    """
    GET /foods/{food_id} - Récupère un aliment spécifique
    """
    food = db.query(FoodDB).filter(FoodDB.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Aliment non trouvé")
    return food

# @router.post("/", response_model=Food, status_code=201)
# def create_food(food: FoodBase, db: Session = Depends(get_db)):
#     """
#     POST /foods - Crée un nouvel aliment dans Neon
#     """
#     db_food = FoodDB(**food.dict())
#     db.add(db_food)
#     db.commit()
#     db.refresh(db_food)
#     return db_food

# @router.delete("/{food_id}", status_code=204)
# def delete_food(food_id: int, db: Session = Depends(get_db)):
#     """
#     DELETE /foods/{food_id} - Supprime un aliment
#     """
#     food = db.query(FoodDB).filter(FoodDB.id == food_id).first()
#     if not food:
#         raise HTTPException(status_code=404, detail="Aliment non trouvé")
    
#     db.delete(food)
#     db.commit()
#     return None