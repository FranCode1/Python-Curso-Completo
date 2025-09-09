# ----------------------------------------
# PRÁCTICA - CLASE 12: FUNCIONES AVANZADAS EN PYTHON
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Usar lambda para restar dos números
# Consigna: Crear una función lambda que reste dos números y mostrar el resultado.

restar = lambda a, b: a - b
print("5 - 2 =", restar(5, 2))

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Usar map para obtener el doble de cada número
# Consigna: Usar map() y lambda para duplicar todos los elementos de una lista.

numeros = [1, 3, 5, 7]
dobles = list(map(lambda x: x * 2, numeros))
print("Dobles:", dobles)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Usar filter para obtener mayores a 10
# Consigna: Usar filter() y lambda para filtrar una lista y dejar solo los mayores a 10.

valores = [4, 11, 9, 15, 3, 20]
mayores = list(filter(lambda x: x > 10, valores))
print("Mayores a 10:", mayores)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Usar zip para juntar productos y precios
# Consigna: Combinar dos listas (productos y precios) en una lista de tuplas.

productos = ["pan", "leche", "huevos"]
precios = [100, 250, 300]

catalogo = list(zip(productos, precios))
print("Catálogo:", catalogo)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Usar enumerate para mostrar elementos con índice
# Consigna: Recorrer una lista de ciudades con su número de orden.

ciudades = ["Buenos Aires", "Córdoba", "Rosario"]

for i, ciudad in enumerate(ciudades):
    print(f"{i+1}. {ciudad}")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Calcular la raíz cuadrada con lambda
# Consigna: Crear una función lambda que calcule la raíz cuadrada de un número.

import math
raiz = lambda x: math.sqrt(x)
print("Raíz de 49:", raiz(49))

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Filtrar palabras cortas
# Consigna: Filtrar una lista y dejar solo palabras de 4 letras o menos.

palabras = ["sol", "luna", "estrella", "mar", "cielo"]
cortas = list(filter(lambda x: len(x) <= 4, palabras))
print("Palabras cortas:", cortas)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Usar map con funciones normales
# Consigna: Crear una función que convierta temperaturas de °C a °F y usar map para aplicarla a una lista.

def c_a_f(c):
    return round((c * 9/5) + 32, 1)

temperaturas = [0, 20, 30, 100]
fahrenheit = list(map(c_a_f, temperaturas))
print("Temperaturas en °F:", fahrenheit)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Sumar listas elemento a elemento
# Consigna: Usar zip() para sumar dos listas de números posición por posición.

a = [1, 2, 3]
b = [4, 5, 6]
suma = [x + y for x, y in zip(a, b)]
print("Suma elemento a elemento:", suma)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Proyecto combinado
# Consigna: A partir de una lista de números, obtener los números pares, elevarlos al cubo y mostrar con su índice.

numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
cubos = list(map(lambda x: x**3, pares))

for i, valor in enumerate(cubos):
    print(f"Índice {i}: {valor}")

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
