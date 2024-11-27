from database.models import async_session
from database.models import Venics
from sqlalchemy import select, update, delete, text
from sqlalchemy.engine.cursor import CursorResult



import datetime

def rows_as_dicts(cursor):
    """convert tuple result to dict with cursor"""
    col_names = [i[0] for i in cursor.name]
    return [dict(zip(col_names, row)) for row in cursor]


async def get_all_venics():
    async with async_session() as session:
        
        data = await session.execute(text("SELECT * FROM Venics"))
        res = data.mappings().all()
        print(type(data))
        print(res)
        return res

