from fastapi import FastAPI,HTTPException
from math import pow
from uuid import UUID, uuid4
from models import User,Gender
from typing import List

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),
         first_name="Raghu",
         gender=Gender.male,
         height= 105.4,
         weight= 16.9,
         bmi=15.2
        )
]

@app.get("/")
def root():
    return{"This is BMI index calculator API"}


@app.post("/api/v1/bmi-index")
def bmi(height:float, weight:float):
    bmi=(weight/ height/ height) *10000
    return{f'Your bmi index is {bmi}'}


@app.post("/api/v1/math")
def powerof(power:int):
    number_power=pow(2,power)
    return{f'Power of the number is {number_power}'}

@app.get("/api/v1/bmi-index-new")
def fetch_users():
    return db;

@app.post("/api/v1/bmi-index-new")
def bmi_new(user: User):
    bmi=(user.weight/ user.height/ user.height) *10000
    db.append(user)
    return{f'Your bmi index is {bmi}'}