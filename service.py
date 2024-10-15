from models import User,Weight
from schema import *
from sqlalchemy.orm import Session
from exceptions import UserNotFoundException,WeightNotFound,ExistingUser
import bcrypt


def current_weight(username:str, db:Session):
    user_existing=db.query(User).filter_by(username=User.username).first()
    if not user_existing:
        raise UserNotFoundException
    get_last_weight = db.query(Weight).filter(Weight.username == username).order_by(Weight.date.desc()).first()
    if not get_last_weight:
        raise WeightNotFound
    msg={"last weight":get_last_weight.weight}
    return msg


def create_new_user(data:CreateNewUser,db:Session):
    existing_user = db.query(User).filter_by(username=data.username).first()
    if existing_user:
        raise ExistingUser
    new_user=User(username=data.username,password=data.password,height=data.height)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"new user is created"}

def create_new_weight(weight:int,date:float,data:NewWeight,db:Session):
    user_existing=db.query(User).filter_by(username=data.username).first()
    if not user_existing:
        raise UserNotFoundException
    existing_weight = db.query(Weight).filter(Weight.username == data.username, Weight.date == date).first()
    if existing_weight:
        existing_weight.weight = weight
        db.commit()
        return {"msg": "Weight is updated"}
    else:
        new_weight=Weight(username=data.username,weight=weight,date=date)
        db.add(new_weight)
        db.commit()
        db.refresh(new_weight)
        return {"msg":"new weight is created"}
    
    
def get_difference_weight(username:str, db:Session):
    user_existing=db.query(User).filter_by(username=User.username).first()
    if not user_existing:
        raise UserNotFoundException
    last_weight = db.query(Weight).filter(Weight.username == username).order_by(Weight.date.desc()).first()
    first_weight=db.query(Weight).filter(Weight.username == username).order_by(Weight.date.asc()).first()
    if not last_weight or not first_weight:
        raise WeightNotFound
    difference=last_weight.weight-first_weight.weight
    msg={"difference of weights":difference}
    return msg

def bmi(username:str, db:Session):
    get_height=db.query(User).filter(User.username == username).first()
    if not get_height:
        raise UserNotFoundException
    get_last_weight = db.query(Weight).filter(Weight.username == username).order_by(Weight.date.desc()).first()
    if not get_last_weight:
        raise WeightNotFound
    get_bmi=get_last_weight.weight/((get_height.height/100)**2)
    msg={"bmi":get_bmi}
    return msg
    