"""
    Logica de negocio
"""
import math
from datetime import datetime
from .models.price import Price
from .models.holiday import Holiday


def get_cost(age, type_lift_pass, date_pass):
    """
        Metodo para el retorno del costo
        @params age
        @params type
    """
    price = Price.query.filter_by(type=type_lift_pass).first()
    reduction = 0
    is_holiday = holiday(date_pass)

    if datetime.strptime(date_pass, '%Y-%m-%d').weekday() == 0:
        if not is_holiday and type_lift_pass != 'Night':
            reduction = 35

    if age >= 6:
        if age > 64:
            if type_lift_pass == 'Night':
                return math.ceil(price.cost * 0.4)
            else:
                return math.ceil(price.cost * 0.75 * (1 - reduction / 100))
        elif type_lift_pass != 'Night' and age < 15:
            return math.ceil(price.cost * 0.7)

        return math.ceil(price.cost * (1 - reduction / 100))

    return 0


def holiday(date_pass):
    """
        Comprobar si es un dia festivo
    """
    date_format = date = datetime.strptime(date_pass, '%Y-%m-%d').date()
    date = Holiday.query.filter_by(date=date_format).first()
    return date is not None
