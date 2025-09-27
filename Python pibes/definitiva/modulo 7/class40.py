# ----------------------------------------
# CLASE 40: LIBRERÍAS ESTÁNDAR EN PYTHON
# ----------------------------------------

# 📌 Python incluye muchas librerías estándar que nos facilitan
# tareas comunes sin necesidad de instalar nada adicional.
# En esta clase veremos:
# - math
# - random
# - datetime
# - os
# - json

# ==========================
# 🔹 MÓDULO math
# ==========================
import math

print("=== MATH ===")
print("Raíz cuadrada de 16:", math.sqrt(16))
print("Seno de 90°:", math.sin(math.radians(90)))
print("Número pi:", math.pi)
print("Logaritmo natural de 10:", math.log(10))
print("Factorial de 5:", math.factorial(5))
print()

# ==========================
# 🔹 MÓDULO random
# ==========================
import random

print("=== RANDOM ===")
print("Número aleatorio entre 1 y 10:", random.randint(1, 10))
print("Número flotante aleatorio entre 0 y 1:", random.random())
print("Elección aleatoria de una lista:", random.choice(["rojo", "verde", "azul"]))
print("Muestra de 2 elementos:", random.sample(range(10), 2))
print()

# ==========================
# 🔹 MÓDULO datetime
# ==========================
from datetime import datetime, timedelta

print("=== DATETIME ===")
ahora = datetime.now()
print("Fecha y hora actual:", ahora)
print("Año:", ahora.year, "Mes:", ahora.month, "Día:", ahora.day)
print("Dentro de 7 días:", ahora + timedelta(days=7))
print("Formato personalizado:", ahora.strftime("%d/%m/%Y %H:%M:%S"))
print()

# ==========================
# 🔹 MÓDULO os
# ==========================
import os

print("=== OS ===")
print("Directorio actual:", os.getcwd())
print("Archivos en el directorio actual:", os.listdir("."))
nuevo_dir = "carpeta_prueba"
os.makedirs(nuevo_dir, exist_ok=True)
print(f"Se creó la carpeta: {nuevo_dir}")
os.rmdir(nuevo_dir)
print(f"Se eliminó la carpeta: {nuevo_dir}")
print()

# ==========================
# 🔹 MÓDULO json
# ==========================
import json

print("=== JSON ===")
datos = {
    "nombre": "Franco",
    "edad": 22,
    "lenguajes": ["Python", "JavaScript", "C++"],
    "activo": True
}

# Convertir diccionario a JSON (serialización)
json_str = json.dumps(datos, indent=4)
print("Diccionario a JSON:")
print(json_str)

# Convertir JSON a diccionario (deserialización)
diccionario = json.loads(json_str)
print("JSON a diccionario:", diccionario)
print()

# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================
# 🎯 Crear un programa que guarde en un archivo JSON
# un registro de temperaturas aleatorias de los próximos 7 días.

registro = []
for i in range(7):
    fecha = (datetime.now() + timedelta(days=i)).strftime("%d/%m/%Y")
    temp = round(random.uniform(10, 35), 2)
    registro.append({"fecha": fecha, "temperatura": temp})

with open("temperaturas.json", "w") as archivo:
    json.dump(registro, archivo, indent=4)

print("✅ Archivo 'temperaturas.json' creado con temperaturas simuladas.")

# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------
# En esta clase aprendiste:
# - Usar funciones matemáticas con math
# - Generar números aleatorios con random
# - Manejar fechas y horas con datetime
# - Interactuar con el sistema de archivos con os
# - Serializar y deserializar datos con json
#
# Próxima clase: Módulo collections en Python.
