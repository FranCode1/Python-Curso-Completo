# =====================================================================
# EJERCICIO 80: Clase Carrito de Compras
# ---------------------------------------------------------------------
# Crear una clase Producto con los siguientes atributos:
# • nombre
# • precio
# • cantidad
# Crear una lista que cargue varios productos (no hace falta que lo
# cargue el usuario).
# Recorre la lista y muestra el total a pagar.
# =====================================================================

class Carrito:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def  mostrar_datos(self):
        print(f"Nombre: {self.nombre} \nPrecio: {self.precio} \nCantidad: {self.cantidad}")

# Establece la cantidad de productos a ingresar
cantidad = 3

# Lista con los productos guardados
chango = []

# Recorre todos los productos
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    # Guarda todos nombre, precio y cantidad de cada producto
    bolsa = Carrito(nombre, precio, cantidad)
    # Luego lo agrega dentro de un diccionario y lo guarda en la lista
    chango.append(bolsa)

# Muestra todos los datos de la lista "chango"
for producto in chango:
    producto.mostrar_datos()