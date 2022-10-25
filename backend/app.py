from flask import Flask
from flask_cors import CORS
from clientes.routes.clientes_route import clientes
from consumos.routes.consumos_route import consumos
from categorias.routes.categorias_route import categorias
from recursos.routes.recursos_route import recursos
from configuraciones.routes.configuraciones_route import configuraciones
from instancias.routes.instancias_route import instancias
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return{"msg": "Si trabaja"}

app.register_blueprint(clientes)
app.register_blueprint(consumos)
app.register_blueprint(categorias)
app.register_blueprint(recursos)
app.register_blueprint(configuraciones)
app.register_blueprint(instancias)

if __name__ == '__main__':
    app.run(debug=True)
