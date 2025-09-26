# ----------------------------------------
# PRÁCTICA - CLASE 1: INTRODUCCIÓN A PYTHON
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Tu primer saludo personalizado
# Consigna: Pedile al usuario su nombre y mostrá un saludo en pantalla.
nombre = "Franco"
print("Hola,", nombre + ". ¡Bienvenido al curso de Python!")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Mostrar tus datos
# Consigna: Creá variables con tu nombre, edad y ciudad, y mostralas con print().
mi_nombre = "Franco"
mi_edad = 22
mi_ciudad = "Buenos Aires"
print("Nombre:", mi_nombre)
print("Edad:", mi_edad)
print("Ciudad:", mi_ciudad)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Detectar tipos
# Consigna: Definí una variable de cada tipo (int, float, str, bool) y mostrá su tipo con type().
entero = 5
decimal = 3.14
texto = "Hola"
booleano = True
print(type(entero))    # <class 'int'>
print(type(decimal))   # <class 'float'>
print(type(texto))     # <class 'str'>
print(type(booleano))  # <class 'bool'>

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Corrigiendo errores
# Consigna: Corregí este código con errores y explicá por qué fallaba:
# saludo = Hola mundo
# print(saludo

# Corrección:
saludo = "Hola mundo"
print(saludo)
# El error era que faltaban las comillas para el string
# y el paréntesis de cierre en la función print()

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Cambiando variables
# Consigna: Creá una variable x con valor 10. Después cambiá su valor a 99 y mostralo antes y después del cambio.
x = 10
print("Valor inicial de x:", x)
x = 99
print("Nuevo valor de x:", x)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: El número favorito
# Consigna: Pedile al usuario que escriba su número favorito y mostralo con un mensaje amigable.
numero_favorito = "7"
print("Tu número favorito es:", numero_favorito)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Mezclando tipos
# Consigna: Creá tres variables: nombre (str), edad (int), y estudiando (bool). Mostralas todas juntas.
nombre = "Franco"
edad = 22
estudiando = True
print("Nombre:", nombre)
print("Edad:", edad)
print("¿Estás estudiando?:", estudiando)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Comentá tu código
# Consigna: Escribí un mini programa que muestre tres mensajes distintos y agregá comentarios explicando cada línea.

# Imprimimos un mensaje de bienvenida
print("Bienvenido a Python")

# Mostramos un número de ejemplo
print(123)

# Mostramos un valor booleano
print(True)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Frase armada
# Consigna: Guardá las palabras "Hola", "Python" y "Mundo" en variables y mostralas en una misma línea.
palabra1 = "Hola"
palabra2 = "Python"
palabra3 = "Mundo"
print(palabra1, palabra2, palabra3)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Mini encuesta
# Consigna: Pedile al usuario su nombre, edad y comida favorita. Mostrá un resumen con esos datos.
nombre_usuario = "Franco"
comida_favorita = "pizza"
edad_usuario = 22
print("Hola,", nombre_usuario + ". Tenés", edad_usuario, "años y tu comida favorita es la", comida_favorita + ".")

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
