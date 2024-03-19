from typing import Union
from uuid import uuid4
from models import User,Gender,Role

from fastapi import FastAPI

app = FastAPI()

db: list[User]=[
    User(
        id=uuid4(),
        first_name="razeen",
        middle_name="mohamed",
        last_name="rasheed",
        gender=Gender.Male,
        role=[Role.admin]
    ),
     User(
        id=uuid4(),
        first_name="rasheed",
        middle_name="mohamed",
        last_name="razeen",
        gender=Gender.Male,
        role=[Role.admin,Role.user]
    )
]

@app.get('/api/v1/users')
async def getUsers():
    return db;

@app.post('/api/v1/users')
async def registerUser(user:User):
    db.append(user)
    return {"id":user.id}
    
    

