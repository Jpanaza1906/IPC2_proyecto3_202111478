from flask import Flask
from flask_cors import CORS
from clientes.routes.clientes_route import clientes
from consumos.routes.consumos_route import consumos
from categorias.routes.categorias_route import categorias
from recursos.routes.recursos_route import recursos
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return{"msg": "Si trabaja"}

app.register_blueprint(clientes)
app.register_blueprint(consumos)
app.register_blueprint(categorias)
app.register_blueprint(recursos)

if __name__ == '__main__':
    app.run(debug=True)
