from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from configuraciones.models.configuraciones_model import Configuraciones

configuraciones = Blueprint('configuraciones', __name__, url_prefix="/configuraciones")

#----------------------------METODOS-------------------------------------
@configuraciones.route('', methods = ['POST'])
def crear():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in body and "descripcion" in body):
            if(body["id"] != "" and body["nombre"] != "" and body["descripcion"] != ""):
                configuracion = Configuraciones(body["id"], body["nombre"], body["descripcion"])
                if(tcDatabase.agregarConfiguraciones(configuracion)):
                    return{'msg': 'Configuracion creada exitosamente.'}, 201 #created
                else:
                    return{'msg': 'Configuracion ya se encuentra registrada.'}, 406 #not acceptable
            else:
                return{'msg': 'El contenido de los campos no es válido.'}, 400 #bad request
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos.'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500

@configuraciones.route('',methods = ['PUT'])
def modificar():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in  body and "descripcion"):
            if(body["id"] != "" and body["nombre"] != "" and body["descripcion"] != ""):
                if(tcDatabase.modificarConfiguraciones(body["id"],body["nombre"],body["descripcion"])):
                    return{'msg': 'Configuracion modificada exitosamente.'}, 200 #ok
                else:
                    return{'msg': 'Configuracion no encontrada.'}, 200 #ok
            else:
                return{'msg': 'El contenido de los campos no es válido.'}, 404 #not found
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos.'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500

@configuraciones.route('', methods = ['GET'])
def buscar():
    id = request.args.get('id')
    try:
        if(id != None):
            configuracionesl = tcDatabase.buscarConfiguracionesid(id)
            return jsonify(configuracionesl), 200 #ok
        else:
            configuracionesl = tcDatabase.buscarConfiguraciones()
            return jsonify(configuracionesl), 200 #ok
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500

@configuraciones.route('', methods = ['DELETE'])
def eliminar():
    id = request.args.get('id')
    try:
        if (id != None):
            if(tcDatabase.eliminarConfiguraciones(id)):                
                return {'msg' : 'La configuracion fue eliminada exitosamente'}, 200
            else:
                return {'msg' : 'No se encontro el id'}, 200
        else:
            return {'msg' : 'No se tienen los parametros suficientes'}, 200
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500
    
@configuraciones.route('', methods = ['PATCH'])
def asignarinstancia():
    idconfig = request.args.get('idconfig')
    idrecurso = request.args.get('idrecurso')
    cantidad = request.args.get('cantidad')
    try:
        if (idconfig != None and idrecurso != None and cantidad != None):
            if(tcDatabase.asignarRecursos(idconfig,idrecurso,cantidad)):                
                return {'msg' : 'El recurso fue asignado correctamente'}, 200
            else:
                return {'msg' : 'No se encontro el id'}, 200
        else:
            return {'msg' : 'No se tienen los parametros suficientes'}, 200
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500