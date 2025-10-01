# ----------------------------------------
# CLASE 35: FUNCIONES PURAS Y PROGRAMACIÓN FUNCIONAL EN PYTHON
# ----------------------------------------

# 📌 Recordatorio:
# - Una función pura siempre devuelve el mismo resultado con los mismos argumentos
#   y no produce efectos secundarios.
# - La programación funcional favorece inmutabilidad y el uso de funciones de orden superior.
# - Python tiene el módulo functools para apoyar este paradigma.

# ==========================
# 🔹 FUNCIONES PURAS
# ==========================

def suma(a, b):
    return a + b

print(suma(2, 3))  # 5
print(suma(2, 3))  # 5 (siempre el mismo resultado)


# Contraejemplo: función impura
x = 10
def sumar_y_modificar(y):
    global x
    x += y
    return x

print(sumar_y_modificar(5))  # 15
print(sumar_y_modificar(5))  # 20 (resultado cambia con mismos argumentos)


# ==========================
# 🔹 INMUTABILIDAD
# ==========================

nums = (1, 2, 3)
nueva = nums + (4,)  # se crea una nueva tupla
print(nums)   # (1, 2, 3)
print(nueva)  # (1, 2, 3, 4)


# ==========================
# 🔹 FUNCIONES DE ORDEN SUPERIOR
# ==========================

def aplicar_funcion(func, lista):
    return [func(x) for x in lista]

print(aplicar_funcion(lambda x: x**2, [1, 2, 3]))
# [1, 4, 9]


# ==========================
# 🔹 FUNCTOOLS: REDUCE
# ==========================

from functools import reduce

nums = [1, 2, 3, 4]
resultado = reduce(lambda a, b: a + b, nums)
print(resultado)  # 10


# ==========================
# 🔹 FUNCTOOLS: PARTIAL
# ==========================

from functools import partial

def potencia(base, exp):
    return base ** exp

cuadrado = partial(potencia, exp=2)
print(cuadrado(5))  # 25


# ==========================
# 🔹 FUNCTOOLS: LRU_CACHE
# ==========================

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(35))  # mucho más rápido gracias al cache


# ==========================
# 🔹 COMBINANDO MAP, FILTER, REDUCE
# ==========================

numeros = [1, 2, 3, 4, 5, 6]

# Doblar todos (map)
dobles = list(map(lambda x: x*2, numeros))
print(dobles)  # [2, 4, 6, 8, 10, 12]

# Filtrar pares (filter)
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

# Sumar todo (reduce)
suma_total = reduce(lambda a, b: a + b, numeros)
print(suma_total)  # 21


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Crear una función pura que calcule factorial de forma funcional
from functools import reduce

def factorial(n):
    return reduce(lambda a, b: a*b, range(1, n+1), 1)

print(factorial(5))  # 120


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué son funciones puras y por qué son importantes
# - Inmutabilidad y creación de nuevos objetos
# - Funciones de orden superior
# - Uso de functools: reduce, partial, lru_cache
# - Combinación de map, filter, reduce
# - Mini proyecto: factorial funcional
#
# Próxima clase: Concurrencia y paralelismo en Python (threading, multiprocessing, async)
