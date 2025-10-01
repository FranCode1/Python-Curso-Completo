# ----------------------------------------
# CLASE 41: ENTORNOS VIRTUALES Y GESTIÓN DE DEPENDENCIAS
# ----------------------------------------

# 📌 En Python, los entornos virtuales (venv) permiten aislar proyectos
# para que cada uno tenga sus propias dependencias sin interferir entre sí.
# Esto es esencial cuando trabajamos con varias versiones de librerías.

# ==========================
# 🔹 CREAR UN ENTORNO VIRTUAL
# ==========================
# Desde la terminal (no en este archivo):
#
#   python -m venv mi_entorno
#
# Esto creará una carpeta llamada `mi_entorno` con el entorno virtual.

# ==========================
# 🔹 ACTIVAR EL ENTORNO VIRTUAL
# ==========================
# Windows:
#   mi_entorno\Scripts\activate
#
# Linux/Mac:
#   source mi_entorno/bin/activate
#
# Para desactivar:
#   deactivate

# ==========================
# 🔹 USAR pip PARA DEPENDENCIAS
# ==========================
# Una vez dentro del entorno virtual, instalamos librerías con pip:
#
#   pip install requests
#   pip install flask
#
# Para ver qué dependencias hay instaladas:
#   pip list
#
# Para desinstalar:
#   pip uninstall flask

# ==========================
# 🔹 requirements.txt
# ==========================
# Para compartir dependencias de un proyecto, podemos crear un archivo:
#
#   pip freeze > requirements.txt
#
# Para instalar todas las dependencias en otro entorno:
#
#   pip install -r requirements.txt

# ==========================
# 🔹 pyproject.toml Y HERRAMIENTAS MODERNAS
# ==========================
# Además de pip, existen herramientas modernas para gestionar dependencias:
# - poetry
# - pipenv
# - hatch
#
# Estas permiten manejar entornos, dependencias y empaquetado más fácilmente.

# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================
# 🎯 Simularemos el flujo de creación de un proyecto con entorno virtual
# y dependencias usando pip.

import os

# Crear un archivo de requirements ficticio
requirements = """requests==2.31.0
flask==2.3.2
"""

with open("requirements.txt", "w") as f:
    f.write(requirements)

print("✅ Archivo 'requirements.txt' creado con dependencias de ejemplo.")

# Simulación: leer requirements.txt y mostrar qué instalaríamos
print("\nDependencias a instalar en el entorno virtual:")
with open("requirements.txt") as f:
    for linea in f:
        print(" -", linea.strip())

# ==========================
# CONCLUSIÓN DE LA CLASE
# ==========================
# En esta clase aprendiste:
# - Qué es un entorno virtual y cómo crearlo con venv
# - Cómo activar y desactivar entornos virtuales
# - Instalar y desinstalar dependencias con pip
# - Usar requirements.txt para compartir dependencias
# - Herramientas modernas como poetry y pipenv
#
# Próxima clase: Uso del módulo collections en Python.
