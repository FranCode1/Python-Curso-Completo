# ----------------------------------------
# CLASE 42: AUTOMATIZACIÓN DE TAREAS CON SCRIPTS
# ----------------------------------------
# 📌 Ejercicios prácticos para aplicar automatización con Python:
# - Manipular archivos y carpetas
# - Procesar texto y datos
# - Descargar información de Internet
# - Limpieza automática
# - Respaldos y logs
# ----------------------------------------

import os
import shutil
import datetime
import requests
import json

# =========================================================
# 🔹 EJERCICIO 1
# ---------------------------------------------------------
# Consigna: Crear una carpeta llamada "reportes" y generar
# dentro un archivo con la fecha actual.
# =========================================================
os.makedirs("reportes", exist_ok=True)
fecha = datetime.datetime.now().strftime("%Y-%m-%d")
with open(f"reportes/reporte_{fecha}.txt", "w") as f:
    f.write("📊 Reporte automático generado.\n")
print(f"[Ejercicio 1] Reporte generado en reportes/reporte_{fecha}.txt")


# =========================================================
# 🔹 EJERCICIO 2
# ---------------------------------------------------------
# Consigna: Descargar un JSON desde Internet y guardarlo en
# un archivo local llamado "datos.json".
# =========================================================
url = "https://jsonplaceholder.typicode.com/users/1"
resp = requests.get(url)
if resp.status_code == 200:
    with open("datos.json", "w") as f:
        f.write(resp.text)
    print("[Ejercicio 2] Archivo 'datos.json' descargado y guardado.")


# =========================================================
# 🔹 EJERCICIO 3
# ---------------------------------------------------------
# Consigna: Leer el archivo "datos.json" y mostrar en pantalla
# el nombre del usuario.
# =========================================================
with open("datos.json") as f:
    datos = json.load(f)
print("[Ejercicio 3] Nombre del usuario en datos.json:", datos["name"])


# =========================================================
# 🔹 EJERCICIO 4
# ---------------------------------------------------------
# Consigna: Crear un respaldo automático copiando todos los
# archivos de la carpeta actual hacia "respaldo_simple".
# =========================================================
os.makedirs("respaldo_simple", exist_ok=True)
for archivo in os.listdir("."):
    if os.path.isfile(archivo):
        shutil.copy(archivo, "respaldo_simple")
print("[Ejercicio 4] Archivos copiados a carpeta respaldo_simple.")


# =========================================================
# 🔹 EJERCICIO 5
# ---------------------------------------------------------
# Consigna: Generar un log con la lista de archivos de la
# carpeta actual, incluyendo tamaño en bytes.
# =========================================================
with open("log_archivos.txt", "w") as log:
    for archivo in os.listdir("."):
        if os.path.isfile(archivo):
            tamaño = os.path.getsize(archivo)
            log.write(f"{archivo} - {tamaño} bytes\n")
print("[Ejercicio 5] Log de archivos generado en log_archivos.txt.")


# =========================================================
# 🔹 EJERCICIO 6
# ---------------------------------------------------------
# Consigna: Eliminar todos los archivos de la carpeta
# "respaldo_simple" que tengan más de 1 KB.
# =========================================================
for archivo in os.listdir("respaldo_simple"):
    ruta = os.path.join("respaldo_simple", archivo)
    if os.path.getsize(ruta) > 1024:
        os.remove(ruta)
        print(f"[Ejercicio 6] Archivo eliminado: {archivo}")


# =========================================================
# 🔹 EJERCICIO 7
# ---------------------------------------------------------
# Consigna: Crear un script que organice los archivos por
# extensión dentro de carpetas (ej: .txt -> carpeta txt).
# =========================================================
for archivo in os.listdir("."):
    if os.path.isfile(archivo):
        ext = archivo.split(".")[-1]
        carpeta = f"ext_{ext}"
        os.makedirs(carpeta, exist_ok=True)
        shutil.move(archivo, os.path.join(carpeta, archivo))
print("[Ejercicio 7] Archivos organizados por extensión.")


# =========================================================
# 🔹 EJERCICIO 8
# ---------------------------------------------------------
# Consigna: Generar automáticamente un archivo README.md con
# la fecha y hora actual.
# =========================================================
ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
with open("README.md", "w") as f:
    f.write(f"# Proyecto de Automatización\n\nÚltima actualización: {ahora}\n")
print("[Ejercicio 8] Archivo README.md generado.")


# =========================================================
# 🔹 EJERCICIO 9
# ---------------------------------------------------------
# Consigna: Descargar 3 recursos diferentes de Internet
# (ejemplo: JSONs) y guardarlos en carpeta "descargas".
# =========================================================
os.makedirs("descargas", exist_ok=True)
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
]
for i, link in enumerate(urls, start=1):
    r = requests.get(link)
    if r.status_code == 200:
        with open(f"descargas/post_{i}.json", "w") as f:
            f.write(r.text)
print("[Ejercicio 9] Archivos descargados en carpeta descargas.")


# =========================================================
# 🔹 EJERCICIO 10
# ---------------------------------------------------------
# Consigna: Crear un script que haga un "respaldo con log":
# copia todos los archivos de la carpeta descargas a una
# carpeta con fecha y crea un log.txt dentro.
# =========================================================
def respaldo_con_log(origen, destino="respaldo_logs"):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    carpeta_destino = os.path.join(destino, f"backup_{fecha}")
    os.makedirs(carpeta_destino, exist_ok=True)
    with open(os.path.join(carpeta_destino, "log.txt"), "w") as log:
        for archivo in os.listdir(origen):
            ruta = os.path.join(origen, archivo)
            if os.path.isfile(ruta):
                shutil.copy(ruta, carpeta_destino)
                log.write(f"Copiado: {archivo}\n")
    print(f"[Ejercicio 10] Respaldo completado en {carpeta_destino}")

respaldo_con_log("descargas")


# ----------------------------------------
# ✅ Conclusión
# ----------------------------------------
# En estos ejercicios aprendiste a:
# - Crear, copiar y eliminar archivos con Python
# - Descargar recursos desde Internet con requests
# - Generar logs automáticos
# - Organizar archivos por extensión
# - Crear respaldos con registro de actividad
# ----------------------------------------
