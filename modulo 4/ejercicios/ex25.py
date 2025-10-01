# ----------------------------------------
# CLASE 26: HERENCIA Y POLIMORFISMO - EJERCICIOS RESUELTOS
# ----------------------------------------

# ========================================
# EJERCICIO 1: Herencia básica
# Consigna: Crear una clase Vehiculo con método arrancar().
# Hacer que Coche y Moto hereden de Vehiculo y sobrescriban arrancar().
# ========================================

class Vehiculo:
    def arrancar(self):
        print("El vehículo arranca 🚗")

class Coche(Vehiculo):
    def arrancar(self):
        print("El coche arranca con llave 🔑")

class Moto(Vehiculo):
    def arrancar(self):
        print("La moto arranca con botón ⚡")

coche = Coche()
moto = Moto()
coche.arrancar()
moto.arrancar()


# ========================================
# EJERCICIO 2: Uso de super()
# Consigna: Crear una clase Persona con nombre.
# Subclase Estudiante que además tenga curso y use super() en el constructor.
# ========================================

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, curso):
        super().__init__(nombre)
        self.curso = curso

    def presentarse(self):
        print(f"Soy {self.nombre} y estudio {self.curso} 📖")

estu = Estudiante("Franco", "Python")
estu.presentarse()


# ========================================
# EJERCICIO 3: Polimorfismo con animales
# Consigna: Crear clases Perro y Gato con un método hablar().
# Usar una función que reciba cualquier animal y ejecute hablar().
# ========================================

class Perro:
    def hablar(self):
        print("Guau 🐶")

class Gato:
    def hablar(self):
        print("Miau 🐱")

def hacer_hablar(animal):
    animal.hablar()

hacer_hablar(Perro())
hacer_hablar(Gato())


# ========================================
# EJERCICIO 4: Herencia múltiple
# Consigna: Crear clases Volador y Nadador. Crear PezVolador que herede de ambas.
# ========================================

class Volador:
    def volar(self):
        print("Estoy volando ✈️")

class Nadador:
    def nadar(self):
        print("Estoy nadando 🐟")

class PezVolador(Volador, Nadador):
    pass

pez = PezVolador()
pez.volar()
pez.nadar()


# ========================================
# EJERCICIO 5: Clase abstracta simulada
# Consigna: Crear una clase Instrumento con método tocar().
# Crear Guitarra y Piano que sobrescriban tocar().
# ========================================

class Instrumento:
    def tocar(self):
        print("Sonido de instrumento 🎵")

class Guitarra(Instrumento):
    def tocar(self):
        print("La guitarra suena 🎸")

class Piano(Instrumento):
    def tocar(self):
        print("El piano suena 🎹")

def concierto(instr):
    instr.tocar()

concierto(Guitarra())
concierto(Piano())


# ========================================
# EJERCICIO 6: Polimorfismo en listas
# Consigna: Crear una lista con varios objetos (Gato, Perro, Guitarra) y
# recorrerla ejecutando su método particular.
# ========================================

objetos = [Perro(), Gato(), Guitarra()]
for obj in objetos:
    obj.hablar() if hasattr(obj, "hablar") else obj.tocar()


# ========================================
# EJERCICIO 7: Herencia en cadena
# Consigna: Crear la clase SerVivo → Animal → Ave → Loro.
# Que cada una agregue un comportamiento.
# ========================================

class SerVivo:
    def respirar(self):
        print("Respiro 🌬️")

class Animal(SerVivo):
    def mover(self):
        print("Me muevo 🚶")

class Ave(Animal):
    def poner_huevo(self):
        print("Pongo un huevo 🥚")

class Loro(Ave):
    def hablar(self):
        print("Hola, soy un loro 🦜")

loro = Loro()
loro.respirar()
loro.mover()
loro.poner_huevo()
loro.hablar()


# ========================================
# EJERCICIO 8: Empleados polimórficos
# Consigna: Clase base Empleado con mostrar_info().
# Subclases: Programador y Diseñador que sobrescriban mostrar_info().
# ========================================

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")

class Programador(Empleado):
    def mostrar_info(self):
        print(f"Programador: {self.nombre} 👨‍💻")

class Disenador(Empleado):
    def mostrar_info(self):
        print(f"Diseñador: {self.nombre} 🎨")

empleados = [Programador("Franco"), Disenador("Lucía"), Empleado("Carlos")]
for e in empleados:
    e.mostrar_info()


# ========================================
# EJERCICIO 9: Herencia múltiple con conflicto
# Consigna: Crear dos clases A y B con un mismo método.
# Hacer que C herede de A y B y ver el orden de resolución (MRO).
# ========================================

class A:
    def saludar(self):
        print("Hola desde A")

class B:
    def saludar(self):
        print("Hola desde B")

class C(A, B):
    pass

c = C()
c.saludar()  # Prioriza A por el orden de herencia


# ========================================
# EJERCICIO 10: Mini sistema de transporte
# Consigna: Clase base Transporte con metodo mover().
# Subclases: Auto, Bicicleta y Avion con comportamientos diferentes.
# ========================================

class Transporte:
    def mover(self):
        print("El transporte se mueve")

class Auto(Transporte):
    def mover(self):
        print("El auto se mueve por carretera 🚗")

class Bicicleta(Transporte):
    def mover(self):
        print("La bicicleta se mueve por pedales 🚴")

class Avion(Transporte):
    def mover(self):
        print("El avión se mueve por el aire ✈️")

transportes = [Auto(), Bicicleta(), Avion()]
for t in transportes:
    t.mover()

# ----------------------------------------
# ✅ Fin de los 10 ejercicios resueltos
# ----------------------------------------
