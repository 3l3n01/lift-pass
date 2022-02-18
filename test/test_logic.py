"""
    Pruebas unitarias para la logica de negocio
"""
import pytest
from src.logic import get_cost


def test_base():
    """
        Prueba unitaria para validar el costo de completo de un servicio
    """
    assert get_cost(20, 'Jour', '2020-05-08') == 35


def test_night():
    """
        Pruenas para validar el resultado correctos de los pases de noche
    """
    assert get_cost(20, 'Night', '2020-05-08') == 19


def test_child():
    """
        Prueba para validar que un menor de 6 años, no requiere pago.
    """
    assert get_cost(5, 'Jour', '2020-05-08') == 0


def test_elderly():
    """
        Prueba para validar el costo de un mayor de edad.
    """
    assert get_cost(65, 'Jour', '2020-05-08') == 27


def test_elderly_night():
    """
        Prueba para validar el costo de un pase para una persona mayor, en viaje de noche.
    """
    assert get_cost(65, 'Night', '2020-05-08') == 8


def test_holiday():
    """
        Validar que no se apliquen otros descuentos en un dia festivo
    """
    assert get_cost(20, 'Jour', '2020-12-25') == 35


def test_monday():
    """
        Validar que se aplique un descuento en dia lunes.
    """
    assert get_cost(20, 'Jour', '2020-05-04') == 23
