"""
    Logic Route
"""
import json
from flask import jsonify, request, Response
from .config_init import app
from .logic import get_cost

def error(message, status):
    """
        Metodo para generar un error con el formato requerido
    """
    return Response(json.dumps({"message": message}), status, content_type="application/json")

@app.route('/prices')
def prices():
    """
        Ruta para el retorno del precio
    """
    age = int(request.args.get('age', 0))
    type_lift = request.args.get('type', None)
    date_pass = request.args.get('date', None)
    cost = 0

    if type_lift is None or date_pass is None or age < 1:
        return error( "los datos proporcionados no son correctos", 500)

    try:
        cost = get_cost(age, type_lift, date_pass)
    except Exception:
        return error("Ocurrio un problema al procesar el costo", 501)

    # Return data
    return jsonify({'cost': cost})
