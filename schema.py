from pydantic import BaseModel
from datetime import date
        
class CreateNewUser(BaseModel):
    username:str
    password:str
    height:int
    class Config:
        extra="forbid"
        
class NewWeight(BaseModel):
    username:str
    date:date
    class Config:
        extra="forbid"