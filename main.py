from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Product API")

class Product(BaseModel):
    id: int
    name: str
    price: int

products: List[Product] = []

@app.get("/products")
def list_products():
    return products
