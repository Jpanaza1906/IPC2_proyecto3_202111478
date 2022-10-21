import json
from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from clientes.models.clientes_model import Clientes
from instancias.model.instancias_model import Instancias

clientes = Blueprint('clientes', __name__, url_prefix="/clientes")

#------------------------METODOS----------------------------------
@clientes.route('', methods = ['POST'])
def crear():
    return {'msg' : 'Clientes metodo post'}

@clientes.route('', methods = ['PUT'])
def modificar():
    return {'msg' : 'Clientes metodo get'}

@clientes.route('', methods = ['GET'])
def buscar():
    return {'msg' : 'Clientes metodo get'}