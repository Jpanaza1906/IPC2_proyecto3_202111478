from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from consumos.models.consumos_model import Consumos

consumos = Blueprint('consumos', __name__, url_prefix="/consumos")

#---------------------MODELOS--------------------------------
@consumos.route('', methods = ['POST'])
def crear():
    body = request.get_json()
    try:
        if ("idcliente" in body and "idinstancia" in body and "tiempo" in body and "descripfechahora" in  body):
            if(body["idcliente"] != "" and body["idinstancia"] != "" and body["tiempo"] != "" and body["descripfechahora"] != ""):
                consumo = Consumos(body["idcliente"], body["idinstancia"], body["tiempo"], body["descripfechahora"])
                if(tcDatabase.agregarConsumos(consumo)):
                    return{'msg':'Consumo creado exitosamente.'}, 201 #created
                else:
                    return{'msg': 'El consumo ya se encuentra registrado.'}, 406 #Not acceptable
            else:
                return{'msg': 'Error en los campos'}, 406 #Not acceptable         
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500 #internal server error

@consumos.route('', methods = ['GET'])
def buscar():
    id = request.args.get('id')
    try:
        if(id != None):
            consumosl = tcDatabase.buscarConsumosid(id)
            return jsonify(consumosl), 200 #ok
        else:
            consumosl = tcDatabase.buscarConsumos()
            return jsonify(consumosl), 200 #ok
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500 #internal server error
    
@consumos.route('', methods = ['DELETE'])
def eliminar():
    id = request.args.get('id')
    try:
        if (id != None):
            if(tcDatabase.eliminarConsumos(id)):                
                return {'msg' : 'El consumo fue eliminado exitosamente'}, 200
            else:
                return {'msg' : 'No se encontro el id'}, 200
        else:
            return {'msg' : 'No se tienen los parametros suficientes'}, 200
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500