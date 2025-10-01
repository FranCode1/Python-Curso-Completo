# ----------------------------------------
# CLASE 22: TESTING CON UNITTEST
# ----------------------------------------

# 📌 ¿Qué es unittest?

# Es el módulo estándar de Python para realizar pruebas unitarias.
# Permite verificar automáticamente que el código funcione correctamente.

# 📌 ¿Por qué testear?
# ✅ Evita errores inesperados
# ✅ Te permite refactorizar sin miedo
# ✅ Automatiza la verificación del código


# ==========================
# 🔹 EJEMPLO BÁSICO DE PRUEBA
# ==========================

# Supongamos que tenemos este archivo llamado `operaciones.py`:

# def sumar(a, b):
#     return a + b

# def dividir(a, b):
#     return a / b

# Creamos un archivo `test_operaciones.py`:

import unittest
from operaciones import sumar, dividir

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(5, 0)

if __name__ == '__main__':
    unittest.main()


# ==========================
# 🔹 ESTRUCTURA DE UNA CLASE DE TEST
# ==========================

# - Hereda de unittest.TestCase
# - Cada método debe comenzar con `test_`
# - Usá métodos como:
#   - assertEqual(x, y)
#   - assertTrue(condición)
#   - assertFalse(condición)
#   - assertRaises(error)
#   - assertIn(valor, lista)
#   - assertIsNone(valor)


# ==========================
# 🔹 ORGANIZACIÓN DEL CÓDIGO DE PRUEBA
# ==========================

# Estructura recomendada:

# ├── mi_proyecto/
# │   ├── operaciones.py
# │   └── tests/
# │       └── test_operaciones.py


# ==========================
# 🔹 EJECUTAR LOS TESTS
# ==========================

# Podés ejecutar el archivo directamente:
# python test_operaciones.py

# O usar:
# python -m unittest test_operaciones.py

# También:
# python -m unittest discover tests


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Crear un archivo `utils.py` con:

# def es_par(n):
#     return n % 2 == 0

# def invertir_texto(txt):
#     return txt[::-1]

# Luego crear `test_utils.py` con:

# import unittest
# from utils import es_par, invertir_texto

# class TestUtils(unittest.TestCase):
#     def test_es_par(self):
#         self.assertTrue(es_par(4))
#         self.assertFalse(es_par(3))

#     def test_invertir_texto(self):
#         self.assertEqual(invertir_texto("python"), "nohtyp")

# if __name__ == "__main__":
#     unittest.main()


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es `unittest` y cómo usarlo
# - Cómo estructurar tus pruebas y verificar que tu código funcione
# - Cómo manejar errores esperados (como divisiones por cero)
# - Cómo organizar un entorno de testing profesional

# Próxima clase: Testing con Pytest – más simple, expresivo y poderoso para proyectos grandes.
