from enum import Enum
from typing import Optional
from uuid import uuid4,UUID
from pydantic import BaseModel


class Gender(str,Enum):
    Male = "male"
    Female = "female"

class Role(str,Enum):
    admin = "Admin"
    user = "User"
    student = "Student"
    

class User(BaseModel):
    id:Optional[UUID] = uuid4()
    first_name : str
    last_name : str
    middle_name : Optional[str]
    gender:Gender
    role : list[Role]
    
