# ----------------------------------------
# CLASE 35: FUNCIONES PURAS Y PROGRAMACIÓN FUNCIONAL
# ----------------------------------------

from functools import reduce, partial, lru_cache

# ============================================================
# EJERCICIO 1: Crear una función pura
# ============================================================
# Consigna:
# Crea una función pura que reciba una lista de números y devuelva
# una nueva lista con cada número al cuadrado.

def cuadrados(lista):
    return [x**2 for x in lista]  # no modifica nada fuera de su alcance

numeros = [1, 2, 3, 4]
print("✅ Ejercicio 1:", cuadrados(numeros))  # [1, 4, 9, 16]


# ============================================================
# EJERCICIO 2: Inmutabilidad
# ============================================================
# Consigna:
# A partir de una tupla, crea una nueva con elementos agregados sin modificar la original.

original = (10, 20, 30)
nueva = original + (40,)
print("✅ Ejercicio 2:", original, nueva)  # (10,20,30) (10,20,30,40)


# ============================================================
# EJERCICIO 3: Función de orden superior
# ============================================================
# Consigna:
# Crea una función que reciba otra función y una lista, y devuelva una nueva lista
# con la función aplicada a cada elemento.

def aplicar(func, lista):
    return [func(x) for x in lista]

print("✅ Ejercicio 3:", aplicar(lambda x: x + 5, [1, 2, 3]))  # [6, 7, 8]


# ============================================================
# EJERCICIO 4: Uso de map, filter y reduce juntos
# ============================================================
# Consigna:
# A partir de una lista, multiplica todos los pares por 2 y suma el resultado.

lista = [1, 2, 3, 4, 5, 6]
resultado = reduce(lambda a, b: a + b, map(lambda x: x * 2, filter(lambda n: n % 2 == 0, lista)))
print("✅ Ejercicio 4:", resultado)  # (2*2 + 4*2 + 6*2) = 24


# ============================================================
# EJERCICIO 5: Usar functools.partial
# ============================================================
# Consigna:
# Usa partial para crear una nueva función `potencia_3` que eleve un número al cubo.

def potencia(base, exp):
    return base ** exp

potencia_3 = partial(potencia, exp=3)
print("✅ Ejercicio 5:", potencia_3(5))  # 125


# ============================================================
# EJERCICIO 6: Memoización con lru_cache
# ============================================================
# Consigna:
# Crea una función recursiva para calcular Fibonacci con lru_cache para mejorar rendimiento.

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("✅ Ejercicio 6:", fibonacci(30))  # 832040


# ============================================================
# EJERCICIO 7: Crear una función pura factorial con reduce
# ============================================================
# Consigna:
# Implementa factorial usando reduce de manera funcional.

def factorial(n):
    return reduce(lambda a, b: a * b, range(1, n + 1), 1)

print("✅ Ejercicio 7:", factorial(6))  # 720


# ============================================================
# EJERCICIO 8: Filtrar datos con funciones puras
# ============================================================
# Consigna:
# Dada una lista de diccionarios con personas, filtra solo las mayores de edad.

personas = [
    {"nombre": "Ana", "edad": 17},
    {"nombre": "Luis", "edad": 22},
    {"nombre": "Sofía", "edad": 30},
]

mayores = list(filter(lambda p: p["edad"] >= 18, personas))
print("✅ Ejercicio 8:", mayores)  
# [{'nombre': 'Luis', 'edad': 22}, {'nombre': 'Sofía', 'edad': 30}]


# ============================================================
# EJERCICIO 9: Transformar datos con map
# ============================================================
# Consigna:
# Dada una lista de nombres, devuelve una nueva lista con todos en mayúsculas.

nombres = ["franco", "sofia", "juan"]
mayus = list(map(str.upper, nombres))
print("✅ Ejercicio 9:", mayus)  # ['FRANCO', 'SOFIA', 'JUAN']


# ============================================================
# EJERCICIO 10: Composición funcional de operaciones
# ============================================================
# Consigna:
# Crea un pipeline funcional: 
# 1️⃣ filtrar números > 10 
# 2️⃣ multiplicarlos por 3 
# 3️⃣ sumar el total.

datos = [5, 12, 7, 20, 3, 15]

resultado_pipeline = reduce(
    lambda a, b: a + b,
    map(lambda x: x * 3, filter(lambda x: x > 10, datos))
)
print("✅ Ejercicio 10:", resultado_pipeline)  
# (12*3 + 20*3 + 15*3) = 141
