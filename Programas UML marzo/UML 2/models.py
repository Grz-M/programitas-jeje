from enum import Enum

class Persona:
    def __init__(self,idPersona,nombre,email):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email
    
    def login(self):
        print(f"Sesión iniciada para: {self.nombre}")
    
    def actualizarPerfil(self,email):
        self.email=email
        print(f"Datos de {self.nombre} actualizados correctamente")

class Cliente(Persona):
    def __init__(self,idPersona,nombre,email,puntosFidelidad):
        super().__init__(idPersona,nombre,email)
        self.puntosFidelidad=puntosFidelidad
        self.historialPedidos=[]
    
    def realizarPedido(self,pedido):
        self.historialPedidos.append(pedido)
        self.puntosFidelidad+=pedido.total*0.1 
        print(f"Pedido {pedido.idPedido} realizado con éxito. Puntos actuales: {self.puntosFidelidad}")
    
    def consultarHistorial(self):
        print(f"Historial de Pedidos de {self.nombre}")
        for x in self.historialPedidos:
            # el ".name" es una propiedad del Enum para obtener el texto
            print(f"Pedido {x.idPedido}. Estado: {x.estado.name}. Total: ${x.total}")
    
    def canjearPuntos(self,puntos_a_usar):
        if self.puntosFidelidad>=puntos_a_usar:
            self.puntosFidelidad-=puntos_a_usar
            print(f"Se han canjeado {puntos_a_usar} puntos. Puntos restantes: {self.puntosFidelidad}")
        else:
            print("Puntos insuficientes para canjear")

Rol=Enum("Rol",["BARISTA","MESERO","GERENTE"])

class Empleado(Persona):
    def __init__(self,idEmpleado,nombre,email,rol:Rol,horario):
        super().__init__(idEmpleado,nombre,email)
        self.rol=rol
        self.horario=horario
    
    def actualizarInventario(self,inventario,ingrediente,cantidad):
        # el 0 del get, es el valor de retorno si no se encuentra ese ingrediente
        inventario.ingredientes[ingrediente]=inventario.ingredientes.get(ingrediente,0)+cantidad
        print(f"Inventario actualizado: {ingrediente} tiene {inventario.ingredientes[ingrediente]} unidades")
    
    def cambiarEstadoPedido(self,pedido,estado2):
        pedido.estado=estado2
        print(f"El estado del pedido {pedido.idPedido} ha cambiado a: {pedido.estado.name}")

Estado=Enum("Estado",["PENDIENTE","PREPARANDO","ENTREGADO"])

class Pedido:
    def __init__(self,idPedido,productos,estado:Estado):
        self.idPedido=idPedido
        self.productos=productos
        self.estado=estado
        self.total=self.calcularTotal()
    
    def calcularTotal(self): 
        suma=0
        for producto in self.productos:
            # isistance es una función que verifica si un objeto es una instancia de una clase específica
            if isinstance(producto,Bebida):
                suma+=producto.calcularPrecioFinal()
            else:
                suma+=producto.precioBase
        self.total=suma
        return suma
    
    def validarStock(self,inventario,ingrediente):
        # el len obtiene el número de elementos que hay en un objeto
        if inventario.ingredientes.get(ingrediente,0)>=len(self.productos):
            print("Stock válido para el pedido")
        else:
            inventario.notificarFaltante(ingrediente)

class ProductoBase:
    def __init__(self,idProducto,nombre,precioBase):
        self.idProducto=idProducto
        self.nombre=nombre
        self.precioBase=precioBase

Temp=Enum("Temperatura",["FRIA","CALIENTE"])

class Bebida(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase,tamaño,temperatura:Temp):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño=tamaño
        self.temperatura=temperatura
        self.modificadores=[]
    
    def agregarExtra(self,extra,costo):
        self.modificadores.append({"extra": extra, "precio": costo})
        print(f"Extra: {extra} (${costo}) agregado a {self.nombre}")
    
    def calcularPrecioFinal(self):
        costo_extra=sum(modificador["precio"] for modificador in self.modificadores)
        return self.precioBase+costo_extra

class Postre(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase,esVegano,sinGluten):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano=esVegano
        self.sinGluten=sinGluten

class Inventario:
    # investigué y no se usa el map en python, se ocupan diccionarios
    # por lo que "self.ingredientes=map" es incorrecto
    # y se usa "Type Hinting" en el constructor
    def __init__(self,ingredientes:dict):
        self.ingredientes=ingredientes
    
    def reducirStock(self,ingrediente,cantidad):
        if self.ingredientes.get(ingrediente,0)>=cantidad:
            self.ingredientes[ingrediente]-=cantidad
            print(f"Stock reducido. Quedan {self.ingredientes[ingrediente]} de {ingrediente}")
            if self.ingredientes[ingrediente]<5:
                self.notificarFaltante(ingrediente)
        else:
            print(f"Error: Stock insuficiente de {ingrediente}")
            self.notificarFaltante(ingrediente)
    
    def notificarFaltante(self,ingrediente):
        print(f"ALERTA. Es necesario reabastecer: {ingrediente}")
