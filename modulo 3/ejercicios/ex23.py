# ----------------------------------------
# CLASE 23: TESTING CON PYTEST
# ----------------------------------------
# Ejercicios prácticos resueltos
# ----------------------------------------

import pytest

# ==================================
# 🔹 FUNCIONES A TESTEAR
# ==================================

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

def es_par(n):
    return n % 2 == 0

def invertir_cadena(cadena):
    return cadena[::-1]

def maximo(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    return max(lista)

def contar_vocales(cadena):
    return sum(1 for c in cadena.lower() if c in "aeiou")

def factorial(n):
    if n < 0:
        raise ValueError("No existe factorial de negativos")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

# ==================================
# 🔹 TESTS UNITARIOS
# ==================================

# 1. Test de suma
def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

# 2. Test de resta
def test_restar():
    assert restar(10, 5) == 5
    assert restar(0, 5) == -5

# 3. Test de multiplicación parametrizado
@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 6),
    (0, 10, 0),
    (-1, 5, -5)
])
def test_multiplicar(a, b, esperado):
    assert multiplicar(a, b) == esperado

# 4. Test de división con manejo de excepción
def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        dividir(8, 0)

# 5. Test de par/impar
def test_es_par():
    assert es_par(4) is True
    assert es_par(7) is False

# 6. Test de invertir cadena
def test_invertir_cadena():
    assert invertir_cadena("hola") == "aloh"
    assert invertir_cadena("") == ""

# 7. Test de máximo con fixture
@pytest.fixture
def lista_ejemplo():
    return [1, 5, 7, 3]

def test_maximo(lista_ejemplo):
    assert maximo(lista_ejemplo) == 7
    with pytest.raises(ValueError):
        maximo([])

# 8. Test de contar vocales
@pytest.mark.parametrize("texto, esperado", [
    ("hola", 2),
    ("PYTEST", 1),
    ("", 0),
    ("murciélago", 5)
])
def test_contar_vocales(texto, esperado):
    assert contar_vocales(texto) == esperado

# 9. Test de factorial
@pytest.mark.parametrize("n, esperado", [
    (0, 1),
    (1, 1),
    (5, 120)
])
def test_factorial(n, esperado):
    assert factorial(n) == esperado

def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-3)

# 10. Test integrador con varias funciones
def test_operaciones_combinadas():
    resultado = multiplicar(sumar(2, 3), restar(10, 5))  # (2+3) * (10-5) = 25
    assert resultado == 25
    assert es_par(resultado) is True
