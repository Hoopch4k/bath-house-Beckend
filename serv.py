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
SERVER_PORT = int(os.getenv("SERVER_PORT"))


app = FastAPI()



origins = [
    SERVER_URL,
    'http://localhost:3000',
    'http://26.179.113.221:3030',
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





@app.get("/api/venic/{img}")
async def venics(img: str):
    try:
        res = FileResponse(f"./static/imgs/{img}")
        return res
    except RuntimeError:
        return {"error": "Error getting img"}





@app.get("/api/all-venics-data")
async def all_venics_data():
    data = await rq.get_all_venics()
    return data
     


@app.get("/api/galery/all-videos")
async def all_video():
    return await rq.get_all_videos()


@app.get("/api/galery/video/{id}")
async def video_by_id(id: int):
    try:
        res = await rq.get_video_by_id(id)
        return FileResponse(f"./static/videos/{res.path}")
    except Exception as e:
        return {'error': "Error getting video"}




@app.get("/api/galery/all-images")
async def get_all_images():
    return await rq.get_all_images()




@app.get("/api/galery/image/{id}")
async def get_image_by_id(id: int):
    try:
        res = await rq.get_image_by_id(id)
        return FileResponse(f"./static/imgs/{res.path}")
    except Exception as e:
        return {'error': "Error getting image"}




async def main():
    import uvicorn
    await db_create_start()
    print("Database started!")
    uvicorn.run('serv:app', port=SERVER_PORT, host='127.0.0.1', reload=True)




if __name__ == '__main__':
    
    asyncio.run(main())
