from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from categorias.models.categorias_model import Categorias

categorias =  Blueprint('categorias', __name__,url_prefix="/categorias")

#------------------METODOS----------------------------------------
@categorias.route('', methods = ['POST'])
def crear():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in  body and "descripCat" in body and "descripTrabajo" in body):
            if(body["id"] != "" and body["nombre"] != "" and body["descripCat"] != "" and body["descripTrabajo"] != ""):
                categoria = Categorias(body["id"], body["nombre"], body["descripCat"], body["descripTrabajo"])
                if(tcDatabase.agregarCategorias(categoria)):
                    return{'msg': 'Categoria creada exitosamente.'}, 201 #created
                else:
                    return{'msg': 'Categoria ya se encuentra registrada.'}, 406 #not acceptable
            else:
                return{'msg': 'El contenido de los campos no es válido.'}, 400 #bad request
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos.'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500

@categorias.route('', methods = ['PUT'])
def modificar():
    body = request.get_json()
    try:
        if("id" in body and "nombre" in  body and "descripCat" in body and "descripTrabajo" in body):
            if(body["id"] != "" and body["nombre"] != "" and body["descripCat"] != "" and body["descripTrabajo"] != ""):
                if(tcDatabase.modificarCategorias(body["id"],body["nombre"],body["descripCat"],body["descripTrabajo"])):
                    return{'msg': 'Categoria modificada exitosamente.'}, 200 #ok
                else:
                    return{'msg': 'Categoria no encontrada.'}, 200 #ok
            else:
                return{'msg': 'El contenido de los campos no es válido.'}, 404 #not found
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos.'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500
    

@categorias.route('', methods = ['GET'])
def buscar():
    id = request.args.get('id')
    try:
        if(id != None):
            categoriasl = tcDatabase.buscarCategoriasid(id)
            return jsonify(categoriasl), 200 #ok
        else:
            categoriasl = tcDatabase.buscarCategorias()
            return jsonify(categoriasl), 200 #ok
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500

@categorias.route('', methods = ['DELETE'])
def eliminar():
    id = request.args.get('id')
    try:
        if (id != None):
            if(tcDatabase.eliminarCategorias(id)):                
                return {'msg' : 'La categoria fue eliminada exitosamente'}, 200
            else:
                return {'msg' : 'No se encontro el id'}, 200
        else:
            return {'msg' : 'No se tienen los parametros suficientes'}, 200
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500

@categorias.route('', methods = ['PATCH'])
def asignarconfig():
    idcat = request.args.get('idcat')
    idconfig = request.args.get('idconfig')
    try:
        if (idconfig != None and idcat != None):
            if(tcDatabase.asignarConfiguracion(idcat,idconfig)):                
                return {'msg' : 'La configuracion fue asignada correctamente'}, 200
            else:
                return {'msg' : 'No se encontro el id'}, 200
        else:
            return {'msg' : 'No se tienen los parametros suficientes'}, 200
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500