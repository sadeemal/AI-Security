from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String)
    status = Column(String)
    ip = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)