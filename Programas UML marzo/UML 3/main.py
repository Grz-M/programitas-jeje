from models import *

# -Red de bibliotecas:

# sucursales y catálogo
suc_norte = Sucursal(1, "Biblioteca Norte")
suc_sur = Sucursal(2, "Biblioteca Sur")
catalogo = Catálogo() # se crea este objeto para poder ocupar los métodos de "Catálogo"

# administrador
admin = Bibliotecario(99, "Laura", "laura@biblio.com", "555-0000")

# 10 usuarios
u1 = Usuario(1, "Ana", "ana@mail.com", "555-01", 2)
u2 = Usuario(2, "Beto", "beto@mail.com", "555-02", 3)
u3 = Usuario(3, "Carlos", "carlos@mail.com", "555-03", 5)
u4 = Usuario(4, "Diana", "diana@mail.com", "555-04", 1)
u5 = Usuario(5, "Elena", "elena@mail.com", "555-05", 3)
u6 = Usuario(6, "Fernando", "fer@mail.com", "555-06", 2)
u7 = Usuario(7, "Gabriela", "gaby@mail.com", "555-07", 4)
u8 = Usuario(8, "Hugo", "hugo@mail.com", "555-08", 2)
u9 = Usuario(9, "Irene", "irene@mail.com", "555-09", 3)
u10 = Usuario(10, "Juan", "juan@mail.com", "555-10", 5)

# 10 libros
l1 = Libro(101, "1984", 1949, True, "George Orwell", "ISBN-1", "Ficción")
l2 = Libro(102, "Rebelión en la Granja", 1945, True, "George Orwell", "ISBN-2", "Sátira")
l3 = Libro(103, "Cien Años de Soledad", 1967, True, "Gabriel Garcia Marquez", "ISBN-3", "Realismo Mágico")
l4 = Libro(104, "El Aleph", 1949, True, "Jorge Luis Borges", "ISBN-4", "Fantasía")
l5 = Libro(105, "Ficciones", 1944, True, "Jorge Luis Borges", "ISBN-5", "Fantasía")
l6 = Libro(106, "Dune", 1965, True, "Frank Herbert", "ISBN-6", "Ciencia Ficción")
l7 = Libro(107, "Fundación", 1951, True, "Isaac Asimov", "ISBN-7", "Ciencia Ficción")
l8 = Libro(108, "Yo, Robot", 1950, True, "Isaac Asimov", "ISBN-8", "Ciencia Ficción")
l9 = Libro(109, "El Hobbit", 1937, True, "J.R.R. Tolkien", "ISBN-9", "Fantasía")
l10 = Libro(110, "Drácula", 1897, True, "Bram Stoker", "ISBN-10", "Terror")

# 10 revistas
r1 = Revista(201, "National Geographic", 2023, True, 150, "Mensual")
r2 = Revista(202, "Science", 2024, True, 800, "Semanal")
r3 = Revista(203, "Nature", 2024, True, 450, "Semanal")
r4 = Revista(204, "Time", 2023, True, 900, "Semanal")
r5 = Revista(205, "Forbes", 2023, True, 300, "Mensual")
r6 = Revista(206, "Wired", 2024, True, 120, "Mensual")
r7 = Revista(207, "The New Yorker", 2023, True, 500, "Semanal")
r8 = Revista(208, "Vogue", 2024, True, 400, "Mensual")
r9 = Revista(209, "GQ", 2023, True, 250, "Mensual")
r10 = Revista(210, "Rolling Stone", 2024, True, 350, "Mensual")

# 10 materiales digitales
d1 = MaterialDigital(301, "Aprende Python", 2022, True, "PDF", "url.com/py", 15.5)
d2 = MaterialDigital(302, "Java in Action", 2021, True, "EPUB", "url.com/java", 8.2)
d3 = MaterialDigital(303, "Clean Code", 2008, True, "PDF", "url.com/clean", 20.0)
d4 = MaterialDigital(304, "Patrones de Diseño", 1994, True, "PDF", "url.com/patrones", 18.4)
d5 = MaterialDigital(305, "Guía Linux", 2020, True, "EPUB", "url.com/linux", 5.0)
d6 = MaterialDigital(306, "Redes Informáticas", 2019, True, "PDF", "url.com/redes", 25.1)
d7 = MaterialDigital(307, "Bases de Datos", 2023, True, "PDF", "url.com/sql", 12.3)
d8 = MaterialDigital(308, "Machine Learning", 2024, True, "PDF", "url.com/ml", 30.5)
d9 = MaterialDigital(309, "Ciberseguridad", 2022, True, "EPUB", "url.com/sec", 7.8)
d10 = MaterialDigital(310, "Desarrollo Web", 2023, True, "PDF", "url.com/web", 14.2)

# aquí se reparte el material a las sucursales
suc_norte.catalogoLocal = [l1, l2, l3, l4, l5, r1, r2, r3, r4, r5, d1, d2, d3, d4, d5]
suc_sur.catalogoLocal = [l6, l7, l8, l9, l10, r6, r7, r8, r9, r10, d6, d7, d8, d9, d10]


# -Prueba de funciones:

print("\n-BÚSQUEDA POR AUTOR")
catalogo.buscarPorAutor("George Orwell", suc_norte); print("\n")
# esta es una prueba a un autor que no existe en el catálogo
catalogo.buscarPorAutor("Stephen King", suc_norte)

print("\n-GESTIONAR PRÉSTAMO Y LÍMITES")
u4.login(); print("\n")
admin.gestionarPrestamo(u4, l1, "PRE-001"); print("\n")
# aquí falla porque alcanzó su límite de préstamos
admin.gestionarPrestamo(u4, l2, "PRE-002"); print("\n")
# aquí falla porque ya lo tomó prestado otra persona
admin.gestionarPrestamo(u1, l1, "PRE-003")

print("\n-BÚSQUEDA GLOBAL")
# aquí se busca un libro en la otra sucursal
catalogo.buscarEnTodasSucursales("Dune", [suc_norte, suc_sur])

print("\n-TRANSFERENCIA DE MATERIAL")
admin.transferirMaterial(l6, suc_sur, suc_norte); print("\n")
# aquí se verifica el cambio de material de la sucursal
catalogo.buscarEnTodasSucursales("Dune", [suc_norte, suc_sur])

print("\n-PENALIZACIÓN")
# aquí son 4 días de retraso
multa_ana = Penalización(4, "Retraso en entrega", False); print("\n")
multa_ana.calcularMulta(); print("\n")
multa_ana.bloquearUsuario(u1); print("\n")

