# ----------------------------------------
# CLASE 29: METACLASSES EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es una metaclase?
# - En Python, TODO es un objeto, incluidas las clases.
# - Una metaclase es la "clase de una clase".
# - Se usa para controlar cómo se crean y configuran las clases.
#
# 🔹 Ejemplo simple:
# type(obj) -> devuelve la clase del objeto
# type(clase) -> devuelve la metaclase (normalmente "type")

# ==========================
# 🔹 EJEMPLO 1: type como metaclase
# ==========================

# Normalmente definimos clases con 'class'
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

p = Persona("Franco")
print(type(p))       # <class '__main__.Persona'>
print(type(Persona)) # <class 'type'>  <-- la metaclase por defecto

# También podemos crear una clase directamente con type()
Animal = type("Animal", (), {"es_vivo": True})
print(Animal)        # <class '__main__.Animal'>
print(Animal.es_vivo) # True


# ==========================
# 🔹 EJEMPLO 2: Creando nuestra metaclase
# ==========================

# Creamos una metaclase que modifica automáticamente las clases
class MiMeta(type):
    def __new__(mcs, nombre, bases, diccionario):
        print(f"Creando la clase {nombre} con metaclase {mcs.__name__}")
        diccionario["creado_por"] = "MiMeta"
        return super().__new__(mcs, nombre, bases, diccionario)

# Clase que usará la metaclase
class Ejemplo(metaclass=MiMeta):
    pass

e = Ejemplo()
print(e.creado_por)  # "MiMeta"


# ==========================
# 🔹 EJEMPLO 3: Validación automática con metaclases
# ==========================

class ValidarAtributos(type):
    def __new__(mcs, nombre, bases, diccionario):
        if "saludar" not in diccionario:
            raise TypeError(f"La clase {nombre} debe implementar un método 'saludar'")
        return super().__new__(mcs, nombre, bases, diccionario)

# Esta clase NO dará error porque implementa saludar
class Correcto(metaclass=ValidarAtributos):
    def saludar(self):
        return "Hola!"

# Esta clase lanzará error al crearse porque no define 'saludar'
# class Incorrecto(metaclass=ValidarAtributos):
#     pass


# ==========================
# 🔹 MINI PROYECTO: Registro automático de clases
# ==========================
# 🎯 Queremos que cada vez que se cree una clase con nuestra metaclase,
# se registre automáticamente en un diccionario central.

registro_clases = {}

class RegistroMeta(type):
    def __new__(mcs, nombre, bases, diccionario):
        cls = super().__new__(mcs, nombre, bases, diccionario)
        registro_clases[nombre] = cls
        return cls

class A(metaclass=RegistroMeta):
    pass

class B(metaclass=RegistroMeta):
    pass

print(registro_clases)
# {'A': <class '__main__.A'>, 'B': <class '__main__.B'>}


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué son las metaclases (clases de las clases)
# - Cómo Python usa 'type' como metaclase por defecto
# - Cómo crear tus propias metaclases
# - Ejemplos prácticos: añadir atributos automáticos, validación, registro de clases

# Próxima clase: Decoradores avanzados en Python
