# ----------------------------------------
# PRÁCTICA - CLASE 2: VARIABLES Y TIPOS DE DATOS
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Crear y mostrar variables
# Consigna: Declarar 4 variables con tu nombre, edad, altura y si estás activo, y mostrarlas.
nombre = "Franco"
edad = 22
altura = 1.78
activo = True

print(nombre)
print(edad)
print(altura)
print(activo)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Mostrar los tipos de datos
# Consigna: Usar type() para mostrar el tipo de cada variable del ejercicio anterior.
print(type(nombre))   # str
print(type(edad))     # int
print(type(altura))   # float
print(type(activo))   # bool

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Reasignar valores
# Consigna: Cambiar el valor de "edad" a 23 y luego a "veintitrés", mostrando su tipo cada vez.
edad = 23
print("Edad actualizada:", edad, "→", type(edad))

edad = "veintitrés"
print("Edad como texto:", edad, "→", type(edad))

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Crear variables con nombres válidos e inválidos (comentados)
# Consigna: Crear 3 variables válidas y 3 inválidas (estas últimas deben ir comentadas).
_mi_nombre = "Franco"
miEdad = 22
altura_en_metros = 1.78

# 2cosas = "no"       ← inválida: empieza con número
# mi-edad = 22        ← inválida: contiene guión
# class = "error"     ← inválida: palabra reservada

print(_mi_nombre, miEdad, altura_en_metros)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Conversión de tipos
# Consigna: Convertí el string "45" a entero y mostralo junto con su tipo.
numero = "45"
print(numero, type(numero))

numero = int(numero)
print(numero, type(numero))

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Más conversiones
# Consigna: Convertí "3.14" a float, 100 a string y 1 a booleano. Mostralos con su tipo.
decimal = float("3.14")
texto = str(100)
booleano = bool(1)

print(decimal, type(decimal))
print(texto, type(texto))
print(booleano, type(booleano))

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Concatenar strings correctamente
# Consigna: Uní el string "Tengo" con la edad 22 y el texto "años", usando str().
edad = 22
print("Tengo " + str(edad) + " años")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Usar f-strings
# Consigna: Mostrá en una sola línea tu nombre, edad y altura usando una f-string.
print(f"{nombre} tiene {edad} años y mide {altura}m")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Variables mal usadas (comentado)
# Consigna: Escribí 2 líneas con errores de tipos, explicá por qué fallan (comentado).
# print("Tengo " + edad + " años")   ← Error: no se puede concatenar str + int
# numero = int("texto")              ← Error: "texto" no se puede convertir a número

print("Este ejercicio contiene ejemplos de errores comentados.")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Mini biografía
# Consigna: Guardá tus datos en variables y mostralos en un texto con f-string.
nombre = "Franco Lugo"
edad = 22
altura = 1.78
ciudad = "Buenos Aires"
print(f"Hola, soy {nombre}, tengo {edad} años, mido {altura} metros y vivo en {ciudad}.")

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
