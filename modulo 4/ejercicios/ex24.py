# ----------------------------------------
# CLASE 25: CLASES Y OBJETOS EN PYTHON - EJERCICIOS RESUELTOS
# ----------------------------------------

# ===============================================
# EJERCICIO 1 - Clase Estudiante
# ===============================================
# Consigna:
# Crear una clase Estudiante con nombre y nota. 
# Agregar un método que indique si aprobó (nota >= 6).

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobo(self):
        return self.nota >= 6

alumno = Estudiante("Franco", 8)
print(alumno.nombre, "aprobó?", alumno.aprobo())  # True


# ===============================================
# EJERCICIO 2 - Clase Producto
# ===============================================
# Consigna:
# Crear una clase Producto con nombre y precio.
# Incluir un método para aplicar descuento.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

p1 = Producto("Laptop", 1000)
p1.aplicar_descuento(10)
print(p1.nombre, "nuevo precio:", p1.precio)  # 900


# ===============================================
# EJERCICIO 3 - Clase Circulo
# ===============================================
# Consigna:
# Crear una clase Circulo con radio.
# Métodos para calcular área y circunferencia.

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def circunferencia(self):
        return 2 * math.pi * self.radio

c = Circulo(5)
print("Área:", c.area(), "Circunferencia:", c.circunferencia())


# ===============================================
# EJERCICIO 4 - Contador con atributo de clase
# ===============================================
# Consigna:
# Crear una clase que cuente cuántos objetos han sido creados.

class ContadorObjetos:
    cantidad = 0  # atributo de clase

    def __init__(self):
        ContadorObjetos.cantidad += 1

obj1 = ContadorObjetos()
obj2 = ContadorObjetos()
obj3 = ContadorObjetos()
print("Objetos creados:", ContadorObjetos.cantidad)  # 3


# ===============================================
# EJERCICIO 5 - Clase Libro con __str__
# ===============================================
# Consigna:
# Crear una clase Libro que muestre título y autor al imprimirse.

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

l = Libro("El Principito", "Saint-Exupéry")
print(l)


# ===============================================
# EJERCICIO 6 - Clase CuentaBancaria
# ===============================================
# Consigna:
# Crear una clase CuentaBancaria con saldo privado (__saldo).
# Métodos: depositar, retirar y mostrar saldo.

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Lucía", 500)
cuenta.depositar(200)
cuenta.retirar(100)
print("Saldo final:", cuenta.mostrar_saldo())  # 600


# ===============================================
# EJERCICIO 7 - Clase Rectangulo
# ===============================================
# Consigna:
# Crear una clase Rectangulo con métodos para calcular área y perímetro.

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

r = Rectangulo(4, 6)
print("Área:", r.area(), "Perímetro:", r.perimetro())


# ===============================================
# EJERCICIO 8 - Clase Empleado
# ===============================================
# Consigna:
# Crear una clase Empleado con nombre y sueldo.
# Método para calcular sueldo anual.

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def sueldo_anual(self):
        return self.sueldo * 12

emp = Empleado("Ana", 3000)
print(emp.nombre, "cobra al año:", emp.sueldo_anual())


# ===============================================
# EJERCICIO 9 - Clase Punto
# ===============================================
# Consigna:
# Crear una clase Punto con coordenadas x, y.
# Método para calcular distancia a otro punto.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otro):
        return math.sqrt((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2)

p1 = Punto(0, 0)
p2 = Punto(3, 4)
print("Distancia:", p1.distancia(p2))  # 5.0


# ===============================================
# EJERCICIO 10 - Clase Tienda
# ===============================================
# Consigna:
# Crear una clase Tienda que gestione productos.
# Métodos: agregar producto y mostrar lista.

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"Productos en {self.nombre}:")
        for p in self.productos:
            print("-", p)

tienda = Tienda("MiTienda")
tienda.agregar_producto("Manzanas")
tienda.agregar_producto("Pan")
tienda.mostrar_productos()
