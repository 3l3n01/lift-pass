"""
    Model: Holiday
"""
from sqlalchemy import Column, Integer, String, Date
from ..config_init import db


class Holiday(db.Model):
    """
        Holiday Class
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        return f'<Holiday {self.name}: {self.date}>'
