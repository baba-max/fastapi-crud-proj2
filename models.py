from sqlalchemy import Column,Integer,String,Float,Date
from db import Base,engine
import datetime

class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    password = Column(String)
    height = Column(Float)

class Weight(Base):
    __tablename__="weights"
    id = Column(Integer,primary_key=True)
    username = Column(String)
    weight = Column(Float)
    date = Column(Date)


Base.metadata.create_all(bind=engine)