from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from categorias.models.categorias_model import Categorias
from configuraciones.models.configuraciones_model import Configuraciones

categorias =  Blueprint('categorias', __name__,url_prefix="/categorias")

#------------------METODOS----------------------------------------
@categorias.route('', methods = ['POST'])
def crear():
    return {'msg' : 'Categorias metodo post'}

@categorias.route('', methods = ['PUT'])
def modificar():
    return {'msg' : 'Categorias metodo get'}

@categorias.route('', methods = ['GET'])
def buscar():
    return {'msg' : 'Categorias metodo get'}