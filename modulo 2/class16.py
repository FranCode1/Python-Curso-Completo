# ----------------------------------------
# CLASE 16: DECORADORES EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es un decorador?

# Es una función que recibe otra función como argumento y devuelve una nueva función.
# Se usa para "envolver" otra función y modificar su comportamiento.

# Se basa en:
# - Funciones como objetos
# - Closures

# Sintaxis básica:
# @decorador
# def mi_funcion():
#     ...

# Es equivalente a: mi_funcion = decorador(mi_funcion)


# ==========================
# 🔹 EJEMPLO BÁSICO
# ==========================

def decorador(func):
    def nueva_funcion():
        print("Antes de ejecutar la función...")
        func()
        print("Después de ejecutar la función...")
    return nueva_funcion

@decorador
def saludar():
    print("Hola, esto es una función normal.")

saludar()

# Salida:
# Antes de ejecutar la función...
# Hola, esto es una función normal.
# Después de ejecutar la función...


# ==========================
# 🔹 DECORADORES CON PARÁMETROS
# ==========================

def decorador_con_parametros(func):
    def wrapper(nombre):
        print("Validando nombre...")
        func(nombre)
        print("Fin de ejecución.")
    return wrapper

@decorador_con_parametros
def saludar(nombre):
    print(f"Hola {nombre}!")

saludar("Franco")


# ==========================
# 🔹 MANTENER LA INFORMACIÓN ORIGINAL
# ==========================

# Para conservar el nombre y la docstring de la función decorada:
from functools import wraps

def decorador_pro(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@decorador_pro
def sumar(a, b):
    """Suma dos números"""
    return a + b

print(sumar(3, 4))  # 7
print(sumar.__doc__)  # Suma dos números


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# Crear un decorador que mida el tiempo de ejecución de una función

# import time

# def medir_tiempo(func):
#     def wrapper(*args, **kwargs):
#         inicio = time.time()
#         resultado = func(*args, **kwargs)
#         fin = time.time()
#         print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
#         return resultado
#     return wrapper

# @medir_tiempo
# def tarea_lenta():
#     for _ in range(10000000):
#         pass

# tarea_lenta()


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es un decorador y cómo funciona
# - Cómo escribir decoradores simples y con argumentos
# - Cómo usar `@wraps` para mantener metadatos de funciones
# - Cómo aplicarlo para validación, logging, tiempo de ejecución, etc.

# Próxima clase: Módulos y paquetes – organización profesional de proyectos.
