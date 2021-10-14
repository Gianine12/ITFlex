from enum import Enum
from sqlalchemy import Column,String, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from . import db
from .groups import Groups

class Certificado(db.Model):
    __tablename__ = 'certificado'

    id = Column(Integer, primary_key=True)

    username = Column(String(30), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    expiration = Column(Integer)
    expirated_at = Column(Date)
    created_at = Column(Date)
    updated_at = Column(Date)

    groups = Column(Integer, ForeignKey("groups.cod"), nullable=False)

    certificado_groups = relationship("Groups", backref=backref("groups_certificado"))
    