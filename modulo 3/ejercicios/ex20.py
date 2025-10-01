# ----------------------------------------
# CLASE 20: MANEJO DE ARCHIVOS EN PYTHON
# ----------------------------------------

# 📌 Ejercicios prácticos resueltos
# Cada ejercicio tiene su consigna y su respuesta.


# ==========================================================
# EJERCICIO 1: Crear un archivo y escribir un mensaje
# Consigna: Crear un archivo "saludo.txt" y escribir "Hola desde Python".
# ==========================================================
with open("saludo.txt", "w") as f:
    f.write("Hola desde Python\n")

print("✅ Ejercicio 1: Archivo 'saludo.txt' creado.")


# ==========================================================
# EJERCICIO 2: Leer un archivo completo
# Consigna: Leer el contenido del archivo "saludo.txt" y mostrarlo en pantalla.
# ==========================================================
with open("saludo.txt", "r") as f:
    contenido = f.read()
    print("✅ Ejercicio 2: Contenido leído ->", contenido.strip())


# ==========================================================
# EJERCICIO 3: Escribir múltiples líneas
# Consigna: Crear un archivo "datos.txt" y guardar tres líneas de texto.
# ==========================================================
with open("datos.txt", "w") as f:
    f.write("Línea 1: Aprendiendo Python\n")
    f.write("Línea 2: Manejo de archivos\n")
    f.write("Línea 3: Ejercicio práctico\n")

print("✅ Ejercicio 3: Archivo 'datos.txt' creado con 3 líneas.")


# ==========================================================
# EJERCICIO 4: Leer línea por línea
# Consigna: Leer el archivo "datos.txt" y mostrar cada línea con un prefijo.
# ==========================================================
with open("datos.txt", "r") as f:
    for linea in f:
        print("✅ Ejercicio 4: Línea ->", linea.strip())


# ==========================================================
# EJERCICIO 5: Agregar texto a un archivo existente
# Consigna: Agregar una línea nueva al final de "datos.txt".
# ==========================================================
with open("datos.txt", "a") as f:
    f.write("Línea 4: Texto agregado con 'a'\n")

print("✅ Ejercicio 5: Línea agregada al archivo 'datos.txt'.")


# ==========================================================
# EJERCICIO 6: Leer archivo como lista de líneas
# Consigna: Cargar todas las líneas de "datos.txt" en una lista y mostrarla.
# ==========================================================
with open("datos.txt", "r") as f:
    lineas = f.readlines()
print("✅ Ejercicio 6: Lista de líneas ->", lineas)


# ==========================================================
# EJERCICIO 7: Verificar si un archivo existe
# Consigna: Comprobar si el archivo "datos.txt" existe en la carpeta.
# ==========================================================
import os
if os.path.exists("datos.txt"):
    print("✅ Ejercicio 7: El archivo 'datos.txt' existe.")
else:
    print("❌ Ejercicio 7: El archivo 'datos.txt' NO existe.")


# ==========================================================
# EJERCICIO 8: Leer y escribir en el mismo archivo
# Consigna: Abrir "mix.txt" en modo "r+" (lectura y escritura),
# escribir "Inicio del archivo" y luego mostrar su contenido.
# ==========================================================
with open("mix.txt", "w") as f:  # primero lo creamos vacío
    f.write("Texto inicial\n")

with open("mix.txt", "r+") as f:
    f.write("Inicio del archivo\n")
    f.seek(0)  # volver al inicio para leer
    print("✅ Ejercicio 8: Contenido de mix.txt ->")
    print(f.read())


# ==========================================================
# EJERCICIO 9: Copiar el contenido de un archivo en otro
# Consigna: Leer "datos.txt" y copiarlo a "copia_datos.txt".
# ==========================================================
with open("datos.txt", "r") as origen, open("copia_datos.txt", "w") as destino:
    for linea in origen:
        destino.write(linea)

print("✅ Ejercicio 9: Copia creada en 'copia_datos.txt'.")


# ==========================================================
# EJERCICIO 10: Mini proyecto de notas
# Consigna: Crear un sistema simple para agregar notas en "notas.txt"
# y luego mostrarlas todas.
# ==========================================================
def agregar_nota(texto):
    with open("notas.txt", "a") as f:
        f.write(texto + "\n")

def ver_notas():
    with open("notas.txt", "r") as f:
        print("Tus notas:")
        for linea in f:
            print("-", linea.strip())

# Probamos el sistema de notas
agregar_nota("Estudiar Python")
agregar_nota("Revisar ejercicios de archivos")
ver_notas()

print("✅ Ejercicio 10: Libreta de notas funcionando.")
