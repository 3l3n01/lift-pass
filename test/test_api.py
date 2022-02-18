"""
    Pruebas unitarias para validar las respuestas de flask
"""
import pytest
from src.app import app


def test_valid_response():
    """
        Validar que al enviar los datos corrector retornar un 200
    """
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 20, 'date': '2020-05-08', 'type': 'Jour'})

        assert response.status_code == 200


def test_invalid_response():
    """
        Validar que al enviar los datos incorrectos retornar un 500
    """
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 20, 'date': '2020-05-08'})

        assert response.status_code == 500


def test_json_response():
    """
        Validar que se tiene una respuesta con cabecera json
    """
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 20, 'date': '2020-05-08', 'type': 'Jour'})

        assert response.headers["content-type"] == "application/json"
