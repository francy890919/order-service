from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Order Service")

orders = []

class OrderRequest(BaseModel):
    product_id: int
    quantity: int

@app.get("/api/orders")
def get_orders():
    return orders

@app.post("/api/orders", status_code=201)
def create_order(order: OrderRequest):
    new_order = {
        "id": len(orders) + 1,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "status": "pending"
    }
    orders.append(new_order)
    return new_order

@app.get("/health")
def health():
    return {"status": "ok"}