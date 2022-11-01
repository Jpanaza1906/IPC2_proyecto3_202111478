from flask import Flask, request, jsonify
from flask_cors import CORS
#RUTAS
from clientes.routes.clientes_route import clientes
from consumos.routes.consumos_route import consumos
from categorias.routes.categorias_route import categorias
from recursos.routes.recursos_route import recursos
from configuraciones.routes.configuraciones_route import configuraciones
from instancias.routes.instancias_route import instancias
from reportes.routes.reportes_route import reportes
#CLASES
from clientes.models.clientes_model import Clientes
from consumos.models.consumos_model import Consumos
from categorias.models.categorias_model import Categorias
from recursos.models.recursos_model import Recursos
from configuraciones.models.configuraciones_model import Configuraciones
from instancias.models.instancias_model import Instancias
#DATABASE
from db.database import tcDatabase
#XML
from xml.etree import ElementTree as ET

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return{"msg": "Si trabaja"}
#LOGIN
@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    try:
        if("usuario" in body and "clave" in body):
            if(body["usuario"] != "" and body["clave"] != ""):
                if(tcDatabase.login(body["usuario"],body["clave"])):
                    return {'msg': 'Bienvenido, credenciales correctas'}, 200
                else:
                    return{'msg': 'Credenciales incorrectas.'}, 406 #not acceptable
            pass
    except:
        return {'msg' : 'Ocurrió un error en el servidor'}, 500
#CARGAR ARCHIVO CONFIGURACION XML
@app.route('/cargarArchivo', methods = ['POST'])
def cargaCompleta():
    xml = request.data.decode('utf-8')
    raiz = ET.XML(xml)
    for firstchild in raiz:
        if(firstchild.tag.lower() == "listarecursos"):
            #en lista de recursos
            for recurso in firstchild:
                id = recurso.attrib["id"]
                for params in recurso:
                    parametro = params.tag.lower()
                    if(parametro == "nombre"):
                        nombre = params.text.strip()
                    elif(parametro == "abreviatura"):
                        abreviatura = params.text.strip()
                    elif(parametro == "metrica"):
                        metrica = params.text.strip()
                    elif(parametro == "tipo"):
                        tipo = params.text.strip()
                    elif(parametro == "valorxhora"):
                        valor = params.text.strip()
                nrecurso = Recursos(id, nombre, abreviatura, metrica, tipo, valor)
                tcDatabase.agregarRecursos(nrecurso)
        elif(firstchild.tag.lower() == "listacategorias"):
            for categoria in firstchild:
                id = categoria.attrib["id"]
                for params in categoria:
                    parametro = params.tag.lower()
                    if(parametro == "nombre"):
                        nombre = params.text.strip()
                    elif(parametro == "descripcion"):
                        descripcion = params.text.strip()
                    elif(parametro == "cargatrabajo"):
                        cargatrabajo = params.text.strip()
                    elif(parametro == "listaconfiguraciones"):
                        ncategoria = Categorias(id, nombre, descripcion,cargatrabajo)
                        tcDatabase.agregarCategorias(ncategoria)
                        for configs in params:
                            idconfig = configs.attrib["id"]
                            for paramconfig in configs:
                                if(paramconfig.tag == "nombre"):
                                    nombreconfig = paramconfig.text.strip()
                                elif(paramconfig.tag == "descripcion"):
                                    descripconfig = paramconfig.text.strip()
                                elif(paramconfig.tag == "recursosConfiguracion"):
                                    nconfig = Configuraciones(idconfig,nombreconfig, descripconfig)
                                    tcDatabase.agregarConfiguraciones(nconfig)
                                    for nrecur in paramconfig:
                                        idrecur = nrecur.attrib["id"]
                                        cantidad = nrecur.text.strip()
                                        tcDatabase.asignarRecursos(idconfig,idrecur,cantidad)
                            tcDatabase.asignarConfiguracion(id, idconfig)
        elif(firstchild.tag.lower() == "listaclientes"):
            for clientes in firstchild:
                id = clientes.attrib["nit"]
                for params in clientes:
                    parametro = params.tag.lower()
                    if(parametro == "nombre"):
                        nombre = params.text.strip()
                    elif(parametro == "usuario"):
                        usuario = params.text.strip()
                    elif(parametro == "clave"):
                        clave = params.text.strip()
                    elif(parametro == "direccion"):
                        direccion = params.text.strip()
                    elif(parametro == "correoelectronico"):
                        mail = params.text.strip()
                    elif(parametro == "listainstancias"):
                        ncliente = Clientes(id, nombre, usuario, clave, direccion, mail)
                        tcDatabase.agregarCliente(ncliente)
                        for instancia in params:
                            idinstancia = instancia.attrib["id"]
                            for paraminstancia in instancia:
                                if(paraminstancia.tag == "idConfiguracion"):
                                    idconfig = paraminstancia.text.strip()
                                elif(paraminstancia.tag == "nombre"):
                                    nombreins = paraminstancia.text.strip()
                                elif(paraminstancia.tag == "fechaInicio"):
                                    fechainicio = paraminstancia.text.strip()
                                elif(paraminstancia.tag == "estado"):
                                    estado = paraminstancia.text.strip()
                                elif(paraminstancia.tag == "fechaFinal"):
                                    fechafin = paraminstancia.text.strip()
                            ninstancia = Instancias(idinstancia, idconfig, nombreins, fechainicio, estado, fechafin)
                            tcDatabase.agregarInstancias(ninstancia)
                            tcDatabase.asignarinstancia(id, idinstancia)
    return {'msg': 'Carga completa'},200
#CARGAR ARCHIVO CONSUMO XML
@app.route('/cargaConsumo', methods = ['POST'])
def cargaConsumo():
    xml = request.data.decode('utf-8')
    raiz = ET.XML(xml)
    for consumo in raiz:
        nitcliente =  consumo.attrib['nitCliente']
        idinstancia = consumo.attrib['idInstancia']
        for params in consumo:
            if(params.tag == "tiempo"):
                tiempo = params.text.strip()
            elif(params.tag == "fechaHora"):
                fechaHora = params.text.strip()
        nconsumo = Consumos(nitcliente, idinstancia, tiempo, fechaHora)
        tcDatabase.agregarConsumos(nconsumo)
    return {'msg': 'Carga completa'}, 200

#GENERAR FACTURA
@app.route('/generarFactura', methods = ['GET'])
def generarFactura():
    fechaini = request.args.get('fechaini')
    fechafin = request.args.get('fechafin')
    if(fechaini != None and fechafin != None):
        facturasl = tcDatabase.generarFacturas(fechaini, fechafin)
        return jsonify(facturasl), 200

#CONSULTAR DATOS
@app.route('/consultarDatos', methods = ['GET'])
def consultarDatos():
    respuesta = tcDatabase.guardarBase()
    return respuesta, 200

app.register_blueprint(clientes)
app.register_blueprint(consumos)
app.register_blueprint(categorias)
app.register_blueprint(recursos)
app.register_blueprint(configuraciones)
app.register_blueprint(instancias)
app.register_blueprint(reportes)

if __name__ == '__main__':
    app.run(debug=True)
