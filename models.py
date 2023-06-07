from pydantic import BaseModel

class Vehicle(BaseModel):
    registration: str
    owner: str
    category: str
    cotation: float