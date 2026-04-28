from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime
engine = create_engine('sqlite:///security.db')

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Log(Base): 
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String)
    status = Column(String)
    timestamp = Column(DateTime)