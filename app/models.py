from pydantic import BaseModel
from typing import Optional

class FoodBase(BaseModel):
    """
    Modèle de base pour un aliment.
    Pydantic valide automatiquement les données.
    """
    alim_grp_code: str
    alim_ssgrp_code: str
    alim_ssssgrp_code: str
    alim_grp_nom_fr: str
    alim_ssgrp_nom_fr: str
    alim_ssssgrp_nom_fr: str
    alim_code: str
    alim_nom_fr: str
    alim_nom_sci: str
    energie_reg_ue_kj: str
    energie_reg_ue_kcal: str
    energie_jones_avec_fibres_kj: str
    energie_jones_avec_fibres_kcal: str
    eau: str
    proteines_jones: str
    proteines: str
    glucides: str
    lipides: str
    sucres: str
    fructose: str
    galactose: str
    glucose: str
    lactose: str
    maltose: str
    saccharose: str
    amidon: str
    fibres: str
    polyols: str
    cendres: str
    alcool: str
    acides_organiques: str
    ags: str
    agmi: str
    agpi: str
    ag_butyrique: str
    ag_caproique: str
    ag_caprylique: str
    ag_caprique: str
    ag_laurique: str
    ag_myristique: str
    ag_palmitique: str
    ag_stearique: str
    ag_oleique: str
    ag_linoleique: str
    ag_alpha_linolenique: str
    ag_arachidonique: str
    EPA: str
    DHA: str
    cholesterol: str
    chlorure_de_sodium: str
    calcium: str
    chlorure: str
    cuivre: str
    fer: str
    iode: str
    magnesium: str
    manganese: str
    phosphore: str
    potassium: str
    selenium: str
    sodium: str
    zinc: str
    retinol: str
    beta_carotene: str
    vitamine_d: str
    vitamine_e: str
    vitamine_k1: str
    vitamine_k2: str
    vitamine_c: str
    vitamine_b1: str
    vitamine_b2: str
    vitamine_b3: str
    vitamine_b5: str
    vitamine_b6: str
    vitamine_b9: str
    vitamine_b12: str

    
class Food(FoodBase):
    """
    Modèle complet avec un ID.
    Hérité de FoodBase pour réutiliser les champs.
    """
    id: int
    
    class Config:
        # Permet de créer un objet depuis un dictionnaire
        from_attributes = True