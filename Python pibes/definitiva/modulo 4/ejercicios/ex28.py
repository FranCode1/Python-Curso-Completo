# ----------------------------------------
# CLASE 29: METACLASSES EN PYTHON
# ----------------------------------------
# Ejercicios resueltos con consignas incluidas
# ----------------------------------------

# 📌 Recordatorio:
# - Una metaclase es la clase de la clase.
# - Se usa para personalizar cómo se crean y configuran las clases.
# - Normalmente, la metaclase por defecto es "type".
# ----------------------------------------


# ======================================================
# EJERCICIO 1: Crear una clase con type()
# Consigna: Crea una clase "Auto" usando type() en vez de class,
#           y agrega un atributo "ruedas" con valor 4.
# ======================================================
Auto = type("Auto", (), {"ruedas": 4})
a = Auto()
print("Ejercicio 1 →", a.ruedas)  # 4


# ======================================================
# EJERCICIO 2: Agregar atributo automático con metaclase
# Consigna: Define una metaclase que agregue el atributo "creador"
#           con tu nombre a todas las clases que usen esa metaclase.
# ======================================================
class MiMeta(type):
    def __new__(mcs, nombre, bases, diccionario):
        diccionario["creador"] = "Franco"
        return super().__new__(mcs, nombre, bases, diccionario)

class Persona(metaclass=MiMeta):
    pass

p = Persona()
print("Ejercicio 2 →", p.creador)  # Franco


# ======================================================
# EJERCICIO 3: Validación de métodos obligatorios
# Consigna: Crea una metaclase que obligue a definir un método "hablar"
#           en todas las clases que la usen.
# ======================================================
class ValidaHablar(type):
    def __new__(mcs, nombre, bases, diccionario):
        if "hablar" not in diccionario:
            raise TypeError(f"La clase {nombre} debe tener el método 'hablar'")
        return super().__new__(mcs, nombre, bases, diccionario)

class Robot(metaclass=ValidaHablar):
    def hablar(self):
        return "Beep bop"

print("Ejercicio 3 →", Robot().hablar())  # Beep bop


# ======================================================
# EJERCICIO 4: Registro automático de clases
# Consigna: Haz una metaclase que registre automáticamente
#           todas las clases creadas en un diccionario global.
# ======================================================
registro = {}

class RegistroMeta(type):
    def __new__(mcs, nombre, bases, diccionario):
        cls = super().__new__(mcs, nombre, bases, diccionario)
        registro[nombre] = cls
        return cls

class A(metaclass=RegistroMeta): pass
class B(metaclass=RegistroMeta): pass

print("Ejercicio 4 →", registro)  
# {'A': <class '__main__.A'>, 'B': <class '__main__.B'>}


# ======================================================
# EJERCICIO 5: Agregar método automáticamente
# Consigna: Define una metaclase que agregue a todas las clases
#           un método "info()" que devuelva el nombre de la clase.
# ======================================================
class InfoMeta(type):
    def __new__(mcs, nombre, bases, diccionario):
        def info(self): return f"Soy la clase {nombre}"
        diccionario["info"] = info
        return super().__new__(mcs, nombre, bases, diccionario)

class Animal(metaclass=InfoMeta): pass

print("Ejercicio 5 →", Animal().info())  # Soy la clase Animal


# ======================================================
# EJERCICIO 6: Controlar creación de atributos
# Consigna: Crea una metaclase que no permita definir
#           atributos con nombres en minúscula.
# ======================================================
class UpperAttrMeta(type):
    def __new__(mcs, nombre, bases, diccionario):
        for attr in diccionario:
            if attr.islower() and not attr.startswith("__"):
                raise TypeError(f"Atributo '{attr}' debe estar en MAYÚSCULAS")
        return super().__new__(mcs, nombre, bases, diccionario)

class Config(metaclass=UpperAttrMeta):
    MAX_USERS = 10

print("Ejercicio 6 →", Config.MAX_USERS)  # 10


# ======================================================
# EJERCICIO 7: Sobrescribir __call__
# Consigna: Crea una metaclase que muestre un mensaje
#           cada vez que se instancie una clase.
# ======================================================
class NotificaMeta(type):
    def __call__(cls, *args, **kwargs):
        print(f"Se está creando una instancia de {cls.__name__}")
        return super().__call__(*args, **kwargs)

class Usuario(metaclass=NotificaMeta):
    pass

u = Usuario()  # Mensaje automático
print("Ejercicio 7 → instancia creada")


# ======================================================
# EJERCICIO 8: Singleton con metaclase
# Consigna: Usa una metaclase para que solo exista una
#           instancia de una clase (patrón Singleton).
# ======================================================
class SingletonMeta(type):
    _instancias = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls._instancias[cls] = super().__call__(*args, **kwargs)
        return cls._instancias[cls]

class Conexion(metaclass=SingletonMeta):
    pass

c1 = Conexion()
c2 = Conexion()
print("Ejercicio 8 →", c1 is c2)  # True


# ======================================================
# EJERCICIO 9: Forzar docstring en clases
# Consigna: Haz una metaclase que obligue a todas las clases
#           a tener un __doc__ definido.
# ======================================================
class DocMeta(type):
    def __new__(mcs, nombre, bases, diccionario):
        if "__doc__" not in diccionario or diccionario["__doc__"] is None:
            raise TypeError(f"La clase {nombre} debe tener docstring")
        return super().__new__(mcs, nombre, bases, diccionario)

class Producto(metaclass=DocMeta):
    """Clase que representa un producto"""
    pass

print("Ejercicio 9 →", Producto.__doc__)


# ======================================================
# EJERCICIO 10: Auto-contador de clases creadas
# Consigna: Implementa una metaclase que cuente cuántas
#           clases han sido creadas con ella.
# ======================================================
class ContadorMeta(type):
    contador = 0
    def __new__(mcs, nombre, bases, diccionario):
        mcs.contador += 1
        return super().__new__(mcs, nombre, bases, diccionario)

class X(metaclass=ContadorMeta): pass
class Y(metaclass=ContadorMeta): pass
class Z(metaclass=ContadorMeta): pass

print("Ejercicio 10 →", ContadorMeta.contador)  # 3
