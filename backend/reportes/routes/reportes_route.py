import json
from flask import Blueprint, jsonify, request
from db.database import tcDatabase

reportes = Blueprint('reportes', __name__, url_prefix="/reportes")

#------------------------------METODOS-----------------------------
@reportes.route('/pago', methods = ['GET'])
def reportePago():
    idfactura = request.args.get('idfactura')
    if(idfactura != None):
        if(tcDatabase.detallePago(idfactura)):        
            return {'msg': 'Se generó el reporte en pdf'},200
        else:
            return {'msg': 'No se pudo ejecutar la peticion'}, 404
    else:
        return {'msg': 'No se pudo ejecutar la peticion'}, 404

@reportes.route('/usadas', methods = ['GET'])
def reporteUsadas():
    fechaini = request.args.get('fechaini')
    fechafin = request.args.get('fechafin')
    if(fechaini != None and fechafin != None):
        tcDatabase.masusadas(fechaini, fechafin)
        return {'msg': 'Se generó el reporte en pdf'},200
    pass

@reportes.route('/ingresos', methods = ['GET'])
def analisisIngreso():
    fechaini = request.args.get('fechaini')
    fechafin = request.args.get('fechafin')
    return {'msg': 'ingresos'}
    pass