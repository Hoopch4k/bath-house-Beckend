from sqlalchemy import BigInteger, String, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

import asyncio

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)



class Database(AsyncAttrs, DeclarativeBase):
    pass



class Venics(Database):
    __tablename__ = 'venics'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    type: Mapped[str] = mapped_column(String(100), nullable=True)
    path: Mapped[str] = mapped_column(String(250))





async def db_create_start():
    async with engine.begin() as conn:
        await conn.run_sync(Database.metadata.create_all)