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
        #Configuraciones
        self.configuraciones = []
        self.idconfiguraciones = []
        #Instancias
        self.instancias = []
        self.idinstancias = []
    #LOGIN ------------------------------------------------
    def login(self, usuario, clave):
        for cliente in self.clientes:
            if(usuario == cliente.usuario and clave == cliente.clave):
                return True
        return False
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
                    self.clientes.pop(cont)
                    self.idclientes.pop(cont)
                    return True
                cont +=1
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
    
    #agregar instancia al cliente
    def asignarinstancia(self,idcliente, idinstancia):
        if idcliente in self.idclientes and idinstancia in self.idinstancias:
            cont = 0
            for cliente in self.clientes:
                if(cliente.id == idcliente):
                    for instancia in self.instancias:
                        if(instancia.id == idinstancia):                            
                            self.clientes[cont].asignar_idinstancias(instancia.id)
                            return True
                cont +=1
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
                if str(consumo.id) == str(id):
                    self.consumos.pop(cont)
                    self.idconsumos.pop(cont)
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
                    self.recursos.pop(cont)
                    self.idrecursos.pop(cont)
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
                    self.categorias.pop(cont)
                    self.idcategorias.pop(cont)
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
    
    #asignar configuraciones
    def asignarConfiguracion(self, idcat, idconfig):
        if idcat in self.idcategorias and idconfig in self.idconfiguraciones:
            cont = 0
            for categoria in self.categorias:
                if(categoria.id == idcat):
                    for configuracion in self.configuraciones:
                        if(configuracion.id == idconfig):
                            self.categorias[cont].asignar_idconfiguraciones(configuracion.id)
                            return True
                cont += 1
        return False
            
    #CONFIGURACIONES -----------------------------------------------------------
    #agregar
    def agregarConfiguraciones(self, configuracion):
        if not(configuracion.id in self.idconfiguraciones):
            self.configuraciones.append(configuracion)
            self.idconfiguraciones.append(configuracion.id)
            return True
        return False
    #modificar
    def modificarConfiguraciones(self, id, nombre, descripcion):
        if id in self.idconfiguraciones:
            for configuracion in self.configuraciones:
                if configuracion.id == id:
                    configuracion.nombre = nombre
                    configuracion.descripcion = descripcion
                    return True
        return False
    #eliminar
    def eliminarConfiguraciones(self, id):
        if id in self.idconfiguraciones:
            cont = 0
            for configuracion in self.configuraciones:
                if configuracion.id == id:
                    self.configuraciones.pop(cont)
                    self.idconfiguraciones.pop(cont)
                    return True
                cont += 1
        return False
                    
    #buscar
    def buscarConfiguraciones(self):
        configuracionesf = []
        for configuracion in self.configuraciones:
            configuracionesf.append(configuracion.getdata())
        return configuracionesf
    
    def buscarConfiguracionesid(self, id):
        if id in self.idconfiguraciones:
            for configuracion in self.configuraciones:
                if configuracion.id == id:
                    return configuracion.getdata()
        return False
    #asignar recursos
    def asignarRecursos(self, idconfig, idrecurso, cantidad):
        if idconfig in self.idconfiguraciones and idrecurso in self.idrecursos:
            cont = 0
            for configuracion in self.configuraciones:
                if(configuracion.id == idconfig):
                    for recurso in self.recursos:
                        if(recurso.id == idrecurso):
                            self.configuraciones[cont].asignar_recursos(recurso.id, cantidad)
                            return True
                cont += 1
        return False
    #INSTANCIAS -----------------------------------------------------------
    #agregar
    def agregarInstancias(self, instancia):
        if not(instancia.id in self.idinstancias):
            self.instancias.append(instancia)
            self.idinstancias.append(instancia.id)
            return True
        return False
    #modificar
    def modificarInstancias(self, id, idconfig, nombre, fechaini, estado, fechafin):
        if id in self.idinstancias:
            for instancia in self.instancias:
                if instancia.id == id:
                    instancia.idconfig = idconfig
                    instancia.nombre = nombre
                    instancia.fechaini = fechaini
                    instancia.estado = estado
                    instancia.fechafin = fechafin
                    return True
        return False
    #eliminar
    def eliminarInstancias(self, id):
        if id in self.idinstancias:
            cont = 0
            for instancia in self.instancias:
                if instancia.id == id:
                    self.instancias.pop(cont)
                    self.idinstancias.pop(cont)
                    return True
                cont += 1
        return False
                    
    #buscar
    def buscarInstancias(self):
        instanciasf = []
        for instancia in self.instancias:
            instanciasf.append(instancia.getdata())
        return instanciasf
    
    def buscarInstanciasid(self, id):
        if id in self.idinstancias:
            for instancia in self.instancias:
                if instancia.id == id:
                    return instancia.getdata()
        return False
tcDatabase = Database()