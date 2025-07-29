from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    quantity: int


@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "quantity": item.quantity}
