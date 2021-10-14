from sqlalchemy import Column,String, Integer
import enum

from . import db

# class Groups(enum.Enum):

#     Adm = 1
#     Comercial = 15
#     RH = 30

class Groups(db.Model):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    cod = Column(Integer, unique=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
