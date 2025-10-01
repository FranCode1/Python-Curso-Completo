# ----------------------------------------
# CLASE 22: TESTING CON UNITTEST
# ----------------------------------------

import unittest

# ==========================================================
# Código base a testear
# ==========================================================
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    return a / b

def multiplicar(a, b):
    return a * b

def es_par(n):
    return n % 2 == 0

def invertir_texto(txt):
    return txt[::-1]

def maximo(lista):
    return max(lista)

def minimo(lista):
    return min(lista)

def es_palindromo(palabra):
    return palabra == palabra[::-1]

def obtener_valor(diccionario, clave):
    return diccionario.get(clave, None)


# ==========================================================
# Ejercicios con consignas y soluciones
# ==========================================================

class TestFunciones(unittest.TestCase):

    # ------------------------------------------------------
    # EJERCICIO 1: Probar función sumar
    # Consigna: Verificar que sumar(a, b) devuelve la suma correcta.
    # ------------------------------------------------------
    def test_sumar(self):
        self.assertEqual(sumar(3, 4), 7)
        self.assertEqual(sumar(-2, 5), 3)

    # ------------------------------------------------------
    # EJERCICIO 2: Probar función restar
    # Consigna: Verificar que restar(a, b) devuelve la resta correcta.
    # ------------------------------------------------------
    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(0, 3), -3)

    # ------------------------------------------------------
    # EJERCICIO 3: Manejar ZeroDivisionError en dividir
    # Consigna: Comprobar que dividir por cero lanza una excepción.
    # ------------------------------------------------------
    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(5, 0)

    # ------------------------------------------------------
    # EJERCICIO 4: Probar multiplicar
    # Consigna: Verificar que multiplicar(a, b) funciona con positivos y negativos.
    # ------------------------------------------------------
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 5), 15)
        self.assertEqual(multiplicar(-2, 4), -8)

    # ------------------------------------------------------
    # EJERCICIO 5: Probar es_par
    # Consigna: Verificar que un número par devuelve True y uno impar False.
    # ------------------------------------------------------
    def test_es_par(self):
        self.assertTrue(es_par(6))
        self.assertFalse(es_par(7))

    # ------------------------------------------------------
    # EJERCICIO 6: Probar invertir_texto
    # Consigna: Verificar que el texto se invierte correctamente.
    # ------------------------------------------------------
    def test_invertir_texto(self):
        self.assertEqual(invertir_texto("python"), "nohtyp")
        self.assertEqual(invertir_texto("hola"), "aloh")

    # ------------------------------------------------------
    # EJERCICIO 7: Probar maximo
    # Consigna: Verificar que devuelve el valor más alto de una lista.
    # ------------------------------------------------------
    def test_maximo(self):
        self.assertEqual(maximo([1, 3, 2, 7]), 7)
        self.assertEqual(maximo([-5, -1, -10]), -1)

    # ------------------------------------------------------
    # EJERCICIO 8: Probar minimo
    # Consigna: Verificar que devuelve el valor más bajo de una lista.
    # ------------------------------------------------------
    def test_minimo(self):
        self.assertEqual(minimo([4, 8, 1, 9]), 1)
        self.assertEqual(minimo([0, -2, 5]), -2)

    # ------------------------------------------------------
    # EJERCICIO 9: Probar es_palindromo
    # Consigna: Verificar que palabras palíndromas devuelven True.
    # ------------------------------------------------------
    def test_es_palindromo(self):
        self.assertTrue(es_palindromo("radar"))
        self.assertFalse(es_palindromo("python"))

    # ------------------------------------------------------
    # EJERCICIO 10: Probar obtener_valor
    # Consigna: Verificar que devuelve el valor correcto o None si no existe.
    # ------------------------------------------------------
    def test_obtener_valor(self):
        datos = {"nombre": "Franco", "edad": 22}
        self.assertEqual(obtener_valor(datos, "nombre"), "Franco")
        self.assertIsNone(obtener_valor(datos, "apellido"))


# ==========================================================
# Punto de entrada de las pruebas
# ==========================================================
if __name__ == "__main__":
    unittest.main()
