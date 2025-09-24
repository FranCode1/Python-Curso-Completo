# ----------------------------------------
# CLASE 26: HERENCIA Y POLIMORFISMO EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es la herencia?
# La herencia permite que una clase (hija o subclase) reutilice atributos y métodos
# de otra clase (padre o superclase).
# Esto favorece la reutilización y organización del código.

# 📌 ¿Qué es el polimorfismo?
# Polimorfismo significa "muchas formas".
# Permite que diferentes clases usen un mismo método con comportamientos distintos.


# ==========================
# 🔹 HERENCIA BÁSICA
# ==========================

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido.")

# Clase Perro hereda de Animal
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau 🐶")

# Clase Gato hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):
        print("Miau 🐱")

perro = Perro("Firulais")
gato = Gato("Mishi")

perro.hacer_sonido()  # Guau
gato.hacer_sonido()   # Miau


# ==========================
# 🔹 FUNCIÓN POLIMÓRFICA
# ==========================

# Una misma función puede trabajar con distintos tipos de objetos
def hacer_hablar(animal):
    animal.hacer_sonido()

hacer_hablar(perro)
hacer_hablar(gato)


# ==========================
# 🔹 USO DE super()
# ==========================
# super() permite llamar al constructor o métodos de la clase padre

class Estudiante(Animal):
    def __init__(self, nombre, curso):
        super().__init__(nombre)   # Llamamos al constructor de Animal
        self.curso = curso

    def presentarse(self):
        print(f"Soy {self.nombre} y estudio {self.curso}.")

est = Estudiante("Franco", "Python Avanzado")
est.presentarse()


# ==========================
# 🔹 HERENCIA MÚLTIPLE
# ==========================
# Python permite heredar de múltiples clases (con orden de resolución de métodos: MRO)

class Volador:
    def volar(self):
        print("Estoy volando ✈️")

class Nadador:
    def nadar(self):
        print("Estoy nadando 🐟")

class Pato(Animal, Volador, Nadador):
    def hacer_sonido(self):
        print("Cuac 🦆")

pato = Pato("Donald")
pato.hacer_sonido()
pato.volar()
pato.nadar()


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================
# 🎯 Crear una jerarquía de clases para un sistema de empleados.
# - Clase base: Empleado (nombre, salario, mostrar_info)
# - Subclase: Programador (lenguaje, sobrescribe mostrar_info)
# - Subclase: Diseñador (herramienta, sobrescribe mostrar_info)

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, Salario: ${self.salario}")

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def mostrar_info(self):
        print(f"Programador: {self.nombre}, Lenguaje: {self.lenguaje}, Salario: ${self.salario}")

class Diseñador(Empleado):
    def __init__(self, nombre, salario, herramienta):
        super().__init__(nombre, salario)
        self.herramienta = herramienta

    def mostrar_info(self):
        print(f"Diseñador: {self.nombre}, Herramienta: {self.herramienta}, Salario: ${self.salario}")

# Probar mini proyecto
prog = Programador("Franco", 3000, "Python")
des = Diseñador("Lucía", 2800, "Figma")

prog.mostrar_info()
des.mostrar_info()


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es la herencia y cómo crear subclases
# - Cómo funciona el polimorfismo en Python
# - Uso de super() para acceder a la clase padre
# - Herencia múltiple y orden de resolución de métodos (MRO)
# - Cómo modelar relaciones en un sistema con herencia

# Próxima clase: Sobrecarga de operadores en Python (__add__, __len__, etc.)
