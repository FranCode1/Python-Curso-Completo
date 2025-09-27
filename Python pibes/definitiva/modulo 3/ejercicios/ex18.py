# ----------------------------------------
# CLASE 18: MÓDULOS Y PAQUETES EN PYTHON (EJERCICIOS)
# ----------------------------------------

# ==========================
# EJERCICIO 1
# ==========================
# Consigna: Crear un módulo "aritmetica" con funciones sumar y restar, e importarlas.
# (Simulación en el mismo archivo)

def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

print("Ej1:", sumar(10, 5), restar(10, 5))


# ==========================
# EJERCICIO 2
# ==========================
# Consigna: Usar el módulo "math" para calcular la raíz cuadrada y el logaritmo.
import math
print("Ej2:", math.sqrt(25), math.log(100, 10))


# ==========================
# EJERCICIO 3
# ==========================
# Consigna: Usar el módulo "random" para simular el lanzamiento de un dado (1 al 6).
import random
print("Ej3: Dado →", random.randint(1, 6))


# ==========================
# EJERCICIO 4
# ==========================
# Consigna: Usar el módulo "datetime" para obtener la fecha y hora actual, y solo el año.
import datetime
ahora = datetime.datetime.now()
print("Ej4:", ahora, "Año:", ahora.year)


# ==========================
# EJERCICIO 5
# ==========================
# Consigna: Crear un módulo "geometria" con una función area_rectangulo(base, altura).
def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo"""
    return base * altura

print("Ej5:", area_rectangulo(10, 4))


# ==========================
# EJERCICIO 6
# ==========================
# Consigna: Crear un "paquete" ficticio "conversores" con dos funciones:
# - metros_a_km
# - km_a_millas
def metros_a_km(metros):
    """Convierte metros a kilómetros"""
    return metros / 1000

def km_a_millas(km):
    """Convierte kilómetros a millas"""
    return km * 0.621371

print("Ej6:", metros_a_km(5000), km_a_millas(10))


# ==========================
# EJERCICIO 7
# ==========================
# Consigna: Usar el módulo "statistics" para calcular la media y la mediana de una lista.
import statistics
datos = [5, 10, 15, 20, 25]
print("Ej7: Media:", statistics.mean(datos), "Mediana:", statistics.median(datos))


# ==========================
# EJERCICIO 8
# ==========================
# Consigna: Crear un "módulo de texto" con una función contar_palabras.
def contar_palabras(texto):
    """
    Cuenta cuántas palabras tiene un texto.

    Parámetros:
    - texto (str)

    Retorna:
    - int: cantidad de palabras
    """
    return len(texto.split())

print("Ej8:", contar_palabras("Hola mundo desde Python módulos"))


# ==========================
# EJERCICIO 9
# ==========================
# Consigna: Usar el módulo "os" para obtener el directorio actual de trabajo.
import os
print("Ej9:", os.getcwd())


# ==========================
# EJERCICIO 10
# ==========================
# Consigna: Crear un paquete ficticio "finanzas" con un módulo "impuestos" que calcule IVA.
def calcular_iva(precio, tasa=0.21):
    """
    Calcula el precio final con IVA.

    Parámetros:
    - precio (float): precio base
    - tasa (float): porcentaje IVA (por defecto 21%)

    Retorna:
    - float: precio con IVA
    """
    return precio * (1 + tasa)

print("Ej10:", calcular_iva(1000))
