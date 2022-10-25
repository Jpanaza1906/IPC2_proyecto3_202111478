import json
from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from recursos.models.recursos_model import Recursos

recursos = Blueprint('recursos', __name__, url_prefix="/recursos")

#------------------------------METODOS-----------------------------
@recursos.route('', methods = ['POST'])
def crear():
    body = request.get_json()
    try:
        if("id" in body and "nombreRecurso" in body and "abreviatura" in body and "nombreMetrica" in body and "tipo" in body and "valor" in body):
            if(body["id"] != "" and body["nombreRecurso"] != "" and body["abreviatura"] != "" and body["nombreMetrica"] != "" and body["tipo"] != "" and body["valor"] != ""):
                recurso = Recursos(body["id"], body["nombreRecurso"],body["abreviatura"],body["nombreMetrica"],body["tipo"],body["valor"])
                if(tcDatabase.agregarRecursos(recurso)):
                    return{'msg':'Recurso creado exitosamente.'}, 201 #created
                else:
                    return{'msg': 'El recurso ya se encuentra registrado.'}, 406 #Not acceptable
            else:
                return{'msg': 'Error en los campos'}, 406 #Not acceptable         
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500 #internal server error

@recursos.route('', methods = ['PUT'])
def modificar():
    body = request.get_json()
    try:
        if("id" in body and "nombreRecurso" in body and "abreviatura" in body and "nombreMetrica" in body and "tipo" in body and "valor" in body):
            if(body["id"] != "" and body["nombreRecurso"] != "" and body["abreviatura"] != "" and body["nombreMetrica"] != "" and body["tipo"] != "" and body["valor"] != ""):
                if(tcDatabase.modificarRecursos(body["id"], body["nombreRecurso"], body["abreviatura"], body["nombreMetrica"],body["tipo"],body["valor"])):
                    return{'msg':'Recurso modificado exitosamente.'}, 201 #created
                else:
                    return{'msg': 'No se encontró el recurso.'}, 406 #Not acceptable
            else:
                return{'msg': 'Error en los campos'}, 406 #Not acceptable         
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500 #internal server error

@recursos.route('', methods = ['GET'])
def buscar():
    id = request.args.get('id')
    try:
        if(id != None):
            recursosl = tcDatabase.buscarRecursosid(id)
            return jsonify(recursosl), 200 #ok
        else:
            recursosl = tcDatabase.buscarRecursos()
            return jsonify(recursosl), 200 #ok
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500 #internal server error