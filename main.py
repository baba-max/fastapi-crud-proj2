from fastapi import FastAPI,Depends
from db import get_db
from sqlalchemy.orm import Session
from schema import *
from service import *

app = FastAPI()

@app.get("/weight/last")
def get_weight(user_name: str, db:Session=Depends(get_db)):
    message=current_weight(username=user_name,db=db)
    return message

@app.post("/user")
def create_user(item:CreateNewUser,db:Session=Depends(get_db)):
    message=create_new_user(data=item,db=db)
    return message

@app.post("/weight")
def create_weight(new_weight:int,item:NewWeight,db:Session=Depends(get_db)):
    message=create_new_weight(weight=new_weight,data=item,db=db)
    return message

@app.get("/weight/difference")
def get_difference(user_name: str, db:Session=Depends(get_db)):
    message=get_difference_weight(username=user_name,db=db)
    return message

@app.get("/bmi")
def get_bmi(user_name: str, db:Session=Depends(get_db)):
    message=bmi(username=user_name,db=db)
    return message