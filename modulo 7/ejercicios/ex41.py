# ----------------------------------------
# CLASE 41: ENTORNOS VIRTUALES Y GESTIÓN DE DEPENDENCIAS
# ----------------------------------------
# 📌 Ejercicios prácticos simulando la creación, gestión y uso
# de entornos virtuales y dependencias en Python.
# ----------------------------------------

import os
import json

# =========================================================
# 🔹 EJERCICIO 1
# ---------------------------------------------------------
# Consigna: Crear un archivo "requirements.txt" con 3 dependencias ficticias
# y mostrar su contenido en pantalla.
# =========================================================
reqs = """requests==2.31.0
flask==2.3.2
pandas==2.1.0
"""
with open("requirements.txt", "w") as f:
    f.write(reqs)

print("\n[Ejercicio 1] Contenido de requirements.txt:")
with open("requirements.txt") as f:
    print(f.read())


# =========================================================
# 🔹 EJERCICIO 2
# ---------------------------------------------------------
# Consigna: Simular la instalación de dependencias leyendo
# el archivo "requirements.txt" y mostrando cada paquete
# como si se instalara.
# =========================================================
print("[Ejercicio 2] Simulación de instalación:")
with open("requirements.txt") as f:
    for linea in f:
        print(f"Instalando {linea.strip()}... ✅")


# =========================================================
# 🔹 EJERCICIO 3
# ---------------------------------------------------------
# Consigna: Crear un archivo "requirements_dev.txt" con dependencias
# de desarrollo y listarlas.
# =========================================================
reqs_dev = """pytest==7.4.0
black==23.7.0
mypy==1.5.0
"""
with open("requirements_dev.txt", "w") as f:
    f.write(reqs_dev)

print("\n[Ejercicio 3] Dependencias de desarrollo:")
with open("requirements_dev.txt") as f:
    for linea in f:
        print("-", linea.strip())


# =========================================================
# 🔹 EJERCICIO 4
# ---------------------------------------------------------
# Consigna: Simular la creación de un entorno virtual
# mostrando la carpeta que se generaría.
# =========================================================
print("\n[Ejercicio 4] Simulación de creación de entorno virtual:")
entorno = "mi_entorno"
os.makedirs(entorno, exist_ok=True)
print(f"Carpeta '{entorno}' creada como entorno virtual simulado.")
os.rmdir(entorno)


# =========================================================
# 🔹 EJERCICIO 5
# ---------------------------------------------------------
# Consigna: Generar un archivo JSON que guarde todas las
# dependencias de requirements.txt como una lista.
# =========================================================
with open("requirements.txt") as f:
    deps = [line.strip() for line in f]

with open("dependencias.json", "w") as f:
    json.dump(deps, f, indent=4)

print("\n[Ejercicio 5] Archivo dependencias.json creado con dependencias.")


# =========================================================
# 🔹 EJERCICIO 6
# ---------------------------------------------------------
# Consigna: Simular la activación de un entorno virtual
# imprimiendo el comando según el sistema operativo.
# =========================================================
print("\n[Ejercicio 6] Comando de activación de entorno:")
sistema = os.name  # 'nt' = Windows, 'posix' = Linux/Mac
if sistema == "nt":
    print("mi_entorno\\Scripts\\activate")
else:
    print("source mi_entorno/bin/activate")


# =========================================================
# 🔹 EJERCICIO 7
# ---------------------------------------------------------
# Consigna: Leer dependencias desde dependencias.json y
# mostrarlas como si fueran instaladas en un nuevo entorno.
# =========================================================
print("\n[Ejercicio 7] Instalación desde dependencias.json:")
with open("dependencias.json") as f:
    lista = json.load(f)
    for dep in lista:
        print(f"Instalando {dep}... ✅")


# =========================================================
# 🔹 EJERCICIO 8
# ---------------------------------------------------------
# Consigna: Crear un archivo "pyproject.toml" simulado con
# dependencias usando formato de texto.
# =========================================================
pyproject = """[tool.poetry]
name = "mi_proyecto"
version = "0.1.0"
description = "Proyecto de ejemplo con poetry"

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.31.0"
flask = "^2.3.2"

[tool.poetry.dev-dependencies]
pytest = "^7.4.0"
"""
with open("pyproject.toml", "w") as f:
    f.write(pyproject)

print("\n[Ejercicio 8] Archivo pyproject.toml creado.")


# =========================================================
# 🔹 EJERCICIO 9
# ---------------------------------------------------------
# Consigna: Simular la desinstalación de una dependencia
# leyendo el archivo requirements.txt.
# =========================================================
print("\n[Ejercicio 9] Simulación de desinstalación:")
with open("requirements.txt") as f:
    primera = f.readline().strip()
    print(f"Desinstalando {primera}... ❌")


# =========================================================
# 🔹 EJERCICIO 10
# ---------------------------------------------------------
# Consigna: Crear un pequeño "gestor de dependencias"
# que liste las dependencias instaladas y permita añadir
# una nueva al archivo requirements.txt.
# =========================================================
def listar_dependencias():
    with open("requirements.txt") as f:
        return [line.strip() for line in f]

def agregar_dependencia(dep):
    with open("requirements.txt", "a") as f:
        f.write(dep + "\n")

print("\n[Ejercicio 10] Gestor de dependencias:")
print("Dependencias actuales:", listar_dependencias())
nueva = "numpy==1.26.0"
agregar_dependencia(nueva)
print(f"Dependencia agregada: {nueva}")
print("Dependencias actualizadas:", listar_dependencias())


# ----------------------------------------
# ✅ Conclusión
# ----------------------------------------
# En estos ejercicios prácticos simulaste:
# - Crear y leer archivos requirements.txt y dev
# - Instalar y desinstalar dependencias
# - Crear entorno virtual (simulado)
# - Guardar dependencias en JSON y pyproject.toml
# - Hacer un mini gestor de dependencias
# ----------------------------------------
