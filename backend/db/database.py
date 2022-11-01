from datetime import *
from distutils.command.config import config
from db.factura import Factura
from reportes.models.reportes_model import PDF
from fpdf import FPDF
class Database():
    def __init__(self):
        #Clientes
        self.clientes = []
        self.idclientes = []
        #Consumos
        self.consumos = []
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
        #facturas
        self.facturas = []
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
        if (consumo.idcliente in self.idclientes and consumo.idinstancia in self.idinstancias):
            cont = 0
            for cliente in self.clientes:
                if(cliente.id == consumo.idcliente):
                    if(len(self.clientes[cont].idinstancias) > 0):
                        self.clientes[cont].idinstancias.remove(consumo.idinstancia)
                cont += 1
            conti = 0
            for instancia in self.instancias:
                if(instancia.id == consumo.idinstancia):
                    self.instancias[conti].estado = "Cancelada"
                    self.instancias[conti].fechafin = consumo.descripfechahora
                    consumo.instancia = instancia
                conti+=1
            self.consumos.append(consumo)
            return True
        return False
                    
    #buscar
    def buscarConsumos(self):
        consumosf = []
        for consumo in self.consumos:
            consumosf.append(consumo.getdata())
        return consumosf
    
    def buscarConsumosid(self, idcliente, idinstancia):
        consumosf = []
        for consumo in self.consumos:
            if consumo.idcliente == idcliente and consumo.idinstancia == idinstancia:
                consumosf.append(consumo.getdata())
        return consumosf
    
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
            if(instancia.idconfig in self.idconfiguraciones):
                self.instancias.append(instancia)
                self.idinstancias.append(instancia.id)
                return True
            else:
                return False
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
    #generar facturas por consumos
    def generarFacturas(self, fechaini, fechafin):
        fechainicial = self.getfecha(fechaini)
        fechafinal = self.getfecha(fechafin)        
        for consumo in self.consumos:
            total = 0
            if(consumo.estadofac == False):
                consumo.estadofac = True
                fechaconsumo = self.getfecha(consumo.descripfechahora)
                if(fechaconsumo < fechafinal and fechaconsumo > fechainicial):
                    idinstancia = consumo.idinstancia
                    for instancia in self.instancias:
                        if(idinstancia == instancia.id):
                            idconfig = instancia.idconfig
                            for configuracion in self.configuraciones:
                                if(idconfig == configuracion.id):
                                    for i in range(0,len(configuracion.idrecursos)):
                                        idrecur = configuracion.idrecursos[i]
                                        cantidad = configuracion.cantidadr[i]
                                        tiempo = consumo.tiempo
                                        for recurso in self.recursos:
                                            if idrecur == recurso.id:
                                                total += (float(recurso.valor) * float(cantidad) * float(tiempo))                                    
                    nfactura = Factura(consumo.idcliente, consumo.descripfechahora, round(total,2))
                    nfactura.consumo = consumo
                    self.facturas.append(nfactura)
        facturasf = []
        for factura in self.facturas:
            facturasf.append(factura.getdata())
        return facturasf
    def getfecha(self, fecha):
        numeros = "0123456789"
        fechabuena = ""
        contsimb = 0
        contnum = 0
        for cadachar in fecha:
            if numeros.find(cadachar) != -1:
                fechabuena += cadachar
                contnum += 1
            elif cadachar == "/" and contnum == 2:
                fechabuena += cadachar
                contsimb += 1
                contnum = 0
            elif contnum == 4 and contsimb == 2:
                break
        if contnum == 4 and contsimb == 2:
            fechabuena = fechabuena.split('/')
            b1 = date(int(fechabuena[2]), int(fechabuena[1]), int(fechabuena[0]))
            return b1                
        return False
                
    #Guardar en archivo XML
    def guardarBase(self):
        texto = "<?xml version=\"1.0\"?>\n<archivoConfiguraciones>\n"
        
        #recursos
        texto += "<listaRecursos>\n"
        for recurso in self.recursos:
            texto += "<recurso id=\"" + recurso.id + "\">\n"
            texto += "<nombre>" + recurso.nombreRecurso + "</nombre>\n"
            texto += "<abreviatura>" + recurso.abreviatura + "</abreviatura>\n"
            texto += "<metrica>" + recurso.nombreMetrica + "</metrica>\n"
            texto += "<tipo>" + recurso.tipo + "</tipo>\n"
            texto += "<valorXhora>" + recurso.valor + "</valorXhora>\n"
            texto += "</recurso>"
        texto += "</listaRecursos>\n"
        
        #categorias
        texto += "<listaCategorias>\n"
        for categoria in self.categorias:
            texto += "<categoria id=\"" + categoria.id + "\">\n"
            texto += "<nombre>" + categoria.nombre + "</nombre>\n"
            texto += "<descripcion>" + categoria.descripCat + "</descripcion>\n"
            texto += "<cargaTrabajo>" + categoria.descripTrabajo + "</cargaTrabajo>\n"
            #configuraciones
            texto += "<listaConfiguraciones>\n"
            for idconfig in categoria.idconfiguraciones:
                for configuracion in self.configuraciones:
                    if idconfig == configuracion.id:
                        texto += "<configuracion id=\"" + configuracion.id + "\">\n"
                        texto += "<nombre>" + configuracion.nombre + "</nombre>\n"
                        texto += "<descripcion>"+ configuracion.descripcion + "</descripcion>\n"
                        #recursos
                        texto += "<recursosConfiguracion>\n"
                        for i in range(0,len(configuracion.idrecursos)):
                            texto += "<recurso id=\"" + configuracion.idrecursos[i] + "\">" + configuracion.cantidadr[i] + "</recurso>\n"
                        texto += "</recursosConfiguracion>\n"
                        texto += "</configuracion>\n"
            texto += "</listaConfiguraciones>\n"
            texto += "</categoria>\n"
        texto += "</listaCategorias>\n"
        
        #clientes
        texto += "<listaClientes>\n"
        for cliente in self.clientes:
            texto += "<cliente nit=\"" + cliente.id + "\">\n"
            texto += "<nombre>" + cliente.nombre + "</nombre>\n"
            texto += "<usuario>" + cliente.usuario + "</usuario>\n"
            texto += "<clave>" + cliente.clave + "</clave>\n"
            texto += "<direccion>" + cliente.direccion + "</direccion>\n"
            texto += "<correoElectronico>" + cliente.mail + "</correoElectronico>\n"
            #instancia
            texto += "<listaInstancias>\n"
            for idinstancia in cliente.idinstancias:
                for instancia in self.instancias:
                    if idinstancia == instancia.id:
                        texto += "<instancia id=\"" + instancia.id + "\">\n"
                        texto += "<idConfiguracion>" + instancia.idconfig + "</idConfiguracion>\n"
                        texto += "<nombre>" + instancia.nombre + "</nombre>\n"
                        texto += "<fechaInicio>" + instancia.fechaini + "</fechaInicio>\n"
                        texto += "<estado>" + instancia.estado + "</estado>\n"
                        texto += "<fechaFinal>" + instancia.fechafin + "</fechaFinal>"
                        texto += "</instancia>\n"
            texto += "</listaInstancias>\n"
            texto += "</cliente>\n"           
        texto += "</listaClientes>\n"
        texto += "</archivoConfiguraciones>"
        archivo1 = open("base.xml", "w")
        archivo1.write(texto)
        archivo1.close()
        return texto
    
    #reporte detalle de pago
    def detallePago(self, idfactura):
        texto = ""
        for nfactura in self.facturas:
            if(nfactura.id == idfactura): 
                texto += "No Factura:" + nfactura.id + "\n"
                texto += "NIT: " + nfactura.nit +"\n"
                consumofac = nfactura.consumo
                tiempo = consumofac.tiempo                
                texto += "Tiempo consumido: " + tiempo + " horas \n\n"
                idinstancia = consumofac.idinstancia
                for instancia in self.instancias:
                    if(instancia.id == idinstancia):
                        idconfig = instancia.idconfig
                        for configuracion in self.configuraciones:
                            if(configuracion.id == idconfig):
                                for i in range(0, len(configuracion.idrecursos)):
                                    idrecurso = configuracion.idrecursos[i]
                                    cantidad = configuracion.cantidadr[i]
                                    for recurso in self.recursos:
                                        if(recurso.id == idrecurso):
                                            total = float(cantidad) * float(recurso.valor) * float(tiempo)
                                            texto += cantidad + " - " + recurso.nombreRecurso + "- valor por hora (" + str(recurso.valor) +") = Q " + "\t" + str(round(total,2)) + "\n"                                          
                        texto += "\nTOTAL INSTANCIA: " + instancia.nombre +"\t = Q " + str(nfactura.monto) + "\n"
                pdf = PDF()
                pdf.add_page()
                pdf.logo('logotec.jpg', 0, 0, 60, 45)
                pdf.texts(texto)
                pdf.titles("Facturacion")
                pdf.output(nfactura.id + ".pdf", 'F')
                return True
        return False
    
    #reporte categorias y configuraciones mas usadas
    def masusadas(self, fechaini, fechafin):
        fechainicial = self.getfecha(fechaini)
        fechafinal = self.getfecha(fechafin)
        for instancia in self.instancias:
            for configuracion in self.configuraciones:
                if configuracion.id == instancia.idconfig:
                    configuracion.use = 0
        idsconfig = []
        for instancia in self.instancias:
            inifechainstancia = self.getfecha(instancia.fechaini)
            finfechainstancia = self.getfecha(instancia.fechafin)
            if(inifechainstancia > fechainicial and inifechainstancia < fechafinal):
                if(finfechainstancia == False):
                    idsconfig.append(instancia.idconfig)
                    for configuracion in self.configuraciones:
                        if configuracion.id == instancia.idconfig:
                            configuracion.use += 1
                elif(finfechainstancia < fechafinal):
                    idsconfig.append(instancia.idconfig)
                    for configuracion in self.configuraciones:
                        if configuracion.id == instancia.idconfig:
                            configuracion.use += 1
                
        nconfigmayor = 0
        for nidconfig in idsconfig:
            for configuracion in self.configuraciones:
                if(nidconfig == configuracion.id):
                    if (configuracion.use > nconfigmayor):
                        nconfigmayor = configuracion.use
        
        
        texto = "CATEGORIAS Y CONFIGURACIONES MÁS UTILIZADA DESDE " + fechaini + " HASTA " + fechafin + "\n\n"
        for nidconfig in idsconfig:
            for configuracion in self.configuraciones:
                if(nidconfig == configuracion.id):
                    if(configuracion.use == nconfigmayor):
                        for categoria in self.categorias:
                            for idconfig in categoria.idconfiguraciones:
                                if(idconfig == configuracion.id):
                                    texto += "- CATEGORIA: " + categoria.nombre + " - " + categoria.id + "\n"
                                    texto += "  Descripcion: " + categoria.descripCat + "\n"
                                    texto += "- CONFIGURACION: " + configuracion.nombre + " - " + configuracion.id + "\n"
                                    texto += "  Descripcion: " + configuracion.descripcion + "\n"
                                    texto += "Utilizada: " + str(configuracion.use) + " veces" + "\n\n"

        pdf = PDF()
        pdf.add_page()
        pdf.logo('logotec.jpg', 0, 0, 60, 45)
        pdf.texts(texto)
        pdf.output("Masuso.pdf", 'F')
        
                
tcDatabase = Database()