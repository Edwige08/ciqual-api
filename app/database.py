from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Récupérer l'URL de connexion
DATABASE_URL = os.getenv("DATABASE_URL")

# Créer le moteur de connexion à la base de données
engine = create_engine(DATABASE_URL)

# SessionLocal : pour créer des sessions de BDD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base : classe de base pour nos modèles SQLAlchemy
Base = declarative_base()

# Fonction pour obtenir une session de BDD
def get_db():
    """
    Générateur qui fournit une session de BDD.
    Se ferme automatiquement après utilisation.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()