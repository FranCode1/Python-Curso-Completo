# ----------------------------------------
# CLASE 18: MÓDULOS Y PAQUETES EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es un módulo?

# Un módulo es un archivo `.py` con funciones, clases o variables que podemos importar y reutilizar.

# 📦 ¿Qué es un paquete?

# Un paquete es una carpeta que contiene módulos y un archivo especial __init__.py
# Sirve para agrupar funcionalmente varios módulos.

# ==========================
# 🔹 EJEMPLO DE MÓDULO
# ==========================

# Supongamos que tenemos un archivo llamado `matematica.py` con este contenido:

# --- matematica.py ---
# def sumar(a, b):
#     return a + b
# def restar(a, b):
#     return a - b

# Lo importamos desde otro archivo así:

# import matematica
# print(matematica.sumar(2, 3))  # 5

# O podemos importar funciones específicas:

# from matematica import sumar
# print(sumar(10, 5))  # 15


# ==========================
# 🔹 CREANDO UN PAQUETE
# ==========================

# Estructura de ejemplo:

# └── mi_proyecto/
#     ├── __init__.py
#     ├── operaciones/
#     │   ├── __init__.py
#     │   ├── suma.py
#     │   └── resta.py
#     └── main.py

# --- suma.py ---
# def sumar(a, b):
#     return a + b

# --- resta.py ---
# def restar(a, b):
#     return a - b

# --- main.py ---
# from operaciones.suma import sumar
# from operaciones.resta import restar

# print(sumar(2, 3))
# print(restar(5, 2))


# ==========================
# 🔹 USO DE MÓDULOS DE LA LIBRERÍA ESTÁNDAR
# ==========================

# Python incluye muchos módulos útiles:

import math
print(math.sqrt(16))  # 4.0

import random
print(random.randint(1, 10))

import datetime
print(datetime.datetime.now())


# ==========================
# 🔹 INSTALAR PAQUETES EXTERNOS CON pip
# ==========================

# pip es el gestor de paquetes de Python
# Para instalar un paquete:

# pip install nombre_paquete

# Ejemplo:
# pip install requests

import requests
respuesta = requests.get("https://api.github.com")
print(respuesta.status_code)


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# Crear un paquete llamado "utilidades" con dos módulos:
# - conversor.py: convierte de dólares a pesos
# - texto.py: cuenta cuántas veces aparece una palabra

# Estructura:
# utilidades/
# ├── __init__.py
# ├── conversor.py
# └── texto.py

# --- conversor.py ---
# def dolares_a_pesos(dolares, tasa):
#     return dolares * tasa

# --- texto.py ---
# def contar_palabra(texto, palabra):
#     return texto.lower().split().count(palabra.lower())

# --- main.py ---
# from utilidades.conversor import dolares_a_pesos
# from utilidades.texto import contar_palabra

# print(dolares_a_pesos(100, 1500))  # 150000
# print(contar_palabra("Hola mundo mundo mundo", "mundo"))  # 3


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es un módulo y cómo importarlo
# - Cómo crear tu propio módulo y paquete
# - Cómo usar módulos de la librería estándar
# - Cómo instalar y usar paquetes externos con pip

# Próxima clase: Manejo de errores y excepciones – try, except, else, finally.
