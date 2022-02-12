from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI
from models import User,Gender,Role
from typing import List


app = FastAPI()

db: List[User] = [
    User(id=UUID("a786afd6-e9af-4b8d-8230-9ff8fb1808fa"),
         first_name="Raghu",
         last_name="Sanur",
         gender=Gender.female,
         roles=[Role.student]
        )
]

@app.get("/")
def root():
    return{"Hello this is fastapi with python"}

@app.get("/api/v1/users")
def fetch_users():
    return db;

@app.post("/api/v1/users")
def add_users(user: User):
    db.append(user)
    return{"id": user.id}