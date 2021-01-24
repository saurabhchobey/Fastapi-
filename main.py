from typing import Optional
# import asyncio
# from hypercorn.config import Config
# from hypercorn.asyncio import serve
from fastapi import FastAPI


app=FastAPI()

@app.get('/')
def read_book():
    return {'hello':'world'}

@app.get('/items/{item_id}')
def read_item(item_id:int,q:Optional[str] = None):
    return {'item_id': item_id , 'q': q}