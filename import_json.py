import json
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.db_models import FoodDB

# Créer les tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

def import_json(json_filepath: str):
    """
    Import des données nutritionnelles depuis un fichier JSON
    """
    db: Session = SessionLocal()
    
    try:
        # Lire le fichier JSON
        with open(json_filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Vérifier si c'est une liste ou un objet avec une clé contenant la liste
        if isinstance(data, dict):
            # Si c'est un dictionnaire, prendre la première valeur qui est une liste
            # Par exemple : {"foods": [...]} ou {"aliments": [...]}
            foods_list = next(iter(data.values())) if data else []
        else:
            # Si c'est directement une liste
            foods_list = data
        
        print(f"📦 {len(foods_list)} aliments trouvés dans le fichier JSON")
        
        count = 0
        errors = 0
        
        for food_data in foods_list:
            try:
                # Supprimer le champ 'id' s'il existe (sera auto-généré)
                if 'id' in food_data:
                    del food_data['id']
                
                # Créer un objet FoodDB
                food = FoodDB(**food_data)
                db.add(food)
                count += 1
                
                # Commit par batch de 100 pour améliorer les performances
                if count % 100 == 0:
                    db.commit()
                    print(f"✅ {count} aliments importés...")
                    
            except Exception as e:
                errors += 1
                print(f"⚠️ Erreur sur un aliment : {e}")
                print(f"   Données : {food_data.get('alim_nom_fr', 'Inconnu')}")
        
        # Commit final
        db.commit()
        print(f"\n🎉 Import terminé !")
        print(f"   ✅ {count} aliments ajoutés avec succès")
        if errors > 0:
            print(f"   ⚠️ {errors} erreurs rencontrées")
            
    except FileNotFoundError:
        print(f"❌ Fichier non trouvé : {json_filepath}")
    except json.JSONDecodeError as e:
        print(f"❌ Erreur de format JSON : {e}")
    except Exception as e:
        print(f"❌ Erreur lors de l'import : {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    # Remplace par le chemin vers ton fichier JSON
    import_json("table_ciqual_2020.json")