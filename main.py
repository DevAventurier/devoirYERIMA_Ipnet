from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from models import Vehicle


#Creation d'une instance de l'application
app = FastAPI()

# instantiation static
vehicles = [
    Vehicle(registration="TG0494", owner="Dad", category="Car", cotation=1000.0),
    Vehicle(registration="TG2040", owner="Hatimou", category="Motorcycle", cotation=400.0),
    Vehicle(registration="TG6379", owner="Rachad", category="Motorcycle", cotation=500.0),
]



# Introduction 
@app.get("/")
async def root():
        return {"message": "Hello Sir, Hope these lines are all good"}
        return {"message": "YOURS ........ YERIMA"}
    
    
# Endpoint pour obtenir la liste des engins d'une catégorie donnée
@app.get("/category/{category}")
async def get_vehicles_by_category(category: str) -> List[Vehicle]:
    # récupération des engins par categorie
    filtered_vehicles = [vehicle for vehicle in vehicles if vehicle.category.lower() == category.lower()]
    return filtered_vehicles


# Endpoint pour obtenir la liste des engins d'un propriétaire donné
@app.get("/owner/{owner}")
async def get_vehicles_by_owner(owner: str) -> List[Vehicle]:
    # récupération des engins par propriétaire
    filtered_vehicles = [vehicle for vehicle in vehicles if vehicle.owner.lower() == owner.lower()]
    return filtered_vehicles


# Endpoint pour obtenir la facture à un propriétaire donné
@app.get("/bills/{owner}")
async def get_bill_for_owner(owner: str):
    # calcul de la facture à implémenter
    owner_vehicles = [vehicle for vehicle in vehicles if vehicle.owner.lower() == owner.lower()]
    insurance_total = sum(vehicle.cotation for vehicle in owner_vehicles)
    markup_total = sum(vehicle.cotation * 0.1 for vehicle in owner_vehicles)
    total_amount = insurance_total + markup_total

    return {
        "owner": owner,
        "total_amount": total_amount
    }


#pour lancer le service : uvicorn main:app --reload