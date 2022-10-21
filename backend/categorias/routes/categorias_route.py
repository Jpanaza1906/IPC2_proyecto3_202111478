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
    return {'msg' : 'Categorias metodo get'}

@categorias.route('', methods = ['GET'])
def buscar():
    return {'msg' : 'Categorias metodo get'}