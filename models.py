from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    plate = Column(String, unique=True, index=True)
    model = Column(String, index=True)
    motorization = Column(String, index=True)

