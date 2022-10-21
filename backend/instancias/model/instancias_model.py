class Instancias():
    def __init__(self, id, idconfig, nombre, fechaini, estado, fechafin):
        self.id = id
        self.idconfig = idconfig
        self.nombre = nombre
        self.fechaini = fechaini
        self.estado = estado
        self.fechafin = fechafin
        pass
    def getdata(self):
        return{
            "id": self.id,
            "idconfig": self.idconfig,
            "nombre": self.nombre,
            "fechaini": self.fechaini,
            "estado": self.estado,
            "fechafin": self.fechafin
        }