from flask import jsonify
class Categorias():
    def __init__(self, id, nombre, descripCat, descripTrabajo):
        self.id = id
        self.nombre = nombre
        self.descripCat = descripCat
        self.descripTrabajo = descripTrabajo
        self.idconfiguraciones = []
    def asignar_idconfiguraciones(self, idconfiguracion):
        self.idconfiguraciones.append(idconfiguracion)
    def getdata(self):
        configs = ""
        for nconfig in self.idconfiguraciones:
            configs += nconfig + ", "
        return{
            "id" : self.id,
            "nombre" : self.nombre,
            "descripCat": self.descripCat,
            "descripTrabajo": self.descripTrabajo,
            "configuraciones": configs
        }