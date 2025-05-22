from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message" : "hello world folks"}

#@app.get('/greet/{name}')
#async def greet_name(name:str) -> dict:
 #   return {"message":f"hello dear {name}"}

#optional parameter (import lib first)
@app.get('/greet')
async def greet_name(name:Optional[str] = "User", age:int=0) -> dict :
    return {"message":f"hello dear {name}","age" : age}


