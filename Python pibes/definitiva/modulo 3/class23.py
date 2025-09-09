# ----------------------------------------
# CLASE 23: TESTING CON PYTEST
# ----------------------------------------

# 📌 ¿Por qué usar pytest?
# - Sintaxis más simple y legible que unittest
# - Soporte nativo para fixtures y parametrización
# - Compatible con unittest
# - Fácil integración con editores y CI

# ==========================
# 🔹 INSTALACIÓN Y USO BÁSICO
# ==========================

# Instalar con pip:
# pip install pytest

# Crear un archivo llamado `test_operaciones.py`:

# --- operaciones.py ---
def sumar(a, b):
    return a + b

def dividir(a, b):
    return a / b

# --- test_operaciones.py ---
from operaciones import sumar, dividir
import pytest

def test_sumar():
    assert sumar(2, 3) == 5

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(4, 0)

# Ejecutar en terminal:
# pytest
# pytest test_operaciones.py

# ==========================
# 🔹 FIXTURES (para datos reutilizables)
# ==========================

import pytest

@pytest.fixture
def datos_ejemplo():
    return (10, 5)

def test_suma_con_fixture(datos_ejemplo):
    a, b = datos_ejemplo
    assert sumar(a, b) == 15


# ==========================
# 🔹 PARAMETRIZACIÓN DE TESTS
# ==========================

# Permite correr el mismo test con diferentes valores:

@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (10, 5, 15),
    (-1, 1, 0)
])
def test_suma_parametrizada(a, b, esperado):
    assert sumar(a, b) == esperado


# ==========================
# 🔹 INTEGRACIÓN CON VS CODE / TERMINAL
# ==========================

# ✅ En terminal:
# Ejecutar en la raíz del proyecto:
# pytest
# pytest -v            → más detalles
# pytest --maxfail=1   → detiene al primer error

# ✅ En VS Code:
# 1. Asegurate de tener Python y pytest instalados.
# 2. En la paleta de comandos (Ctrl+Shift+P), escribí:
#    “Python: Configure Tests” → elegí pytest.
# 3. Detectará los tests automáticamente.
# 4. Desde el explorador lateral podés correr tests individuales.

# ✅ Bonus: crear un archivo de configuración opcional:
# pytest.ini
# ----------------------
# [pytest]
# addopts = -v
# testpaths = tests
# ----------------------


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Crear tests para archivo `math_utils.py` con:
# def multiplicar(a, b):
#     return a * b

# def es_par(n):
#     return n % 2 == 0

# --- test_math_utils.py ---
# import pytest
# from math_utils import multiplicar, es_par

# @pytest.mark.parametrize("a, b, esperado", [
#     (2, 3, 6),
#     (0, 5, 0),
#     (-1, 5, -5)
# ])
# def test_multiplicar(a, b, esperado):
#     assert multiplicar(a, b) == esperado

# def test_es_par():
#     assert es_par(4) is True
#     assert es_par(5) is False


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Cómo instalar y usar pytest con tests simples
# - Cómo usar fixtures para compartir datos entre tests
# - Cómo usar parametrización para testear muchos casos fácilmente
# - Cómo integrar pytest con tu editor y automatizar tu flujo de trabajo

# Próxima clase: Concurrencia y multiprocessing – cómo escribir programas eficientes y paralelos.
