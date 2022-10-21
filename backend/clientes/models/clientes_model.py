from flask import jsonify
class Clientes:
    def __init__(self, nit, nombre, usuario, clave, direccion, mail):
        self.id = nit
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.direccion = direccion
        self.mail = mail
        self.instancias = []
    
    def asignar_instancias(self, instancia):
        self.instancias.append(instancia)
    
    def getdata(self):
        instanciar = []
        for ninstancia in self.instancias:
            instanciar.append(ninstancia.getdata())
        return{
            "nit" : self.id,
            "nombre" : self.nombre,
            "usuario": self.usuario,
            "clave": self.clave,
            "direccion": self.direccion,
            "email": self.mail,
            "instancias": jsonify(instanciar)
        }