from fastapi import APIRouter, HTTPException, status
from typing import List
from src.schemas.models import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])

# In-memory storage for demonstration
fake_db: List[dict] = [
    {"id": 1, "title": "FastAPI Masterclass", "description": "Production Guide", "price": 49.99, "is_active": True},
    {"id": 2, "title": "Pydantic v2 Mastery", "description": "Validation Engine", "price": 29.99, "is_active": True},
]

@router.get("", response_model=List[ItemResponse])
async def get_items():
    return fake_db

@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    for item in fake_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(payload: ItemCreate):
    new_id = len(fake_db) + 1
    new_item = {"id": new_id, **payload.model_dump()}
    fake_db.append(new_item)
    return new_item
