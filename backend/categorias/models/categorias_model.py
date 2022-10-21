from flask import jsonify
class Categorias():
    def __init__(self, id, nombre, descripCat, descripTrabajo):
        self.id = id
        self.nombre = nombre
        self.descripCat = descripCat
        self.descripTrabajo = descripTrabajo
        self.configuraciones = []
    def asignar_configuraciones(self, configuracion):
        self.configuraciones.append(configuracion)
    def gedata(self):
        configr = []
        for nconfig in self.configuraciones:
            configr.append(nconfig.getdata())
        return{
            "id" : self.id,
            "nombre" : self.nombre,
            "descripCat": self.descripCat,
            "descripTrabajo": self.descripTrabajo,
            "configuraciones": jsonify(configr)
        }