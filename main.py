# Author: Orian Ben Old
from fastapi import FastAPI
from .app.controller.user_controller import router as user_router
from .app.repository.database import database

app = FastAPI(title="User Service")
app.include_router(user_router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
