from typing import List
from fastapi import APIRouter, HTTPException, status
from ..model.user import User, UserCreate, UserUpdate
from ..service import user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    return await user_service.create_user(user)


@router.get("/", response_model=List[User])
async def get_all_users():
    return await user_service.get_all_users()


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate):
    updated = await user_service.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.post("/{user_id}/register", response_model=User)
async def register_user(user_id: int):
    user = await user_service.register_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await user_service.delete_user(user_id)
    return None
