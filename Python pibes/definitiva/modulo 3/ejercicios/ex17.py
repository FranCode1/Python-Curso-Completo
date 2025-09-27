# ----------------------------------------
# CLASE 17: DOCUMENTACIÓN EN PYTHON (EJERCICIOS)
# ----------------------------------------

# ==========================
# EJERCICIO 1
# ==========================
# Consigna: Documentar una función que calcule el área de un círculo.
import math

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    - radio (float): Radio del círculo

    Retorna:
    - float: Área del círculo
    """
    return math.pi * radio ** 2

print("Ej1:", area_circulo(5))


# ==========================
# EJERCICIO 2
# ==========================
# Consigna: Documentar una función que convierta grados Celsius a Fahrenheit.
def celsius_a_fahrenheit(c):
    """
    Convierte grados Celsius a Fahrenheit.

    Fórmula: F = (C * 9/5) + 32

    Parámetros:
    - c (float): Temperatura en grados Celsius

    Retorna:
    - float: Temperatura en grados Fahrenheit
    """
    return (c * 9/5) + 32

print("Ej2:", celsius_a_fahrenheit(30))


# ==========================
# EJERCICIO 3
# ==========================
# Consigna: Documentar una clase que represente un rectángulo con métodos de área y perímetro.
class Rectangulo:
    """
    Representa un rectángulo.

    Atributos:
    - base (float): longitud de la base
    - altura (float): longitud de la altura
    """

    def __init__(self, base, altura):
        """
        Inicializa un rectángulo.

        Parámetros:
        - base (float)
        - altura (float)
        """
        self.base = base
        self.altura = altura

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.base * self.altura

    def perimetro(self):
        """Devuelve el perímetro del rectángulo."""
        return 2 * (self.base + self.altura)

rect = Rectangulo(10, 5)
print("Ej3:", rect.area(), rect.perimetro())


# ==========================
# EJERCICIO 4
# ==========================
# Consigna: Documentar una función que invierta un string.
def invertir_texto(texto):
    """
    Invierte el texto recibido.

    Parámetros:
    - texto (str): cadena a invertir

    Retorna:
    - str: texto invertido
    """
    return texto[::-1]

print("Ej4:", invertir_texto("Python"))


# ==========================
# EJERCICIO 5
# ==========================
# Consigna: Documentar una clase "Estudiante" con un método para mostrar información.
class Estudiante:
    """
    Representa a un estudiante.

    Atributos:
    - nombre (str): nombre del estudiante
    - carrera (str): carrera que estudia
    """

    def __init__(self, nombre, carrera):
        """
        Inicializa un estudiante.

        Parámetros:
        - nombre (str)
        - carrera (str)
        """
        self.nombre = nombre
        self.carrera = carrera

    def presentar(self):
        """Imprime una presentación del estudiante."""
        return f"Soy {self.nombre} y estudio {self.carrera}."

e = Estudiante("Franco", "Ingeniería Informática")
print("Ej5:", e.presentar())


# ==========================
# EJERCICIO 6
# ==========================
# Consigna: Documentar una función que cuente las vocales en un texto.
def contar_vocales(texto):
    """
    Cuenta cuántas vocales tiene un texto.

    Parámetros:
    - texto (str): cadena de texto

    Retorna:
    - int: cantidad de vocales en el texto
    """
    return sum(1 for letra in texto.lower() if letra in "aeiou")

print("Ej6:", contar_vocales("Documentación"))


# ==========================
# EJERCICIO 7
# ==========================
# Consigna: Documentar una función que devuelva el número mayor de una lista.
def numero_mayor(lista):
    """
    Devuelve el número mayor en una lista.

    Parámetros:
    - lista (list): lista de números

    Retorna:
    - int/float: el valor máximo
    """
    return max(lista)

print("Ej7:", numero_mayor([5, 10, 2, 99, 32]))


# ==========================
# EJERCICIO 8
# ==========================
# Consigna: Documentar una función que valide si una palabra es un palíndromo.
def es_palindromo(palabra):
    """
    Verifica si una palabra es un palíndromo.

    Parámetros:
    - palabra (str): palabra a verificar

    Retorna:
    - bool: True si es palíndromo, False en caso contrario
    """
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

print("Ej8:", es_palindromo("Anita lava la tina"))


# ==========================
# EJERCICIO 9
# ==========================
# Consigna: Documentar una función que calcule el factorial de un número.
def factorial(n):
    """
    Calcula el factorial de un número de forma recursiva.

    Parámetros:
    - n (int): número entero no negativo

    Retorna:
    - int: factorial de n
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Ej9:", factorial(5))


# ==========================
# EJERCICIO 10
# ==========================
# Consigna: Documentar una clase que represente una cuenta bancaria.
class CuentaBancaria:
    """
    Representa una cuenta bancaria.

    Atributos:
    - titular (str): nombre del dueño
    - saldo (float): saldo disponible
    """

    def __init__(self, titular, saldo=0):
        """
        Inicializa una cuenta bancaria.

        Parámetros:
        - titular (str)
        - saldo (float, opcional): por defecto 0
        """
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        """Agrega dinero a la cuenta."""
        self.saldo += monto

    def retirar(self, monto):
        """Retira dinero de la cuenta si hay saldo suficiente."""
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        return False

    def mostrar_saldo(self):
        """Devuelve el saldo actual de la cuenta."""
        return self.saldo

cuenta = CuentaBancaria("Franco", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
print("Ej10:", cuenta.mostrar_saldo())
