class Recursos:
    def __init__(self, id, nombreRecurso, abreviatura, nombreMetrica, tipo, valor):
        self.id = id
        self.nombreRecurso = nombreRecurso
        self.abreviatura = abreviatura
        self.nombreMetrica = nombreMetrica
        self.tipo = tipo
        self.valor = valor
    def getdata(self):
        return{
            'id': self.id,
            'nombreRecurso': self.nombreRecurso,
            'abreviatura': self.abreviatura,
            'nombreMetrica': self.nombreMetrica,
            'tipo': self.tipo,
            'valor': self.valor
        }