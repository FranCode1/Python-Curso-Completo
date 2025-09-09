# ----------------------------------------
# CLASE 17: DOCUMENTACIÓN EN PYTHON
# ----------------------------------------

# 📌 ¿Por qué es importante documentar código?

# - Facilita la comprensión (para otros y para vos en el futuro)
# - Mejora la colaboración en equipo
# - Permite que IDEs/autocompletado muestren ayuda útil
# - Profesionaliza tu trabajo

# Existen varias formas de documentar en Python:
# - Comentarios (inline o de bloque)
# - Docstrings (documentación de funciones, clases, módulos)


# ==========================
# 🔹 COMENTARIOS
# ==========================

# Comentarios simples con "#"
# Se usan para explicar líneas específicas

# Esta función calcula la suma de dos números
def sumar(a, b):
    return a + b  # Devuelve el resultado


# ==========================
# 🔹 DOCSTRINGS (""" """)
# ==========================

# Un docstring es un string al inicio de funciones, clases o archivos que explica su propósito

def saludar(nombre):
    """
    Recibe un nombre y muestra un saludo personalizado.

    Parámetros:
    - nombre (str): El nombre de la persona a saludar

    Retorna:
    - None
    """
    print(f"Hola, {nombre}!")

help(saludar)  # Muestra la documentación


# ==========================
# 🔹 DOCUMENTAR CLASES
# ==========================

class Persona:
    """
    Representa a una persona.

    Atributos:
    - nombre (str): nombre de la persona
    - edad (int): edad en años
    """

    def __init__(self, nombre, edad):
        """
        Inicializa una nueva persona.

        Parámetros:
        - nombre (str)
        - edad (int)
        """
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """Imprime un saludo con nombre y edad."""
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


# ==========================
# 🔹 VER DOCUMENTACIÓN OFICIAL
# ==========================

# Sitios útiles:
# - https://docs.python.org/3/
# - https://pypi.org/ → para buscar librerías de terceros
# - https://realpython.com/ → tutoriales y ejemplos claros
# - https://devdocs.io/python/ → documentación rápida
# - https://www.w3schools.com/python/ → para principiantes

# Podés usar help() en consola para ver documentación rápida:
# help(print)
# help(len)


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# Documentá este pequeño módulo que contiene 2 funciones

# def area_triangulo(base, altura):
#     """Calcula el área de un triángulo dado su base y altura."""
#     return (base * altura) / 2

# def es_par(numero):
#     """Devuelve True si el número es par, False si es impar."""
#     return numero % 2 == 0

# # Probar funciones con ayuda
# print(area_triangulo(10, 5))
# print(es_par(8))
# help(area_triangulo)


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Cómo escribir comentarios útiles y claros
# - Qué es un docstring y cómo documentar funciones, clases y módulos
# - Cómo usar help() y otras herramientas para entender código
# - Dónde encontrar y cómo leer la documentación oficial de Python

# Próxima clase: Módulos y paquetes – organización profesional del código.
