from http import client


class Database():
    def __init__(self):
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
    #CLIENTES --------------------------------------------------------------------
    #agregar
    def agregarCliente(self, cliente):
        if not(cliente.id in self.idclientes):
            self.clientes.append(cliente)
            self.idclientes.append(cliente.id)
            return True
        return False
    #modificar
    def modificarCliente(self, nit, nombre, usuario, clave, direccion, mail):
        if nit in self.idclientes:
            for cliente in self.clientes:
                if cliente.id == nit:
                    cliente.nombre = nombre
                    cliente.usuario = usuario
                    cliente.clave = clave
                    cliente.direccion = direccion
                    cliente.mail = mail
                    return True
        return False
    #eliminar
    def eliminarCliente(self, nit):
        if nit in self.idclientes:
            cont = 0
            for cliente in self.clientes:
                if cliente.id == nit:
                    self.clientes[cont].pop()
                    return True
                cont += 1
        return False
    #buscar
    def buscarCliente(self):
        clientesf = []
        for cliente in self.clientes:
            clientesf.append(cliente.getdata())
        return clientesf
    
    def buscarClienteid(self, nit):
        if nit in self.idclientes:
            for cliente in self.clientes:
                if cliente.id == nit:
                    return cliente.getdata()
        return False    
    
    
    #CONSUMOS -------------------------------------------------------------------
    #agregar
    def agregarConsumos(self, consumo):
        if not(consumo.id in self.idconsumos):
            self.consumos.append(consumo)
            self.idconsumos.append(consumo.id)
            return True
        return False
    #eliminar
    def eliminarConsumos(self, id):
        if id in self.idconsumos:
            cont = 0
            for consumo in self.consumos:
                if consumo.id == id:
                    self.consumos[cont].pop()
                    return True
                cont += 1
        return False
                    
    #buscar
    def buscarConsumos(self):
        consumosf = []
        for consumo in self.consumos:
            consumosf.append(consumo.getdata())
        return consumosf
    
    def buscarConsumosid(self, id):
        if id in self.idconsumos:
            for consumo in self.consumos:
                if consumo.id == id:
                    return consumo.getdata()
        return False
    
    #RECURSOS -------------------------------------------------------------------
    #agregar
    def agregarRecursos(self, recurso):
        if not(recurso.id in self.idrecursos):
            self.recursos.append(recurso)
            self.idrecursos.append(recurso.id)
            return True
        return False
    #modificar
    def modificarRecursos(self, id, nombreRecurso, abreviatura, nombreMetrica, tipo, valor):
        if id in self.idrecursos:
            for recurso in self.recursos:
                if recurso.id == id:
                    recurso.nombreRecurso = nombreRecurso
                    recurso.abreviatura = abreviatura
                    recurso.nombreMetrica = nombreMetrica
                    recurso.tipo = tipo
                    recurso.valor = valor
                    return True
        return False                    
    #eliminar
    def eliminarRecursos(self, id):
        if id in self.idrecursos:
            cont = 0
            for recurso in self.recursos:
                if recurso.id == id:
                    self.recursos[cont].pop()
                    return True
                cont += 1
        return False
                    
    #buscar
    def buscarRecursos(self):
        recursosf = []
        for recurso in self.recursos:
            recursosf.append(recurso.getdata())
        return recursosf
    
    def buscarRecursosid(self, id):
        if id in self.idrecursos:
            for recurso in self.recursos:
                if recurso.id == id:
                    return recurso.getdata()
        return False
    
    #CATEGORÍAS -----------------------------------------------------------
    #agregar
    def agregarCategorias(self, categoria):
        if not(categoria.id in self.idcategorias):
            self.categorias.append(categoria)
            self.idcategorias.append(categoria.id)
            return True
        return False
    #modificar
    def modificarCategorias(self, id, nombre, descripCat, descripTrabajo):
        if id in self.idcategorias:
            for categoria in self.categorias:
                if categoria.id == id:
                    categoria.nombre = nombre
                    categoria.descripCat = descripCat
                    categoria.descripTrabajo = descripTrabajo
                    return True
        return False
    #eliminar
    def eliminarCategorias(self, id):
        if id in self.idcategorias:
            cont = 0
            for categoria in self.categorias:
                if categoria.id == id:
                    self.categorias[cont].pop()
                    return True
            cont += 1
        return False
                    
    #buscar
    def buscarCategorias(self):
        categoriasf = []
        for categoria in self.categorias:
            categoriasf.append(categoria.getdata())
        return categoriasf
    
    def buscarCategoriasid(self, id):
        if id in self.idcategorias:
            for categoria in self.categorias:
                if categoria.id == id:
                    return categoria.getdata()
        return False
    
tcDatabase = Database()