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
                return{'msg': 'Error en los campos'}, 406 #Not acceptable         
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500 #internal server error

@clientes.route('', methods = ['PUT'])
def modificar():
    body = request.get_json()
    try:
        if("nit" in body and "nombre" in body and "usuario" in body and "clave" in body and "direccion" in body and "email" in body):
            if(body["nit"] != "" and body["nombre"] != "" and body["usuario"] != "" and body["clave"] != "" and body["direccion"] != "" and body["email"] != ""):
                if(tcDatabase.modificarCliente(body["nit"], body["nombre"], body["usuario"], body["clave"], body["direccion"], body["email"])):
                    return{'msg':'Cliente modificado exitosamente.'}, 201 #created
                else:
                    return{'msg': 'El NIT del cliente no se encontró.'}, 406 #Not acceptable
            else:
                return{'msg': 'Error en los campos'}, 406 #Not acceptable         
        else:
            return{'msg': 'Asegurese de introducir correctamente TODOS los campos'}, 400 #bad request
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500 #internal server error

@clientes.route('', methods = ['GET'])
def buscar():
    id = request.args.get('id')
    try:
        if(id != None):
            clientesl = tcDatabase.buscarClienteid(id)
            return jsonify(clientesl), 200 #ok
        else:
            clientesl = tcDatabase.buscarCliente()
            return jsonify(clientesl), 200 #ok
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500 #internal server error