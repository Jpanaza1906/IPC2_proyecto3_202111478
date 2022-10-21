from flask import Blueprint, jsonify, request
from db.database import tcDatabase
from consumos.models.consumos_model import Consumos

consumos = Blueprint('consumos', __name__, url_prefix="/consumos")

#---------------------MODELOS--------------------------------
@consumos.route('', methods = ['POST'])
def crear():
    return {'msg' : 'Consumos metodo post'}

@consumos.route('', methods = ['PUT'])
def modificar():
    return {'msg' : 'Consumos  metodo get'}

@consumos.route('', methods = ['GET'])
def buscar():
    return {'msg' : 'Consumos metodo get'}