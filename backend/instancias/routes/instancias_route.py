from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from instancias.models.instancias_model import Instancias

instancias = Blueprint('instancias', __name__, url_prefix="/instancias")

#----------------------METODOS------------------------------------------
@instancias.route('', methods = ['POST'])
def crear():
    body = request.get_json()
    try:
        if("id" in body and "idconfig" in body and "nombre" in body and "fechaini" in body and "estado" in body and "fechafin" in body):
            if(body["id"] != "" and body["idconfig"] != "" and body["nombre"] != "" and body["fechaini"] != "" and body["estado"] != ""):
                instancia = Instancias(body["id"], body["idconfig"], body["nombre"], body["fechaini"], body["estado"], body["fechafin"])
                if(tcDatabase.agregarInstancias(instancia)):
                    return{'msg': 'Instancia creada exitosamente.'}, 201 #created
                else:
                    return{'msg': 'Instancia ya se encuentra registrada o la configuracion no existe.'}, 406 #not acceptable
            else:
                return{'msg': 'El contenido de los campos no es válido.'}, 400 #bad request
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos.'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500

@instancias.route('', methods = ['PUT'])
def modificar():
    body = request.get_json()
    try:
        if("id" in body and "idconfig" in body and "nombre" in body and "fechaini" in body and "estado" in body and "fechafin" in body):
            if(body["id"] != "" and body["idconfig"] != "" and body["nombre"] != "" and body["fechaini"] != "" and body["estado"] != ""):
                if(tcDatabase.modificarInstancias(body["id"], body["idconfig"], body["nombre"], body["fechaini"], body["estado"], body["fechafin"])):
                    return{'msg': 'Instancia modificada exitosamente.'}, 200 #ok
                else:
                    return{'msg': 'Instancia no encontrada.'}, 200 #ok
            else:
                return{'msg': 'El contenido de los campos no es válido.'}, 404 #not found
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos.'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500

@instancias.route('', methods = ['GET'])
def buscar():
    id = request.args.get('id')
    try:
        if(id != None):
            instanciasl = tcDatabase.buscarInstanciasid(id)
            return jsonify(instanciasl), 200 #ok
        else:
            instanciasl = tcDatabase.buscarInstancias()
            return jsonify(instanciasl), 200 #ok
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500

@instancias.route('', methods = ['DELETE'])
def eliminar():
    id = request.args.get('id')
    try:
        if (id != None):
            if(tcDatabase.eliminarInstancias(id)):                
                return {'msg' : 'La instancia fue eliminada exitosamente'}, 200
            else:
                return {'msg' : 'No se encontro el id'}, 200
        else:
            return {'msg' : 'No se tienen los parametros suficientes'}, 200
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500