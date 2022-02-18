"""
    Init Db
"""

from datetime import datetime
from src.config_init import db
from src.models.holiday import Holiday
from src.models.price import Price


if __name__ == "__main__":

    db.create_all()

    data_prices = [
        {"types": 'Jour', "cost": 35},
        {"types": 'Night', "cost": 19}
    ]

    data_Holidays = [
        {"name": 'Christmas', "date": datetime(2020, 12, 25).date()},
        {"name": 'New Year', "date": datetime(2021, 1, 1).date()},
        {"name": 'valentines day', "date": datetime(2022, 2, 14).date()}
    ]

    for price in data_prices:
        db.session.add(Price(type=price["types"], cost=price["cost"]))

    for holiday in data_Holidays:
        db.session.add(Holiday(name=holiday["name"], date=holiday["date"]))

    db.session.commit()
