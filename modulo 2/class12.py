# ----------------------------------------
# CLASE 12: FUNCIONES AVANZADAS EN PYTHON
# ----------------------------------------

# En esta clase veremos:
# - Funciones lambda (funciones anónimas)
# - map() → aplicar una función a cada elemento
# - filter() → filtrar elementos según una condición
# - zip() → combinar listas
# - enumerate() → obtener índice y valor en un bucle


# ==========================
# 🔹 FUNCIÓN LAMBDA
# ==========================

# Una función lambda es una función anónima, de una sola línea

# Sintaxis: lambda argumentos : expresión

suma = lambda x, y: x + y
print(suma(3, 5))  # 8

# Equivalente a:
# def suma(x, y):
#     return x + y

cuadrado = lambda n: n ** 2
print(cuadrado(4))  # 16


# ==========================
# 🔹 map()
# ==========================

# map(función, iterable) → aplica una función a cada elemento del iterable

numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)  # [1, 4, 9, 16]

# También con funciones normales:
def triple(n):
    return n * 3

triples = list(map(triple, numeros))
print("Triples:", triples)


# ==========================
# 🔹 filter()
# ==========================

# filter(función_condición, iterable) → filtra elementos que cumplan la condición

pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)  # [2, 4]


# ==========================
# 🔹 zip()
# ==========================

# zip() une varios iterables en tuplas (elemento a elemento)

nombres = ["Ana", "Luis", "Marta"]
edades = [22, 30, 25]

combinado = list(zip(nombres, edades))
print("Zip:", combinado)  # [('Ana', 22), ('Luis', 30), ('Marta', 25)]


# ==========================
# 🔹 enumerate()
# ==========================

# enumerate() devuelve el índice y el valor al recorrer una lista

frutas = ["manzana", "banana", "kiwi"]

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# A partir de una lista de números:
# - Filtrar los impares
# - Obtener el cuadrado de cada impar
# - Mostrar la lista final con su índice

# numeros = [1, 2, 3, 4, 5, 6, 7]

# impares = list(filter(lambda x: x % 2 != 0, numeros))
# cuadrados = list(map(lambda x: x**2, impares))

# for i, valor in enumerate(cuadrados):
#     print(f"{i}: {valor}")

# Resultado esperado: índice y el cuadrado de los impares


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Funciones lambda para código conciso
# - map() para aplicar funciones a listas
# - filter() para filtrar elementos
# - zip() para combinar múltiples listas
# - enumerate() para trabajar con índices en bucles

# Próxima clase: Programación funcional (conceptos y herramientas como reduce, funciones puras, etc.)
