from enum import Enum

class Persona:
    def __init__(self,idPersona,nombre,email,telefono):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email
        self.telefono=telefono
    
    def login(self):
        print(f"Sesión iniciada para: {self.nombre}")
    
    def logout(self):
        print(f"Sesión terminada para: {self.nombre}")
    
    def actualizarDatos(self,email,telefono):
        self.email=email
        self.telefono=telefono
        print(f"Datos de {self.nombre} actualizados correctamente")

class Usuario(Persona):
    def __init__(self,idPersona,nombre,email,telefono):
        super().__init__(idPersona,nombre,email,telefono)
        self.historialReservas=[]
    
    def crearReserva(self,pelicula,asientos):
        reserva = {"Pelicula": pelicula, "Asientos": asientos}
        self.historialReservas.append(reserva)
        print(f"Reserva creada con éxito para {pelicula}. Asientos: {', '.join(asientos)}")
    
    def consultarPromociones(self):
        print("Si tienes algún código y todavía no expira, puedes canjearlo")
    
    def cancelarReserva(self,pelicula):
        for x in self.historialReservas:
            if x["Pelicula"]==pelicula:
                self.historialReservas.remove(x)
                print(f"La reserva para {pelicula} ha sido cancelada")
                return
        print(f"No se encontró ninguna reserva para {pelicula}")

Rol=Enum("Rol",["TAQUILLERO","ADMIN","LIMPIEZA"])

class Empleado(Persona):
    def __init__(self,idEmpleado,nombre,email,telefono,horario,rol:Rol):
        super().__init__(idEmpleado,nombre,email,telefono)
        self.horario=horario
        self.rol=rol
    
    def marcarEntrada(self):
        print(f"Entrada registrada")
    
    def gestionarFunciones(self):
        if self.rol.name=="ADMIN":
            siono=input("Agregar nueva función?, SI o NO")
            if siono=="SI":
                print("Película agregada")
            else:
                print("No se ha agregado alguna película")
        else:
            print("Acceso denegado, solo administradores pueden gestionar funciones")

class Espacio:
    def __init__(self,idEspacio,nombre,ubicacion):
        self.idEspacio=idEspacio
        self.nombre=nombre
        self.ubicacion=ubicacion
    
    def verificarDisponibilidad(self):
        if self.ubicacion!="OCUPADO":
            print(f"El lugar: {self.nombre} está disponible")
        else:
            print("El lugar está ocupado")
    
    def limpiarEspacio(self):
        print(f"El lugar: {self.nombre} ha sido limpiado")

class ZonaComida(Espacio):
    def __init__(self,idEspacio,nombre,ubicacion):
        super().__init__(idEspacio,nombre,ubicacion)
        self.listaProductos=[]
        self.stockActual={}
    
    def venderProducto(self,producto,cantidad):
        if self.stockActual.get(producto,0)>=cantidad:
            print("Producto vendido")
        else:
            print("Stock insuficiente de ",producto)
    
    def actualizarInventario(self,producto,cantidad):
        self.stockActual[producto]=self.stockActual.get(producto,0)+cantidad
        print(f"Inventario actualizado: {producto} ahora tiene {self.stockActual[producto]} unidades")

Tipo=Enum("Tipo",["2D","3D","IMAX"])

class Sala(Espacio):
    def __init__(self,idEspacio,nombre,ubicacion,capacidadTotal,esVip,tipo:Tipo):
        super().__init__(idEspacio,nombre,ubicacion)
        self.capacidadTotal=capacidadTotal
        self.esVip=esVip
        self.tipo=tipo
    
    def ajustarAforo(self,capacidad):
        if capacidad<=self.capacidadTotal:
            self.capacidadTotal=capacidad
            print(f"Aforo {self.nombre} ajustado a {capacidad} personas")
        else:
            print("No puedes exceder la capacidad total")
    
    def obtenerTipoSala(self):
        if self.esVip:
            categoria="VIP"
        else:
            categoria="Tradicional"
        print(f"Esta es una sala {categoria} con tecnología {self.tipo}.")
        return f"{categoria} - {self.tipo}"

Estado=Enum("Estado",["PENDIENTE","PAGADA","CANCELADA"])

class Reserva:
    def __init__(self,idReserva,usuario,funcion,asientos,montoTotal,estado:Estado):
        self.idReserva=idReserva
        self.usuario=usuario
        self.funcion=funcion
        self.asientos=[]
        self.montoTotal=montoTotal
        self.estado=estado
    
    def confirmarPago(self):
        self.estado="PAGADA"
        print("Su pago ha sido confirmado")
    
    def generarTicket(self):
        if self.estado=="PAGADA":
            print("TICKET DE CINE")
            print(f"Película: {self.funcion}")
            print(f"Cliente: {self.usuario}")
            print(f"ID: {self.idReserva}")
        else:
            print("Tienes que confirmar antes el pago")
    
    def aplicarPromocion(self,promo):
        descuento=self.montoTotal*(promo/100)
        self.montoTotal-=descuento
        print("Promoción aplicada")
        print(f"Nuevo precio a pagar: ${self.montoTotal}")

class Funcion:
    def __init__(self,idFuncion,pelicula,sala,horarioInicio,precioBase):
        self.idFuncion=idFuncion
        self.pelicula=pelicula
        self.sala=sala
        self.horarioInicio=horarioInicio
        self.precioBase=precioBase
        self.asientos_ocupados=[]
    
    def calcularAsientosLibres(self):
        total=self.sala.capacidadTotal
        libres=total-len(self.asientos_ocupados)
        print(f"Asientos libres: {libres} de {total}")
        return libres
    
    def obtenerDetallesFuncion(self):
        detalles=(
            f"Película: {self.pelicula.titulo}\n"
            f"Sala: {self.sala.nombre} ({self.sala.tipo})\n"
            f"Inicia: {self.horarioInicio}\n"
            f"Precio: ${self.precioBase}"
            )
        print(detalles)
        return detalles

class Promocion:
    def __init__(self,codigo,descripcion,porcentajeDescuento,fechaExpiracion):
        self.codigo=codigo
        self.descripcion=descripcion
        self.porcentajeDescuento=porcentajeDescuento
        self.fechaExpiracion=fechaExpiracion
    
    def esValida(self,usuario):
        print(f"Validando promoción {self.codigo} para el usuario {usuario}")
        return True
    
    def aplicarDescuento(self,monto):
        descuento=monto*(self.porcentajeDescuento/100)
        montoFinal=monto-descuento
        print(f"Descuento aplicado. Total: ${montoFinal}")
        return montoFinal

class Pelicula:
    def __init__(self,titulo,duracion,clasificacion,genero):
        self.titulo=titulo
        self.duracion=duracion
        self.clasificacion=clasificacion
        self.genero=genero
    
    def obtenerSinopsis(self):
        return f"Sinopsis detallada de {self.titulo} ({self.genero})"
    
    def esAptaParaTodoPublico(self):
        if self.clasificacion=="A":
            print("Es apta para todo público")
        else:
            print("No es apta para todo público")