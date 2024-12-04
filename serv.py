from fastapi import FastAPI, Response, Form, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from typing import Annotated
import asyncio

# from pydantic import BaseModel
from database.models import db_create_start
import database.requests as rq

from typing import *

import os
import pathlib
from dotenv import load_dotenv


load_dotenv()

SERVER_URL = os.getenv("SERVER_URL")


app = FastAPI()



origins = [
    SERVER_URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






async def sendHtml(html):
    return Response(content=html, media_type="text/plain")





@app.get("/api/venic/{img}", response_class=FileResponse)
async def venics(img: str):
    return pathlib.Path(f"./static/imgs/{img}")





@app.get("/api/all-venics-data")
async def all_venics_data():
    data = await rq.get_all_venics()

    return data
     




async def main():
    import uvicorn
    await db_create_start()
    print("Database started!")
    uvicorn.run('serv:app', port=int(os.getenv("SERVER_PORT")), host='127.0.0.1', reload=True)




if __name__ == '__main__':
    
    asyncio.run(main())
