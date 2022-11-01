import json
from flask import Blueprint, jsonify, request
from db.database import tcDatabase

reportes = Blueprint('reportes', __name__, url_prefix="/reportes")

#------------------------------METODOS-----------------------------
@reportes.route('/pago', methods = ['GET'])
def reportePago():
    idfactura = request.args.get('idfactura')
    if(tcDatabase.detallePago(idfactura)):        
        return {'msg': 'Se generó el reporte en pdf'}
    else:
        return {'msg': 'No se pudo ejecutar la peticion'}
    pass

@reportes.route('/usadas', methods = ['GET'])
def reporteUsadas():
    fechaini = request.args.get('fechaini')
    fechafin = request.args.get('fechafin')
    return {'msg': 'usadas'}
    pass

@reportes.route('/ingresos', methods = ['GET'])
def analisisIngreso():
    fechaini = request.args.get('fechaini')
    fechafin = request.args.get('fechafin')
    return {'msg': 'ingresos'}
    pass