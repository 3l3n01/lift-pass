"""
    Configuracion basica
"""
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .constant import SQLALCHEMY_DATABASE_URI
from .logs import get_logger

# Logger
LOG = get_logger("config_init")

if SQLALCHEMY_DATABASE_URI is None:
    LOG.error("No database uri")
    sys.exit(-1)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
