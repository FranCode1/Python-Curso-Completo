# ----------------------------------------
# CLASE 1: INTRODUCCIÓN A PYTHON
# ----------------------------------------

# 📌 ¿Qué es Python?
# Python es un lenguaje de programación interpretado, de alto nivel, 
# de propósito general y muy fácil de leer. Fue creado por Guido van Rossum
# y su primera versión fue lanzada en 1991.

# ✅ Usos comunes de Python:
# - Desarrollo web (con frameworks como Django, Flask)
# - Ciencia de datos y machine learning
# - Automatización de tareas
# - Scripts para administrar sistemas
# - Videojuegos (con pygame)
# - Aplicaciones de escritorio

# 🔍 ¿Por qué aprender Python?
# - Sintaxis simple y clara
# - Comunidad enorme
# - Muchas librerías disponibles
# - Versátil y potente


# -------------------------------
# PRIMER CONTACTO CON PYTHON
# -------------------------------

# Vamos a imprimir un mensaje en pantalla usando la función print()

print("Hola, mundo!")  # Este es el clásico primer programa

# 📝 Comentarios:
# Todo lo que está después del símbolo # es un comentario y no se ejecuta
# Se usa para explicar el código o dejar anotaciones


# -------------------------------
# TIPOS DE DATOS BÁSICOS
# -------------------------------

# 🔢 Números
print(5)          # Entero
print(3.14)       # Decimal (float)

# 🔤 Texto (Strings)
print("Esto es un string")

# 🧠 Booleanos
print(True)       # Verdadero
print(False)      # Falso

# 📦 Python detecta automáticamente el tipo de dato


# -------------------------------
# VARIABLES
# -------------------------------

# Una variable guarda un valor que podés usar más adelante
mensaje = "Bienvenidos al curso de Python"
numero = 42
pi = 3.14159
activo = True

print(mensaje)
print(numero)
print(pi)
print(activo)

# Podés reasignar una variable:
numero = 100
print("Nuevo valor de número:", numero)


# -------------------------------
# FUNCIONES BÁSICAS
# -------------------------------

# type() nos dice el tipo de dato
print(type(mensaje))   # <class 'str'>
print(type(numero))    # <class 'int'>
print(type(pi))        # <class 'float'>
print(type(activo))    # <class 'bool'>


# -------------------------------
# ERRORES COMUNES DE PRINCIPIANTES
# -------------------------------

# ❌ Olvidar las comillas
# print(Hola mundo)   ← Esto da error, debería ser print("Hola mundo")

# ❌ Dejar espacios de más
#   print("Hola")     ← Esto también da error por identación (no en este caso, pero en funciones sí)


# -------------------------------
# INPUT (Entrada del usuario)
# -------------------------------

# input() sirve para pedir algo al usuario
# nombre = input("¿Cómo te llamás? ")
# print("Hola,", nombre)

# 🧪 Podés probar esto descomentando las líneas anteriores y ejecutando el código


# -------------------------------
# CONCLUSIÓN DE LA CLASE
# -------------------------------

# En esta clase vimos:
# - Qué es Python y por qué aprenderlo
# - Cómo imprimir texto en pantalla
# - Tipos de datos básicos: int, float, str, bool
# - Cómo crear y usar variables
# - Uso básico de la función input()
# - Comentarios y errores comunes

# En la próxima clase veremos más sobre tipos de datos y operaciones con ellos.
