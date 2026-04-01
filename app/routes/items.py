from fastapi import APIRouter, HTTPException
from app.models.item import Item

router = APIRouter(prefix="/items", tags=["Items"])

fake_db = []

@router.post("/")
def create_item(item: Item):
    fake_db.append(item)
    return {"message": "Item added", "item": item}

@router.get("/")
def get_items():
    return fake_db

@router.get("/{item_id}")
def get_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]