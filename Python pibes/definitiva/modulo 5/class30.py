# ----------------------------------------
# CLASE 31: COMPRENSIÓN DE LISTAS, SETS Y DICTS AVANZADOS
# ----------------------------------------

# 📌 ¿Qué son las comprensiones en Python?
# - Son una forma concisa y poderosa de crear colecciones (listas, sets, diccionarios).
# - Usan una sintaxis compacta en lugar de bucles tradicionales.

# ==========================
# 🔹 LIST COMPREHENSIONS
# ==========================

# Forma tradicional
numeros = []
for i in range(10):
    numeros.append(i * 2)
print(numeros)

# Forma con list comprehension
numeros = [i * 2 for i in range(10)]
print(numeros)

# Con condición
pares = [i for i in range(20) if i % 2 == 0]
print(pares)

# Con if/else dentro de la expresión
clasificacion = ["par" if i % 2 == 0 else "impar" for i in range(10)]
print(clasificacion)


# ==========================
# 🔹 SET COMPREHENSIONS
# ==========================

# Eliminan duplicados automáticamente
texto = "programacion en python"
letras_unicas = {c for c in texto if c.isalpha()}
print(letras_unicas)  # {'p', 't', 'm', 'r', 'y', 'o', 'e', 'a', 'g', 'i', 'c', 'n'}


# ==========================
# 🔹 DICT COMPREHENSIONS
# ==========================

# Crear un diccionario a partir de listas
nombres = ["Franco", "Ana", "Luis"]
edades = [22, 25, 30]
personas = {n: e for n, e in zip(nombres, edades)}
print(personas)  # {'Franco': 22, 'Ana': 25, 'Luis': 30}

# Filtrar con condiciones
personas_mayores = {n: e for n, e in personas.items() if e > 23}
print(personas_mayores)  # {'Ana': 25, 'Luis': 30}


# ==========================
# 🔹 ANIDADAS Y COMPLEJAS
# ==========================

# Matriz 3x3
matriz = [[j for j in range(3)] for i in range(3)]
print(matriz)

# Aplanar una matriz
aplanada = [num for fila in matriz for num in fila]
print(aplanada)  # [0, 1, 2, 0, 1, 2, 0, 1, 2]


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Crear un analizador de texto:
# - Obtener todas las palabras
# - Contar la frecuencia de cada palabra
# - Guardar solo palabras con más de 3 letras

texto = "Python es poderoso y Python es divertido porque Python es simple"

palabras = texto.lower().split()
frecuencia = {palabra: palabras.count(palabra) for palabra in set(palabras) if len(palabra) > 3}

print(frecuencia)
# {'simple': 1, 'poderoso': 1, 'divertido': 1, 'porque': 1, 'python': 3}


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - List comprehensions con condiciones y expresiones if/else
# - Set comprehensions para eliminar duplicados
# - Dict comprehensions con zip() y filtrado
# - Uso de comprensiones anidadas
# - Mini proyecto de análisis de texto con dict comprehensions

# Próxima clase: Manejo avanzado de colecciones en Python (collections, itertools, functools)
