# ----------------------------------------
# CLASE 42: AUTOMATIZACIÓN DE TAREAS CON SCRIPTS
# ----------------------------------------

# 📌 Una de las grandes ventajas de Python es que podemos usarlo
# para automatizar tareas repetitivas como:
# - Manipular archivos y carpetas
# - Procesar texto y datos
# - Descargar información de Internet
# - Enviar correos electrónicos
# - Ejecutar procesos del sistema

import os
import shutil
import datetime
import requests

# ==========================
# 🔹 AUTOMATIZAR ARCHIVOS Y CARPETAS
# ==========================

# Crear una carpeta automáticamente
carpeta = "backup"
os.makedirs(carpeta, exist_ok=True)
print(f"📂 Carpeta '{carpeta}' creada o ya existente.")

# Crear un archivo de texto con fecha actual
fecha = datetime.datetime.now().strftime("%Y-%m-%d")
with open(f"{carpeta}/registro_{fecha}.txt", "w") as f:
    f.write("Este es un archivo de respaldo automático.\n")
print(f"📝 Archivo de registro creado en {carpeta}/")

# Copiar archivo a otra carpeta (simulación de backup)
destino = "backup_copia"
os.makedirs(destino, exist_ok=True)
shutil.copy(f"{carpeta}/registro_{fecha}.txt", destino)
print(f"✅ Archivo copiado en {destino}/")

# ==========================
# 🔹 AUTOMATIZAR DESCARGAS
# ==========================

url = "https://jsonplaceholder.typicode.com/todos/1"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    with open("tarea.json", "w") as f:
        f.write(respuesta.text)
    print("⬇ Archivo JSON descargado desde la web y guardado como 'tarea.json'.")

# ==========================
# 🔹 AUTOMATIZAR LIMPIEZA DE ARCHIVOS
# ==========================

# Eliminar archivos viejos de la carpeta backup (más de 0 días en este ejemplo)
for archivo in os.listdir(carpeta):
    ruta = os.path.join(carpeta, archivo)
    if os.path.isfile(ruta):
        edad = datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(ruta))
        if edad.days > 0:
            os.remove(ruta)
            print(f"🗑 Archivo eliminado: {archivo}")

# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Script de automatización de "respaldo diario":
# - Crea una carpeta backup con fecha
# - Copia todos los archivos de una carpeta origen
# - Genera un log con fecha y hora

def respaldo_automatico(origen, destino="backup_diario"):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    carpeta_destino = os.path.join(destino, f"respaldo_{fecha}")
    os.makedirs(carpeta_destino, exist_ok=True)

    with open(os.path.join(carpeta_destino, "log.txt"), "w") as log:
        log.write(f"Respaldo generado el {fecha}\n")
        log.write("Archivos respaldados:\n")

        for archivo in os.listdir(origen):
            ruta = os.path.join(origen, archivo)
            if os.path.isfile(ruta):
                shutil.copy(ruta, carpeta_destino)
                log.write(f"- {archivo}\n")

    print(f"📦 Respaldo completado en: {carpeta_destino}")

# Ejecutar mini proyecto (usa la carpeta actual como origen)
respaldo_automatico(".")

# ==========================
# CONCLUSIÓN DE LA CLASE
# ==========================
# En esta clase aprendiste:
# - Cómo automatizar creación, copia y eliminación de archivos
# - Cómo descargar datos de Internet con requests
# - Cómo generar respaldos automáticos con Python
#
# Próxima clase: Web scraping con BeautifulSoup.
