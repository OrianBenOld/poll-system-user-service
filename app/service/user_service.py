from typing import List, Optional
import httpx
from ..model.user import User, UserCreate, UserUpdate
from ..repository import user_repository
from ..config import config


async def create_user(user_data: UserCreate) -> User:
    user_id = await user_repository.create_user(user_data.model_dump())
    return await get_user(user_id)


async def get_user(user_id: int) -> Optional[User]:
    row = await user_repository.get_by_id(user_id)
    if not row:
        return None
    return User(**row)


async def get_all_users() -> List[User]:
    rows = await user_repository.get_all()
    return [User(**row) for row in rows]


async def update_user(user_id: int, user_data: UserUpdate) -> Optional[User]:
    update_payload = {k: v for k, v in user_data.model_dump().items() if v is not None}
    if not update_payload:
        return await get_user(user_id)
    updated = await user_repository.update_user(user_id, update_payload)
    if not updated:
        return None
    return User(**updated)


async def register_user(user_id: int) -> Optional[User]:
    updated = await user_repository.register_user(user_id)
    if not updated:
        return None
    return User(**updated)


async def delete_user(user_id: int) -> None:
    await user_repository.delete_user(user_id)
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            await client.delete(f"{config.POLL_SERVICE_URL}/users/{user_id}/answers")
    except (httpx.RequestError, httpx.TimeoutException):
        # Poll service might be unavailable, but user deletion should still succeed
        pass
