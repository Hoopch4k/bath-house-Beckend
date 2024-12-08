from database.models import async_session
from database.models import Venics
from sqlalchemy import select, update, delete, text
from sqlalchemy.engine.cursor import CursorResult



import datetime


async def get_all_venics():
    async with async_session() as session:
        data = await session.execute(text("SELECT * FROM Venics"))
        return data.mappings().all()
    
    
    
async def get_all_videos():
    async with async_session() as session:
        data = await session.execute(text("SELECT * FROM Videos"))
        return data.mappings().all()
    


async def get_all_images():
    async with async_session() as session:
        data = await session.execute(text("SELECT * FROM Images"))
        return data.mappings().all()

    

    
async def get_video_by_id(id: int):
    async with async_session() as session:
        data = await session.execute(text(f"SELECT * FROM Videos WHERE id = {id}"))
        return data.mappings().fetchone()
    
    
    
async def get_image_by_id(id: int):
    async with async_session() as session:
        data = await session.execute(text(f"SELECT * FROM Images WHERE id = {id}"))
        return data.mappings().fetchone()
    
    
    