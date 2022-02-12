from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    male="male"
    female="female"

class Role(str,Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class UserupdateRequest(BaseModel):
    first_name: Optional[str]
    middle_name: Optional[str]
    gender: Optional[str]
    roles: Optional[List[Role]]
