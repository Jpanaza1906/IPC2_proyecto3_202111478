from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from categorias.models.categorias_model import Categorias
from configuraciones.models.configuraciones_model import Configuraciones

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