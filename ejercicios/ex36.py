# =====================================================================
# EJERCICIO 36: Funciones para Calcular el Factorial
# ---------------------------------------------------------------------
# El factorial de un número (n) se define como:
# n! = n × (n-1) × (n-2) × ... × 1
# Ejemplo: 3! = 3 × 2 × 1 = 6
# =====================================================================


# ---------- Forma 1: usando for ----------
def factorial_for(nro):
    resultado = 1
    for i in range(1, nro + 1):
        resultado *= i
    return resultado

print("Factorial usando for:", factorial_for(3))  # Salida esperada: 6

# ---------- Forma 2: usando while ----------
def factorial_while(nro):
    resultado = 1
    while nro > 1:
        resultado *= nro
        nro -= 1
    return resultado

print("Factorial usando while:", factorial_while(3))  # Salida esperada: 6

# ---------- Forma 3: recursivo ----------
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

print("Factorial recursivo:", factorial_recursivo(3))  # Salida esperada: 6

# ---------- Forma 4: usando math.prod ----------
from math import prod
def factorial_prod(n):
    return prod(range(1, n + 1))

print("Factorial usando math.prod:", factorial_prod(3))  # Salida esperada: 6

# ---------- Forma 5: usando functools.reduce ----------
from functools import reduce
def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

print("Factorial usando reduce:", factorial_reduce(3))  # Salida esperada: 6





# ❌ VERSIÓN CON ERRORES (MALA IMPLEMENTACIÓN)
# Esta función siempre devuelve el mismo número porque multiplica nro * 1 en cada iteración
# La lógica es incorrecta
def factorial_mal_1(nro):
    resultado = 1
    for i in range(1, nro + 1):
        resultado = nro * 1  # Incorrecto: no está usando el bucle correctamente
    return resultado

print("Versión incorrecta 1:", factorial_mal_1(3))  # Devuelve 3


# ❌ OTRA VERSIÓN CON ERRORES
# Intenta una lógica innecesariamente complicada y da un resultado incorrecto
def factorial_mal_2(num):
    resultado = 1
    for i in range(num):
        resultado += i * (i - 1)  # Esto no es una multiplicación encadenada como el factorial
    return resultado

print("Versión incorrecta 2:", factorial_mal_2(3))  # Devuelve 3


# ❌ VERSIÓN SUMANDO EN VEZ DE MULTIPLICAR
# Esto suma los valores del número hacia 1, pero eso no es un factorial.
def factorial_mal_3(num):
    result = 1
    for i in range(num, 0, -1):
        result += i  # Esto suma en lugar de multiplicar
    return result

print("Versión incorrecta 3:", factorial_mal_3(3))  # Devuelve 7


# -----------------------------------------
# CONCLUSIÓN:
# Las formas correctas de calcular un factorial son:
# - Usar un bucle for o while con multiplicación acumulativa
# - Usar recursividad
# -----------------------------------------
