# ----------------------------------------
# CLASE 30: METAPROGRAMACIÓN EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es la metaprogramación?
# - Es la capacidad de un programa de tratar su propio código como datos.
# - En Python se hace mediante introspección, reflexión y funciones especiales como getattr, setattr, hasattr, etc.

# ==========================
# 🔹 getattr(), hasattr(), setattr(), delattr()
# ==========================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Franco", 22)

# getattr → obtener un atributo por nombre (string)
print(getattr(p, "nombre"))  # Franco

# hasattr → verificar si un objeto tiene un atributo
print(hasattr(p, "edad"))  # True
print(hasattr(p, "altura"))  # False

# setattr → asignar un valor a un atributo dinámicamente
setattr(p, "altura", 1.80)
print(p.altura)  # 1.8

# delattr → eliminar un atributo
delattr(p, "edad")
print(hasattr(p, "edad"))  # False


# ==========================
# 🔹 INTROSPECCIÓN EN PYTHON
# ==========================

# Introspección = examinar objetos en tiempo de ejecución

print(type(p))              # <class '__main__.Persona'>
print(isinstance(p, Persona)) # True
print(dir(p))               # Lista de atributos y métodos del objeto
print(p.__dict__)           # Diccionario con los atributos de instancia


# ==========================
# 🔹 REFLEXIÓN
# ==========================

# Reflexión = modificar el comportamiento del programa en tiempo de ejecución

# Ejemplo: crear clases dinámicamente con type()
Animal = type("Animal", (), {"es_vivo": True})
a = Animal()
print(a.es_vivo)  # True

# Ejemplo: invocar métodos dinámicamente
class Calculadora:
    def sumar(self, x, y): return x + y
    def restar(self, x, y): return x - y

calc = Calculadora()

operacion = "sumar"
resultado = getattr(calc, operacion)(5, 3)  # llama a calc.sumar(5,3)
print(resultado)  # 8


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================
# 🎯 Crear una función genérica que convierta cualquier objeto en diccionario,
# incluyendo atributos dinámicos.

def objeto_a_diccionario(obj):
    atributos = {}
    for attr in dir(obj):
        if not attr.startswith("__"):  # ignorar internos
            valor = getattr(obj, attr)
            if not callable(valor):   # ignorar métodos
                atributos[attr] = valor
    return atributos

print(objeto_a_diccionario(p))
# {'altura': 1.8, 'nombre': 'Franco'}


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es la metaprogramación
# - Usar getattr, hasattr, setattr, delattr
# - Introspección: type, isinstance, dir, __dict__
# - Reflexión: modificar clases/objetos en tiempo de ejecución
# - Cómo crear clases y métodos dinámicamente

# Próxima clase: Manejo avanzado de colecciones en Python (collections, itertools, functools)
