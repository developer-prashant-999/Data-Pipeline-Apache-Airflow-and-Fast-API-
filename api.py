from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class User(BaseModel):
    username: str
    salary: int

mydata: List[User] = [User(
    username="Ram",
    salary=50000
)]

@app.get("/getusers")
async def get_users():
    return mydata

@app.post("/adduser")
async def add_user(username:str,salary:str):
    user = User(username=username,salary=salary)
    mydata.append(user)
    return mydata



