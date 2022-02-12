from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI,HTTPException
from models import User,Gender,Role,UserupdateRequest
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

@app.delete("/api/v1/users/{user_id}")
# delete_users(input:type)
def delete_users(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_coode=404,
        details=f'user with id:{user_id} does not exists'
    )

@app.put("/api/v1/users/{user_id}")
# delete_users(input:type)
def delete_users(user_update:UserupdateRequest,user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.gender is not None:
                user.gender= user_update.gender
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
        raise HTTPException(
            status_code=404,
            details=f"user with id: {user_id} does not exists"
        )