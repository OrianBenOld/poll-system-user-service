from .database import database


async def create_user(user_data: dict) -> int:
    query = """
        INSERT INTO users (
            first_name, last_name, email, age, address, joining_date, is_registered
        ) VALUES (:first_name, :last_name, :email, :age, :address, :joining_date, :is_registered)
    """
    last_id = await database.execute(query, values=user_data)
    return int(last_id)


async def get_by_id(user_id: int):
    query = "SELECT * FROM users WHERE id = :user_id"
    return await database.fetch_one(query, values={"user_id": user_id})


async def get_all():
    query = "SELECT * FROM users ORDER BY id"
    return await database.fetch_all(query)


async def update_user(user_id: int, update_data: dict):
    # Only update fields that were explicitly provided
    if not update_data:
        return None
    fields = ", ".join(f"{key} = :{key}" for key in update_data)
    query = f"UPDATE users SET {fields} WHERE id = :user_id"
    values = {**update_data, "user_id": user_id}
    await database.execute(query, values)
    return await get_by_id(user_id)


async def register_user(user_id: int):
    query = "UPDATE users SET is_registered = TRUE WHERE id = :user_id"
    await database.execute(query, values={"user_id": user_id})
    return await get_by_id(user_id)


async def delete_user(user_id: int):
    query = "DELETE FROM users WHERE id = :user_id"
    await database.execute(query, values={"user_id": user_id})
