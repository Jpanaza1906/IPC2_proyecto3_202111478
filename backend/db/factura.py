from uuid import uuid4;
class Factura():
    def __init__(self, nit, fecha, monto):
        self.id = str(uuid4())
        self.nit = nit
        self.fecha = fecha
        self.monto = monto
        self.consumo = None
        
    def getdata(self):
        return{
            'id': self.id,
            'nit': self.nit,
            'fecha': self.fecha,
            'monto': self.monto
        }