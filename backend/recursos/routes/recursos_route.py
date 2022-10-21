from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from recursos.models.recursos_model import Recursos

recursos = Blueprint('recursos', __name__, url_prefix="/recursos")

#------------------------------METODOS-----------------------------
@recursos.route('', methods = ['POST'])
def crear():
    return {'msg' : 'Recursos metodo post'}

@recursos.route('', methods = ['PUT'])
def modificar():
    return {'msg' : 'Recursos  metodo get'}

@recursos.route('', methods = ['GET'])
def buscar():
    return {'msg' : 'Recursos metodo get'}