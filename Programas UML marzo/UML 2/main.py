from models import *

# 1 inventario (porque no hace falta tener 10)
inv_central = Inventario({
    "Café": 50, "Leche": 40, "Azúcar": 100, "Vainilla": 20, 
    "Cacao": 30, "Harina": 50, "Huevos": 60, "Matcha": 15, 
    "Caramelo": 25, "Hielo": 100 })

# 10 empleados
e1 = Empleado(101, "Carlos", "carlos@cafe.com", Rol.GERENTE, "Matutino")
e2 = Empleado(102, "Diana", "diana@cafe.com", Rol.BARISTA, "Matutino")
e3 = Empleado(103, "Elena", "elena@cafe.com", Rol.BARISTA, "Vespertino")
e4 = Empleado(104, "Fernando", "fer@cafe.com", Rol.MESERO, "Matutino")
e5 = Empleado(105, "Gabriela", "gaby@cafe.com", Rol.MESERO, "Vespertino")
e6 = Empleado(106, "Hugo", "hugo@cafe.com", Rol.BARISTA, "Mixto")
e7 = Empleado(107, "Irene", "irene@cafe.com", Rol.MESERO, "Matutino")
e8 = Empleado(108, "Jorge", "jorge@cafe.com", Rol.MESERO, "Vespertino")
e9 = Empleado(109, "Karla", "karla@cafe.com", Rol.BARISTA, "Matutino")
e10 = Empleado(110, "Luis", "luis@cafe.com", Rol.GERENTE, "Vespertino")

# 10 clientes
c1 = Cliente(1, "Ana", "ana@mail.com", 50)
c2 = Cliente(2, "Beto", "beto@mail.com", 120)
c3 = Cliente(3, "Celia", "celia@mail.com", 0)
c4 = Cliente(4, "Daniel", "daniel@mail.com", 15)
c5 = Cliente(5, "Erika", "erika@mail.com", 200)
c6 = Cliente(6, "Fabian", "fabian@mail.com", 10)
c7 = Cliente(7, "Gloria", "gloria@mail.com", 80)
c8 = Cliente(8, "Hector", "hector@mail.com", 0)
c9 = Cliente(9, "Ines", "ines@mail.com", 300)
c10 = Cliente(10, "Juan", "juan@mail.com", 45)

# 10 bebidas
b1 = Bebida(201, "Americano", 30, "Mediano", Temp.CALIENTE)
b2 = Bebida(202, "Latte Clásico", 45, "Grande", Temp.CALIENTE)
b3 = Bebida(203, "Frappe Mocha", 60, "Grande", Temp.FRIA)
b4 = Bebida(204, "Espresso Doble", 35, "Chico", Temp.CALIENTE)
b5 = Bebida(205, "Té de Manzanilla", 25, "Mediano", Temp.CALIENTE)
b6 = Bebida(206, "Matcha Latte", 55, "Mediano", Temp.CALIENTE)
b7 = Bebida(207, "Cold Brew", 48, "Grande", Temp.FRIA)
b8 = Bebida(208, "Capuchino", 40, "Mediano", Temp.CALIENTE)
b9 = Bebida(209, "Smoothie Fresa", 50, "Grande", Temp.FRIA)
b10 = Bebida(210, "Chocolate Caliente", 38, "Mediano", Temp.CALIENTE)

# 10 postres
p1 = Postre(301, "Brownie de Chocolate", 35, False, False)
p2 = Postre(302, "Galleta de Avena", 20, True, False)
p3 = Postre(303, "Pastel de Zanahoria", 50, False, False)
p4 = Postre(304, "Cheesecake", 55, False, True)
p5 = Postre(305, "Muffin de Arándano", 28, False, False)
p6 = Postre(306, "Tartaleta de Frutas", 45, True, True)
p7 = Postre(307, "Croissant", 25, False, False)
p8 = Postre(308, "Panque de Limón", 30, False, False)
p9 = Postre(309, "Alfajor", 18, False, False)
p10 = Postre(310, "Macaron", 22, False, True)


# Prueba de funciones

print("-PERSONALIZACIÓN DE BEBIDAS")
b2.agregarExtra("Leche de Almendras", 12)
b2.agregarExtra("Shot de Vainilla", 8)
b3.agregarExtra("Crema Batida", 10)

print("\n-CREACIÓN Y CÁLCULO DE PEDIDOS")
ped1 = Pedido(1001, [b2, p1], Estado.PENDIENTE)
ped2 = Pedido(1002, [b3, p4, p4], Estado.PENDIENTE)
ped3 = Pedido(1003, [b1, b4], Estado.PENDIENTE)
ped4 = Pedido(1004, [b6, p2], Estado.PENDIENTE)
ped5 = Pedido(1005, [b8, p7], Estado.PENDIENTE)
ped6 = Pedido(1006, [b10, p1, p5], Estado.PENDIENTE)
ped7 = Pedido(1007, [b7, b9], Estado.PENDIENTE)
ped8 = Pedido(1008, [b5], Estado.PENDIENTE)
ped9 = Pedido(1009, [p3, p6], Estado.PENDIENTE)
ped10 = Pedido(1010, [b2, b2, p10], Estado.PENDIENTE)

ped1.calcularTotal()
ped2.calcularTotal()
ped10.calcularTotal()
print(f"Total Pedido 1: ${ped1.total}")
print(f"Total Pedido 10: ${ped10.total}")

print("\n-COMPRA Y STOCK")
c1.login()
if ped1.validarStock(inv_central,"Café"):
    c1.realizarPedido(ped1)
    inv_central.reducirStock("Café", 1)

print("\n-CHAMBA DE EMPLEADOS")
e2.cambiarEstadoPedido(ped1, Estado.PREPARANDO)
e1.actualizarInventario(inv_central, "Café", 20)
e2.cambiarEstadoPedido(ped1, Estado.ENTREGADO)

print("\n-CANJEO DE PUNTOS")
c1.consultarHistorial()
c1.canjearPuntos(50)

print("\n-ALERTA DE INVENTARIO")
inv_central.reducirStock("Matcha", 12)