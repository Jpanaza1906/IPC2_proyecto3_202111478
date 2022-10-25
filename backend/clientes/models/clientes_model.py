from flask import jsonify
class Clientes:
    def __init__(self, nit, nombre, usuario, clave, direccion, mail):
        self.id = nit
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.direccion = direccion
        self.mail = mail
        self.idinstancias = []
    
    def asignar_idinstancias(self, idinstancia):
        self.idinstancias.append(idinstancia)
    
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