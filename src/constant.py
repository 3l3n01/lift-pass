"""
    Constant env
"""
import os

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    "postgresql://postgres:postgres@localhost:5432/lift"
)
