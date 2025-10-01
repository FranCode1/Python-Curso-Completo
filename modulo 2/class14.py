# ----------------------------------------
# CLASE 14: RECURSIVIDAD EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es la recursividad?

# Es una técnica en la que una función se llama a sí misma para resolver un problema.
# Cada llamada reduce el problema hasta llegar a un caso base.

# Estructura:
# def funcion():
#     if caso_base:
#         return resultado
#     else:
#         return funcion(modificacion_del_problema)


# ==========================
# 🔹 EJEMPLO 1: CONTAR REGRESIVAMENTE
# ==========================

def cuenta_regresiva(n):
    if n <= 0:
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n - 1)

cuenta_regresiva(5)


# ==========================
# 🔹 EJEMPLO 2: FACTORIAL
# ==========================

# Factorial de n = n * (n-1) * (n-2) * ... * 1
# 5! = 5*4*3*2*1 = 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("5! =", factorial(5))  # 120


# ==========================
# 🔹 EJEMPLO 3: SUMA DE UNA LISTA
# ==========================

def sumar_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumar_lista(lista[1:])

print(sumar_lista([1, 2, 3, 4]))  # 10


# ==========================
# ⚠️ PRECAUCIÓN: CASOS BASE
# ==========================

# Si no hay caso base, la función se llama infinitamente y da error:
# RecursionError: maximum recursion depth exceeded

# Siempre asegurate de:
# - Tener un caso base
# - Acercarte al caso base en cada llamada


# ==========================
# 🧠 BONUS: FIBONACCI
# ==========================

# Serie de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ...
# f(n) = f(n-1) + f(n-2), con f(0)=0 y f(1)=1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(6):", fibonacci(6))  # 8


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# Crear una función recursiva para invertir un string

# def invertir_texto(texto):
#     if len(texto) == 0:
#         return ""
#     else:
#         return texto[-1] + invertir_texto(texto[:-1])

# print(invertir_texto("python"))  # nohtyp


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es la recursividad y cómo usarla
# - Cómo definir casos base y evitar errores
# - Ejemplos comunes: factorial, suma, Fibonacci
# - Cómo usar la recursión para resolver problemas prácticos

# Próxima clase: Módulos y organización de código – importaciones, archivos, reutilización.
