# ============================================================
# CLASE 47: GUÍA DE SIGUIENTES PASOS Y ÁREAS DE ESPECIALIZACIÓN
# ============================================================
# 🎯 Objetivo:
# Practicar con ejemplos prácticos de distintas áreas en las que
# te podés especializar como programador Python.
# ============================================================

import os
import json
import numpy as np
import pandas as pd
import shutil
import requests
import unittest

# ============================================================
# 📌 EJERCICIO 1: Mini API con Flask
# ------------------------------------------------------------
# Consigna:
# Crear una app básica con Flask que devuelva un mensaje en la ruta "/".
# (Simulado aquí con una función en lugar de levantar el servidor).
# ============================================================
def mini_api():
    return "¡Hola desde Flask (simulado)!"


# ============================================================
# 📌 EJERCICIO 2: Modelo simple estilo Django
# ------------------------------------------------------------
# Consigna:
# Simular la creación de un modelo Django con clases Python puras.
# ============================================================
class Usuario:
    def __init__(self, nombre, email, activo=True):
        self.nombre = nombre
        self.email = email
        self.activo = activo

    def __str__(self):
        return f"👤 {self.nombre} ({'Activo' if self.activo else 'Inactivo'})"


# ============================================================
# 📌 EJERCICIO 3: Análisis de datos con pandas y numpy
# ------------------------------------------------------------
# Consigna:
# Crear un DataFrame y calcular el promedio de una columna.
# ============================================================
def promedio_edades():
    datos = {"nombre": ["Ana", "Luis", "Marta"], "edad": [23, 34, 29]}
    df = pd.DataFrame(datos)
    return np.mean(df["edad"])


# ============================================================
# 📌 EJERCICIO 4: Visualización con matplotlib
# ------------------------------------------------------------
# Consigna:
# Crear un gráfico de barras con matplotlib (simulación con lista).
# ============================================================
def generar_datos_grafico():
    return {"categorias": ["A", "B", "C"], "valores": [5, 3, 8]}


# ============================================================
# 📌 EJERCICIO 5: Automatizar organización de archivos
# ------------------------------------------------------------
# Consigna:
# Simular mover un archivo de "origen.txt" a la carpeta "destino".
# ============================================================
def mover_archivo(origen, destino):
    # (comentado para evitar mover cosas reales en tu PC)
    # shutil.move(origen, destino)
    return f"Archivo {origen} → {destino} (simulado)"


# ============================================================
# 📌 EJERCICIO 6: Automatizar descarga de un archivo
# ------------------------------------------------------------
# Consigna:
# Descargar el contenido de una URL con requests.
# ============================================================
def descargar_url(url):
    try:
        resp = requests.get(url, timeout=5)
        return resp.status_code
    except Exception as e:
        return f"Error: {e}"


# ============================================================
# 📌 EJERCICIO 7: Simular estructura de librería
# ------------------------------------------------------------
# Consigna:
# Crear un módulo "matematica" dentro de este mismo archivo
# con una función de suma reutilizable.
# ============================================================
class Matematica:
    @staticmethod
    def suma(a, b):
        return a + b


# ============================================================
# 📌 EJERCICIO 8: Simular publicación en PyPI
# ------------------------------------------------------------
# Consigna:
# Crear un diccionario que represente un `setup.py` simple.
# ============================================================
def generar_setup():
    return {
        "name": "mi_libreria",
        "version": "0.1.0",
        "author": "Franco Lugo",
        "description": "Ejemplo de librería Python",
    }


# ============================================================
# 📌 EJERCICIO 9: Flujo de GitHub (simulado)
# ------------------------------------------------------------
# Consigna:
# Simular un flujo de trabajo en GitHub: fork, branch, commit, PR.
# ============================================================
def flujo_github():
    return ["Fork repo", "Crear rama", "Commit cambios", "Abrir Pull Request"]


# ============================================================
# 📌 EJERCICIO 10: Pruebas unitarias
# ------------------------------------------------------------
# Consigna:
# Crear pruebas unitarias para las funciones y clases creadas.
# ============================================================
class TestEspecializacion(unittest.TestCase):
    def test_flask_api(self):
        self.assertEqual(mini_api(), "¡Hola desde Flask (simulado)!")

    def test_usuario(self):
        u = Usuario("Ana", "ana@mail.com")
        self.assertTrue(u.activo)
        self.assertIn("Ana", str(u))

    def test_promedio(self):
        self.assertEqual(promedio_edades(), (23+34+29)/3)

    def test_matematica(self):
        self.assertEqual(Matematica.suma(3, 4), 7)

    def test_setup(self):
        setup = generar_setup()
        self.assertEqual(setup["name"], "mi_libreria")

    def test_flujo_github(self):
        flujo = flujo_github()
        self.assertIn("Commit cambios", flujo)


# ------------------------------------------------------------
# 📌 EJECUCIÓN DEL ARCHIVO
# ------------------------------------------------------------
if __name__ == "__main__":
    print("🚀 Ejercicios de especialización en Python")
    print("Edad promedio (pandas + numpy):", promedio_edades())
    print("Simulación mover archivo:", mover_archivo("origen.txt", "destino/"))
    print("Setup simulado:", generar_setup())
    print("Flujo GitHub:", flujo_github())

    print("\n🧪 Ejecutando pruebas...")
    unittest.main(exit=False)
