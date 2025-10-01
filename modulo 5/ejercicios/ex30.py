# ----------------------------------------
# CLASE 31: COMPRENSIÓN DE LISTAS, SETS Y DICTS AVANZADOS
# ----------------------------------------

# ===============================================
# 1) Generar una lista con los cuadrados del 1 al 10 usando list comprehension
# ===============================================
cuadrados = [i**2 for i in range(1, 11)]
print("Ejercicio 1:", cuadrados)


# ===============================================
# 2) Crear una lista con los números pares entre 0 y 20, y poner "impar" en los demás casos
# ===============================================
pares_impares = [i if i % 2 == 0 else "impar" for i in range(21)]
print("Ejercicio 2:", pares_impares)


# ===============================================
# 3) Aplanar una matriz 3x3 usando list comprehension
# ===============================================
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [num for fila in matriz for num in fila]
print("Ejercicio 3:", aplanada)


# ===============================================
# 4) Obtener todas las vocales únicas de un texto usando set comprehension
# ===============================================
texto = "Programación en Python es genial"
vocales = {c for c in texto.lower() if c in "aeiou"}
print("Ejercicio 4:", vocales)


# ===============================================
# 5) Crear un diccionario con los números del 1 al 5 y sus cubos como valores
# ===============================================
cubos = {i: i**3 for i in range(1, 6)}
print("Ejercicio 5:", cubos)


# ===============================================
# 6) Filtrar un diccionario para quedarnos solo con las personas mayores de 25 años
# ===============================================
personas = {"Ana": 22, "Luis": 30, "Pedro": 28, "Franco": 24}
mayores = {nombre: edad for nombre, edad in personas.items() if edad > 25}
print("Ejercicio 6:", mayores)


# ===============================================
# 7) Generar una lista de tuplas (número, cuadrado) para números del 1 al 10
# ===============================================
pares = [(i, i**2) for i in range(1, 11)]
print("Ejercicio 7:", pares)


# ===============================================
# 8) Crear un set con todas las letras únicas de un texto excluyendo espacios
# ===============================================
frase = "Hola mundo en Python"
letras = {c for c in frase if c != " "}
print("Ejercicio 8:", letras)


# ===============================================
# 9) Generar un diccionario de frecuencias de palabras de un texto
# ===============================================
texto2 = "python es divertido y python es poderoso porque python es simple"
palabras = texto2.lower().split()
frecuencias = {palabra: palabras.count(palabra) for palabra in set(palabras)}
print("Ejercicio 9:", frecuencias)


# ===============================================
# 10) Crear una matriz identidad 3x3 usando list comprehension
# ===============================================
identidad = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print("Ejercicio 10:", identidad)
