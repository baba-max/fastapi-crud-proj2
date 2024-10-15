from pydantic import BaseModel

        
class CreateNewUser(BaseModel):
    username:str
    password:str
    height:int
    class Config:
        extra="forbid"
        
class NewWeight(BaseModel):
    username:str
    class Config:
        extra="forbid"