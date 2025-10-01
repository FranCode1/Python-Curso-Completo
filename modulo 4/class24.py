# ----------------------------------------
# CLASE 25: CLASES Y OBJETOS EN PYTHON
# ----------------------------------------

# 📌 ¿Qué son las clases y objetos?
# En Python, una clase es un molde o plantilla que define cómo crear objetos.
# Los objetos son instancias de una clase y contienen:
# - Atributos (variables que guardan datos)
# - Métodos (funciones que definen comportamiento)

# ==========================
# 🔹 DEFINIR UNA CLASE Y CREAR OBJETOS
# ==========================

class Persona:
    # Constructor con __init__
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo de instancia
        self.edad = edad      # atributo de instancia

    # Método de la clase
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear objetos (instancias)
persona1 = Persona("Franco", 22)
persona2 = Persona("Lucía", 25)

persona1.saludar()
persona2.saludar()


# ==========================
# 🔹 ATRIBUTOS DE CLASE VS. DE INSTANCIA
# ==========================

class Coche:
    ruedas = 4  # Atributo de clase (igual para todos los objetos)

    def __init__(self, marca, modelo):
        self.marca = marca      # Atributo de instancia
        self.modelo = modelo    # Atributo de instancia

    def descripcion(self):
        return f"{self.marca} {self.modelo}, Ruedas: {Coche.ruedas}"

auto = Coche("Toyota", "Corolla")
print(auto.descripcion())


# ==========================
# 🔹 MÉTODOS ESPECIALES (DUNDER METHODS)
# ==========================

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    # __str__ define cómo se imprime el objeto
    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

libro = Libro("1984", "George Orwell")
print(libro)  # Llama a __str__


# ==========================
# 🔹 ENCAPSULACIÓN
# ==========================
# Convenciones:
# - Público: atributo normal (self.nombre)
# - Protegido: atributo con _guion_bajo (self._saldo)
# - Privado: atributo con __doble_guion (self.__pin)

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo      # protegido
        self.__pin = 1234        # privado

    def depositar(self, cantidad):
        self._saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        return self._saldo

cuenta = CuentaBancaria("Franco", 1000)
cuenta.depositar(500)
print(cuenta.mostrar_saldo())  # 1500


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================
# 🎯 Crear una clase Rectangulo que calcule área y perímetro

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

rect = Rectangulo(10, 5)
print("Área:", rect.area())
print("Perímetro:", rect.perimetro())


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué son clases y objetos en Python
# - Diferencia entre atributos de clase y de instancia
# - Cómo usar métodos especiales como __str__
# - Encapsulación (público, protegido, privado)
# - Cómo modelar problemas con clases (mini proyecto de rectángulo)

# Próxima clase: Herencia y polimorfismo en Python.
