# ----------------------------------------
# CLASE 20: MANEJO DE ARCHIVOS EN PYTHON
# ----------------------------------------

# 📌 ¿Por qué es importante?
# Permite leer y escribir archivos de texto, guardar logs, datos o configuraciones externas.

# Función básica: open()
# Sintaxis: open("archivo.txt", "modo")

# Modos comunes:
# "r"  → leer
# "w"  → escribir (sobrescribe si ya existe)
# "a"  → agregar al final
# "x"  → crear un archivo nuevo (error si ya existe)
# "b"  → modo binario
# "+"  → lectura y escritura


# ==========================
# 🔹 ESCRIBIR UN ARCHIVO
# ==========================

# Abre (o crea) el archivo y escribe una línea
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo\n")
    archivo.write("Segunda línea")

# El archivo se cierra automáticamente al salir del with


# ==========================
# 🔹 LEER UN ARCHIVO
# ==========================

# Leer todo el contenido
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido completo:")
    print(contenido)

# Leer línea por línea
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print("Línea:", linea.strip())


# ==========================
# 🔹 AGREGAR TEXTO A UN ARCHIVO
# ==========================

with open("archivo.txt", "a") as archivo:
    archivo.write("\nNueva línea agregada")


# ==========================
# 🔹 LEER LÍNEAS COMO LISTA
# ==========================

with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()
    print("Lista de líneas:", lineas)


# ==========================
# 🔹 LEER Y ESCRIBIR EN UN SOLO ARCHIVO
# ==========================

# open("archivo.txt", "r+")  → leer y escribir desde el principio
# open("archivo.txt", "a+")  → leer y agregar desde el final


# ==========================
# 🔹 COMPROBAR SI UN ARCHIVO EXISTE (opcional)
# ==========================

import os

if os.path.exists("archivo.txt"):
    print("El archivo existe.")
else:
    print("El archivo no existe.")


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Crear una libreta de notas simple
# - Agregar una nota al archivo
# - Leer todas las notas guardadas

# def agregar_nota(texto):
#     with open("notas.txt", "a") as f:
#         f.write(texto + "\n")

# def ver_notas():
#     with open("notas.txt", "r") as f:
#         print("Tus notas:")
#         for linea in f:
#             print("-", linea.strip())

# agregar_nota("Estudiar Python")
# agregar_nota("Clase 20 completa")
# ver_notas()


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Cómo leer, escribir y agregar texto en archivos
# - La diferencia entre modos ("r", "w", "a", etc.)
# - Cómo usar `with open()` correctamente
# - Cómo verificar si un archivo existe
# - Cómo implementar una libreta de notas simple

# Próxima clase: Excepciones en Python – cómo manejar errores con try-except.
