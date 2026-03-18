import datetime # para las operaciones que requieran fechas (préstamos)

class Material:
    def __init__(self,idMaterial,titulo,añoPublicacion,disponible):
        self.idMaterial=idMaterial
        self.titulo=titulo
        self.añoPublicacion=añoPublicacion
        self.disponible=disponible

class Libro(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible,autor,isbn,genero):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.autor=autor
        self.isbn=isbn
        self.genero=genero

class Revista(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible,edicion,periodicidad):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.edicion=edicion
        self.periodicidad=periodicidad

class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible,tipoArchivo,urlDescarga,tamañoMB):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.tipoArchivo=tipoArchivo
        self.urlDescarga=urlDescarga
        self.tamañoMB=tamañoMB

class Persona:
    def __init__(self,idPersona,nombre,email,telefono):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email
        self.telefono=telefono
    
    def login(self):
        print(f"Sesión iniciada para: {self.nombre}")
    
    def logout(self):
        print(f"Sesión concluida para: {self.nombre}")
    
    def actualizarPerfil(self,email,telefono):
        self.email=email
        self.telefono=telefono
        print(f"Datos actualizados para: {self.nombre}")

class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, telefono,limitePrestamos):
        super().__init__(idPersona, nombre, email, telefono)
        self.limitePrestamos=limitePrestamos
        self.listaActiva=[]

class Sucursal:
    def __init__(self,idSucursal,nombre):
        self.idSucursal=idSucursal
        self.nombre=nombre
        self.catalogoLocal=[]

class Bibliotecario(Persona):
    def __init__(self, idPersona, nombre, email, telefono):
        super().__init__(idPersona, nombre, email, telefono)
    
    # Aquí uso pistas de tipo para usuario y material
    # para que reciban las instancias de esas clases, y no sean simples datos.
    # También en otros métodos que requieran toda la instancia de algún objeto
    def gestionarPrestamo(self,usuario:Usuario,material:Material,idPrestamo):
        # verifica si el material está disponible
        if not material.disponible:
            print(f"El material: {material.titulo}, no está disponible")
            return
        
        # verifica si el numero de materiales que tiene la persona supera a su límite de préstamos
        if len(usuario.listaActiva)>=usuario.limitePrestamos:
            print(f"{usuario.nombre} ha alcanzado su límite de préstamos")
            return
        
        # el material pasa a no estar disponible
        material.disponible=False
        # se usa la librería "datetime" para obtener la fecha del día de préstamo
        hoy=datetime.date.today()
        # ".timedelta" se usa para el incremento de tiempo
        devolucion=hoy+datetime.timedelta(weeks=2)
        
        # se crea un nuevo préstamo y se añade a la lista activa del usuario
        prestamo=Prestamo(idPrestamo,hoy,devolucion,usuario,material)
        usuario.listaActiva.append(prestamo)
        
        print(f"Préstamo realizado: {material.titulo} prestado a {usuario.nombre}")
    
    def transferirMaterial(self,material:Material,origen:Sucursal,destino:Sucursal):
        if material in origen.catalogoLocal:
            origen.catalogoLocal.remove(material)
            destino.catalogoLocal.append(material)
            print(f"{material.titulo} transferido de {origen.nombre} a {destino.nombre}")
        else:
            print(f"Error: el material no está en la sucursal de origen")

class Prestamo:
    def __init__(self,idPrestamo,fechaInicio,fechaDevolucion,usuario:Usuario,material:Material):
        self.idPrestamo=idPrestamo
        self.fechaInicio=fechaInicio
        self.fechaDevolucion=fechaDevolucion
        self.usuario=usuario
        self.material=material

class Penalización:
    # aquí tomé a "monto" como los días de atraso, 
    # porque sería un poco absurdo que el usuario anote su monto
    def __init__(self,monto,motivo,pagada):
        self.monto=monto
        self.motivo=motivo
        self.pagada=pagada
    
    def calcularMulta(self):
        multa=self.monto*5
        print(f"Multa calculada: ${multa} por {self.monto} días de retraso")
    
    def bloquearUsuario(self,usuario:Usuario):
        print(f"{usuario.nombre} bloqueado. Motivo: {self.motivo}")
        

class Catálogo:
    def buscarPorAutor(self,autor,sucursal:Sucursal):
        busqueda=False
        for material in sucursal.catalogoLocal:
            # "isinstance" valida que sea un Libro, ya que Revista o MaterialDigital no tienen el atributo "autor"
            if isinstance(material,Libro) and material.autor==autor:
                # aquí en vez de escribir:
                #   if material.disponible: estado="Disponible" 
                #   else: estado="Prestado"
                # puedo ocupar un operador ternario para que se vea mejor:
                estado="Disponible" if material.disponible else "Prestado"
                print(f"*{material.titulo} ({estado})")
                busqueda=True
        if not busqueda:
            print("No se encontraron resultados")
    
    def buscarEnTodasSucursales(self,titulo,lista_sucursales):
        for sucursal in lista_sucursales:
            for material in sucursal.catalogoLocal:
                if material.titulo==titulo:
                    print(f"Material encontrado en: {sucursal.nombre}")
                    # aquí termina la búsqueda si lo encuentra
                    return 
        print("Material no encontrado en ninguna sucursal")