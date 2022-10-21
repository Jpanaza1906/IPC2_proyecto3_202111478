class Database():
    def __init__(self) -> None:
        #Clientes
        self.clientes = []
        self.idclientes = []
        #Consumos
        self.consumos = []
        self.idconsumos = []
        #Recursos
        self.recursos = []
        self.idrecursos = []
        #Categorias
        self.categorias = []
        self.idcategorias = []
    #CLIENTES
    def agregarCliente(self, cliente):
        if not(cliente.id in self.idclientes):
            self.clientes.append(cliente)
            self.idclientes.append(cliente.id)
            return True
        return False
    #CONSUMOS
    def agregarConsumos(self, consumo):
        if not(consumo.id in self.idconsumos):
            self.consumos.append(consumo)
            self.idconsumos.append(consumo.id)
            return True
        return False
    #RECURSOS
    def agregarRecursos(self, recurso):
        if not(recurso.id in self.idrecursos):
            self.recursos.append(recurso)
            self.idrecursos.append(recurso.id)
            return True
        return False
    #CATEGORÍAS
    def agregarCategorias(self, categoria):
        if not(categoria.id in self.idcategorias):
            self.categorias.append(categoria)
            self.idcategorias.append(categoria.id)
            return True
        return False
    
tcDatabase = Database()