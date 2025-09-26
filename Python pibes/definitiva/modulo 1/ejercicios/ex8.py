# ----------------------------------------
# PRÁCTICA - CLASE 8: TUPLAS Y SETS EN PYTHON
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Crear una tupla
# Consigna: Crear una tupla con los días de la semana y mostrarla.
dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
print("Días de la semana:", dias)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Acceder a elementos de una tupla
# Consigna: Mostrar el primer y último día.
print("Primer día:", dias[0])
print("Último día:", dias[-1])

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Desempaquetar tupla
# Consigna: Desempaquetar una tupla con coordenadas y mostrar x e y.
coordenadas = (10, 20)
x, y = coordenadas
print("x:", x)
print("y:", y)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Crear una tupla con datos variados
# Consigna: Crear una tupla con un nombre, edad y si está activo.
usuario = ("Franco", 22, True)
print("Usuario:", usuario)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Crear un set sin duplicados
# Consigna: Crear un set con números del 1 al 5 con duplicados y mostrarlo.
numeros = {1, 2, 2, 3, 4, 4, 5}
print("Números únicos:", numeros)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Agregar y eliminar elementos en un set
# Consigna: Agregar 6 al set y eliminar el 3.
numeros.add(6)
print("Agregado 6:", numeros)
numeros.remove(3)
print("Eliminado 3:", numeros)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Verificar pertenencia en un set
# Consigna: Verificar si el número 4 está y si el 10 no está en el set.
print("¿Está el 4?", 4 in numeros)
print("¿No está el 10?", 10 not in numeros)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Unión de sets
# Consigna: Unir dos sets y mostrar el resultado.
pares = {2, 4, 6}
impares = {1, 3, 5}
todos = pares | impares
print("Unión:", todos)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Intersección y diferencia
# Consigna: Mostrar la intersección y la diferencia entre dos sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Intersección:", set1 & set2)
print("Diferencia:", set1 - set2)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Mini proyecto - colores únicos
# Consigna: Simular ingresar colores a un set y mostrarlos ordenados.
entradas = ["rojo", "azul", "verde", "rojo", "amarillo", "azul"]
colores = set()

for color in entradas:
    colores.add(color)

print("Colores únicos ordenados:", sorted(colores))

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
