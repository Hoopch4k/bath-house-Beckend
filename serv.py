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


app.mount("/static", StaticFiles(directory="static"), name="static")



async def sendHtml(html):
    return Response(content=html, media_type="text/plain")





@app.get("/api/venic/{img}")
async def venics(img: str):
    return FileResponse(path=f"./static/imgs/{img}")


@app.get("/api/all-venics-data")
async def all_venics_data():
    res = []
    data = await rq.get_all_venics()
    
    for i in data:
        res.append({
            "id": i.id,
            "name": i.name,
            "type": i.type,
            "path": i.path
        })
    return res
     




async def main():
    import uvicorn
    await db_create_start()
    print("Database started!")
    uvicorn.run('serv:app', port=8080, host='127.0.0.1', reload=True)




if __name__ == '__main__':
    
    asyncio.run(main())
