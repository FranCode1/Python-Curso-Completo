# ============================================================
# CLASE 47: GUÍA DE SIGUIENTES PASOS Y ÁREAS DE ESPECIALIZACIÓN
# ============================================================
# 🎯 Objetivo:
# Ahora que ya dominás los fundamentos de Python y completaste
# un proyecto integrador, llega el momento de pensar en el futuro.
# ¿Qué camino querés seguir como programador Python?
#
# En esta clase no hay tanto código, sino una guía práctica
# con ejemplos de cómo podés especializarte en diferentes áreas.
# ============================================================


# ------------------------------------------------------------
# 📌 1. DESARROLLO WEB (Flask, Django)
# ------------------------------------------------------------
# Flask → microframework, ideal para proyectos chicos y medianos.
# Django → framework completo, incluye ORM, panel admin, seguridad, etc.

# Ejemplo mini app con Flask:
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola desde Flask!"

if __name__ == "__main__":
    app.run(debug=True)
"""

# Ejemplo de creación de un modelo en Django (ORM):
"""
from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    completada = models.BooleanField(default=False)
"""


# ------------------------------------------------------------
# 📌 2. DATA SCIENCE
# ------------------------------------------------------------
# Python es uno de los lenguajes más usados en ciencia de datos,
# machine learning e inteligencia artificial.

# Librerías clave:
# - numpy → cálculos numéricos
# - pandas → análisis de datos
# - matplotlib / seaborn → visualización
# - scikit-learn → machine learning
# - tensorflow / pytorch → deep learning

# Ejemplo simple:
import numpy as np
import pandas as pd

datos = {"nombre": ["Ana", "Luis", "Marta"], "edad": [23, 34, 29]}
df = pd.DataFrame(datos)
print("\n📊 DataFrame de ejemplo:")
print(df)
print("Edad promedio:", np.mean(df["edad"]))


# ------------------------------------------------------------
# 📌 3. AUTOMATIZACIÓN AVANZADA
# ------------------------------------------------------------
# Python puede automatizar tareas repetitivas en tu PC, como
# organizar archivos, enviar mails o interactuar con la web.

# Ejemplo: mover archivos con `shutil`
import shutil
import os

# (comentado para evitar mover cosas reales)
# shutil.move("archivo.txt", "carpeta_destino/")


# ------------------------------------------------------------
# 📌 4. APLICACIONES MÓVILES
# ------------------------------------------------------------
# Opciones:
# - Kivy → framework para apps móviles multiplataforma.
# - BeeWare → permite crear apps nativas con Python.
# - O usar Python solo en backend + Flutter/React Native para frontend.


# ------------------------------------------------------------
# 📌 5. CREACIÓN DE LIBRERÍAS
# ------------------------------------------------------------
# Podés empaquetar tu código como librería reutilizable.
# Estructura básica:
"""
mi_libreria/
├── mi_libreria/
│   ├── __init__.py
│   ├── modulo1.py
│   └── modulo2.py
├── tests/
│   └── test_modulo1.py
├── setup.py
└── README.md
"""


# ------------------------------------------------------------
# 📌 6. PUBLICAR EN PyPI
# ------------------------------------------------------------
# Pasos básicos:
# 1. Crear tu librería con `setup.py`
# 2. Instalar herramientas → `pip install twine setuptools wheel`
# 3. Empaquetar → `python setup.py sdist bdist_wheel`
# 4. Subir a PyPI → `twine upload dist/*`


# ------------------------------------------------------------
# 📌 7. CONTRIBUIR A PROYECTOS OPEN SOURCE
# ------------------------------------------------------------
# - GitHub es el lugar principal.
# - Flujo básico:
#   1. Hacer un fork del repo
#   2. Crear una rama nueva para tus cambios
#   3. Hacer commits y push
#   4. Abrir un Pull Request


# ------------------------------------------------------------
# 🧭 CONCLUSIÓN Y PRÓXIMOS PASOS
# ------------------------------------------------------------
# - Elegí un área de especialización (web, datos, automatización, etc.)
# - Construí proyectos reales y prácticos en esa área
# - Publicá tu código en GitHub como portafolio
# - Aprendé a colaborar con otros en proyectos open source
# - Si querés, creá y publicá tu propia librería en PyPI
#
# Python es un lenguaje muy versátil. Ahora depende de vos decidir
# hacia dónde llevar tu camino como desarrollador.
