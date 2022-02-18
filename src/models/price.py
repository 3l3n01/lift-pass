"""
    Module: Price
"""
from sqlalchemy import Column, Integer, String
from ..config_init import db


class Price(db.Model):
    """
        Price class
    """
    id = Column(Integer, primary_key=True)
    type = Column(String(80), unique=True, nullable=False)
    cost = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Price {self.type}: {self.cost}>'
