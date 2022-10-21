from uuid import uuid4
class Consumos:
    def __init__(self, idcliente, idinstancia, tiempo, descripfechahora):
        self.id = uuid4()
        self.idcliente = idcliente
        self.idinstancia = idinstancia
        self.tiempo = tiempo
        self.descripfechahora = descripfechahora
    def getdata(self):
        return{
            'id': self.id,
            'idcliente': self.idcliente,
            'idinstancia': self.idinstancia,
            'tiempo': self.tiempo,
            'descrip_fechahora': self.descripfechahora
        }