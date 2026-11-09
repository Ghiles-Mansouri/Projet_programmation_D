from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI(title="Microservice Collecteur - Rôtisserie")

# Stockage temporaire en mémoire pour simuler la base de données
base_de_donnees_memoire = []

# Modèle de validation : si une requête ne respecte pas ce format, FastAPI la rejette
class Commande(BaseModel):
    id_produit: str
    quantite: int
    prix_total: float
    date_heure: datetime

@app.post("/api/ventes", status_code=201)
async def enregistrer_vente(commande: Commande):
    # Validation métier : refus des quantités invalides
    if commande.quantite <= 0:
        raise HTTPException(status_code=400, detail="La quantité doit être supérieure à zéro.")
    
    # Ajout à la base de données en mémoire
    base_de_donnees_memoire.append(commande.dict())
    return {"message": "Commande enregistrée", "commande": commande}

@app.get("/api/ventes", response_model=List[Commande])
async def consulter_ventes():
    # Permet de vérifier que les données sont bien stockées
    return base_de_donnees_memoire 