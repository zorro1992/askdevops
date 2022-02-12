from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    male="male"
    female="female"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    gender: Gender
    height: float
    weight: float