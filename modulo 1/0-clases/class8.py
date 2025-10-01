# ----------------------------------------
# CLASE 8: TUPLAS Y SETS EN PYTHON
# ----------------------------------------

# ==========================
# 📌 TUPLAS
# ==========================

# Una tupla es como una lista, pero inmutable: no se puede modificar.
# Se usa cuando queremos proteger los datos o asegurar que no cambien.

# Sintaxis: paréntesis () o sin nada

coordenadas = (4, 5)
colores = "rojo", "verde", "azul"  # también válido

print(coordenadas)
print(type(coordenadas))  # <class 'tuple'>


# ✅ Acceso a elementos (igual que listas)
print(colores[0])
print(colores[-1])

# ❌ No se puede modificar
# coordenadas[0] = 10 → Error: 'tuple' object does not support item assignment

# ✅ Tuplas pueden contener cualquier tipo de dato
mi_tupla = ("texto", 100, True, 3.14)

# ✅ Desempaquetado
x, y = coordenadas
print("x:", x)
print("y:", y)


# ==========================
# 📌 SETS
# ==========================

# Un set es una colección no ordenada, sin elementos repetidos.
# Se usa cuando no nos importa el orden, y queremos elementos únicos.

# Sintaxis: llaves {} o set()

numeros = {1, 2, 3, 4, 5}
print(numeros)
print(type(numeros))  # <class 'set'>

# ❗ Los sets eliminan duplicados automáticamente
repetidos = {1, 2, 2, 3, 4, 4, 5}
print("Sin duplicados:", repetidos)  # {1, 2, 3, 4, 5}

# ✅ Agregar elementos
numeros.add(6)
print("Agregado 6:", numeros)

# ❌ No hay índices (no se puede hacer numeros[0])

# ✅ Eliminar elementos
numeros.remove(3)  # si no existe, da error
print("Después de remove(3):", numeros)

numeros.discard(10)  # si no existe, no da error

# ✅ Verificar pertenencia
print(2 in numeros)   # True
print(9 not in numeros)  # True


# ✅ Operaciones entre sets
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}
mezcla = {3, 4, 5, 6}

print("Unión:", pares | impares)           # union
print("Intersección:", mezcla & pares)     # elementos comunes
print("Diferencia:", mezcla - pares)       # solo en mezcla
print("Simétrica:", mezcla ^ pares)        # no comunes


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# Programa para ingresar una serie de colores únicos y mostrarlos ordenados

# colores = set()

# while True:
#     color = input("Agregá un color (o escribí 'fin'): ").lower()
#     if color == "fin":
#         break
#     colores.add(color)

# print("Colores únicos que ingresaste:", sorted(colores))


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es una tupla y cómo se usa (inmutable, ordenada)
# - Qué es un set y cómo se usa (no ordenado, sin duplicados)
# - Métodos útiles: add, remove, discard, in
# - Operaciones entre sets: unión, intersección, diferencia

# Próxima clase: Diccionarios – trabajar con claves y valores.
