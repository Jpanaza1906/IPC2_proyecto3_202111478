class Consumos:
    def __init__(self, idcliente, idinstancia, tiempo, descripfechahora):
        self.idcliente = idcliente
        self.idinstancia = idinstancia
        self.tiempo = tiempo
        self.descripfechahora = descripfechahora
        self.estadofac = False
        self.instancia = None
    def getdata(self):
        return{
            'idcliente': self.idcliente,
            'idinstancia': self.idinstancia,
            'tiempo': self.tiempo,
            'descrip_fechahora': self.descripfechahora
        }