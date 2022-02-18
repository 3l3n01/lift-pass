"""
    Archivo principal de logs
"""
import sys
from logbook import Logger, StreamHandler
StreamHandler(sys.stdout).push_application()


def get_logger(name):
    """
        Genera un logger para el modulo/class
    """
    return Logger(name)
