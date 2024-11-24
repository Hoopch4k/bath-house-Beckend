from database.models import async_session
from database.models import Venics
from sqlalchemy import select, update, delete, text
import sqlalchemy

import datetime


async def get_all_venics():
    async with async_session() as session:
        return await session.execute(text("SELECT * FROM Venics"))

