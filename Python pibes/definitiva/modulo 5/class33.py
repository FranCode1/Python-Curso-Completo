# ----------------------------------------
# CLASE 34: DECORADORES AVANZADOS
# ----------------------------------------

# 📌 Recordatorio:
# - Un decorador es una función que recibe otra función y devuelve una nueva función.
# - Se usa con el operador "@".
# - Permite añadir funcionalidad sin modificar el código original.

# ==========================
# 🔹 DECORADOR BÁSICO
# ==========================

def mi_decorador(func):
    def wrapper(*args, **kwargs):
        print("➡ Antes de ejecutar la función")
        resultado = func(*args, **kwargs)
        print("⬅ Después de ejecutar la función")
        return resultado
    return wrapper

@mi_decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Franco")


# ==========================
# 🔹 DECORADORES ANIDADOS
# ==========================

def mayusculas(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado.upper()
    return wrapper

def exclamacion(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado + "!!!"
    return wrapper

@exclamacion
@mayusculas
def mensaje():
    return "python decorators"

print(mensaje())  # PYTHON DECORATORS!!!


# ==========================
# 🔹 DECORADORES CON ARGUMENTOS
# ==========================

def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def hola():
    print("Hola!")

hola()


# ==========================
# 🔹 FUNCTOOLS.WRAP
# ==========================

# Problema: los decoradores cambian el __name__ y __doc__ de la función.
# Solución: usar functools.wraps

from functools import wraps

def decorador_con_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Ejecutando función decorada...")
        return func(*args, **kwargs)
    return wrapper

@decorador_con_wraps
def sumar(a, b):
    """Suma dos números"""
    return a + b

print(sumar(2, 3))
print(sumar.__name__)  # sumar
print(sumar.__doc__)   # Suma dos números


# ==========================
# 🔹 DECORANDO MÉTODOS DE CLASE
# ==========================

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con {args[1:]} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

class Calculadora:
    @log
    def multiplicar(self, a, b):
        return a * b

calc = Calculadora()
print(calc.multiplicar(4, 5))


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Crear un decorador que mida el tiempo de ejecución de una función
import time

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱️ {func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def calcular():
    return sum([i**2 for i in range(1_000_000)])

print(calcular())


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Decoradores anidados y con argumentos
# - Uso de functools.wraps para preservar metadata
# - Decoradores en métodos de clases
# - Mini proyecto: decorador para medir tiempo de ejecución

# Próxima clase: Programación funcional en Python (map, filter, reduce, itertools, functools)
