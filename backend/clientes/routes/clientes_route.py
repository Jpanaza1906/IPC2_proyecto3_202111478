import json
from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from clientes.models.clientes_model import Clientes
from instancias.model.instancias_model import Instancias

clientes = Blueprint('clientes', __name__, url_prefix="/clientes")

#------------------------METODOS----------------------------------
@clientes.route('', methods = ['POST'])
def crear():
    body = request.get_json()
    try:
        if("nit" in body and "nombre" in body and "usuario" in body and "clave" in body and "direccion" in body and "email" in body):
            if(body["nit"] != "" and body["nombre"] != "" and body["usuario"] != "" and body["clave"] != "" and body["direccion"] != "" and body["email"] != ""): 
                cliente = Clientes(body["nit"], body["nombre"], body["usuario"], body["clave"], body["direccion"],body["email"])                
                if(tcDatabase.agregarCliente(cliente)):
                    return{'msg':'Cliente creado exitosamente.'}, 201 #created
                else:
                    return{'msg': 'El Nit del cliente ya se encuentra registrado.'}, 406 #Not acceptable
            else:
                return{'msg': 'Error en los campo'}, 406 #Not acceptable         
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500 #internal server error

@clientes.route('', methods = ['PUT'])
def modificar():
    return {'msg' : 'Clientes metodo get'}

@clientes.route('', methods = ['GET'])
def buscar():
    return {'msg' : 'Clientes metodo get'}