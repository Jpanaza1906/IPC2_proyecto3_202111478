from flask import jsonify
class Configuraciones():
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.idrecursos = []
        self.cantidadr = []
        self.use = 0
    def asignar_recursos(self, idrecurso, cantidad):
        self.idrecursos.append(idrecurso)
        self.cantidadr.append(cantidad)
    def getdata(self):
        nrecurr = ""
        for i in range(0,len(self.idrecursos)):
            nrecurr += "[ " + self.idrecursos[i] +"-" + self.cantidadr[i] + "], "
        return{
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'recursos_adquiridos': nrecurr
        }
        