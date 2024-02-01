import asyncio
from http.client import HTTPException
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def some(name: str, age: str):
    try:
        print(name)

async def main():
   
    
