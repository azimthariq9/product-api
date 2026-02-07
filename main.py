from fastapi import FastAPI, HTTPException
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

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return {"message": "Produk ditambahkan", "data": product}

@app.put("/products/{product_id}")
def update_product(product_id: int, updated: Product):
    for i, p in enumerate(products):
        if p.id == product_id:
            products[i] = updated
            return {"message": "Produk diupdate", "data": updated}
    raise HTTPException(status_code=404, detail="Produk tidak ditemukan")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for p in products:
        if p.id == product_id:
            products.remove(p)
            return {"message": "Produk dihapus"}
    raise HTTPException(status_code=404, detail="Produk tidak ditemukan")
