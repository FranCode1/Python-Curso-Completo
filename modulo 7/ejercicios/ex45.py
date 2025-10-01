# ============================================================
# CLASE 45: Buenas prácticas en Python
# ============================================================
# En esta clase veremos:
# 1. Estilo PEP8
# 2. Código limpio y legible
# 3. Modularidad (organización en módulos y funciones)
# 4. Uso básico de Git para control de versiones
# ============================================================

import math

# ============================================================
# 1. PEP8: nombres descriptivos y snake_case
# ============================================================
# Consigna: Crea una función que convierta grados Celsius a Fahrenheit
# siguiendo las reglas de PEP8.
def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return celsius * 9 / 5 + 32


print("Ejercicio 1:", celsius_a_fahrenheit(30))

# ============================================================
# 2. Código limpio: una sola responsabilidad
# ============================================================
# Consigna: Divide la funcionalidad en funciones pequeñas y claras.
def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio**2


def mostrar_area(radio: float) -> None:
    """Muestra el área del círculo de forma formateada."""
    print(f"Ejercicio 2: Área del círculo: {calcular_area_circulo(radio):.2f}")


mostrar_area(7)

# ============================================================
# 3. Reutilización de código
# ============================================================
# Consigna: Usa funciones auxiliares en lugar de repetir lógica.
def es_par(numero: int) -> bool:
    """Verifica si un número es par."""
    return numero % 2 == 0


def filtrar_pares(numeros: list[int]) -> list[int]:
    """Devuelve solo los números pares de una lista."""
    return [n for n in numeros if es_par(n)]


print("Ejercicio 3:", filtrar_pares(list(range(1, 11))))

# ============================================================
# 4. Anotaciones de tipo
# ============================================================
# Consigna: Añade hints de tipo para mejorar la legibilidad.
def sumar(a: int, b: int) -> int:
    """Devuelve la suma de dos números enteros."""
    return a + b


print("Ejercicio 4:", sumar(5, 10))

# ============================================================
# 5. Docstrings (PEP257)
# ============================================================
# Consigna: Usa docstrings para documentar clases y métodos.
class Persona:
    """Representa a una persona con nombre y edad."""

    def __init__(self, nombre: str, edad: int) -> None:
        """Inicializa una nueva persona."""
        self.nombre = nombre
        self.edad = edad

    def saludar(self) -> str:
        """Devuelve un saludo con nombre y edad."""
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


persona = Persona("Franco", 22)
print("Ejercicio 5:", persona.saludar())

# ============================================================
# 6. Principio DRY (Don't Repeat Yourself)
# ============================================================
# Consigna: Evita repetir código usando funciones reutilizables.
def aplicar_operacion(lista: list[int], funcion) -> list[int]:
    """Aplica una función a cada elemento de una lista."""
    return [funcion(x) for x in lista]


print("Ejercicio 6:", aplicar_operacion([1, 2, 3], lambda x: x * 2))

# ============================================================
# 7. Principio SRP (Single Responsibility Principle)
# ============================================================
# Consigna: Divide la lógica de cálculo y presentación.
def calcular_promedio(numeros: list[int]) -> float:
    """Calcula el promedio de una lista de números."""
    return sum(numeros) / len(numeros)


def mostrar_promedio(numeros: list[int]) -> None:
    """Muestra el promedio de una lista de números."""
    print(f"Ejercicio 7: Promedio = {calcular_promedio(numeros):.2f}")


mostrar_promedio([4, 6, 8, 10])

# ============================================================
# 8. Manejo de excepciones
# ============================================================
# Consigna: Escribe código limpio con manejo de errores.
def dividir(a: int, b: int) -> float:
    """Divide a entre b, manejando división por cero."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: División por cero.")
        return float("inf")


print("Ejercicio 8:", dividir(10, 2))
print("Ejercicio 8 (error):", dividir(5, 0))

# ============================================================
# 9. Modularidad (simulación)
# ============================================================
# Consigna: Separa la lógica en "módulos".
# Aquí simulamos imports con funciones en el mismo archivo.
def saludar(nombre: str) -> str:
    """Función que estaría en utils.py."""
    return f"Hola {nombre}"


def ejecutar_modularidad():
    """Función que simula main.py importando utils."""
    print("Ejercicio 9:", saludar("Franco"))


ejecutar_modularidad()

# ============================================================
# 10. Git (ejemplo en comentarios)
# ============================================================
# Consigna: Escribe un flujo de Git para un proyecto.
# ------------------------------------------------------------
# git init
# git add .
# git commit -m "Primer commit"
# git branch nueva-funcionalidad
# git checkout nueva-funcionalidad
# git merge main
# git push origin main
# ------------------------------------------------------------
print("Ejercicio 10: Flujo de Git documentado en comentarios.")

# ============================================================
# CONCLUSIÓN
# - PEP8 garantiza un estilo consistente.
# - Código limpio facilita mantenimiento.
# - Modularidad y principios SOLID organizan mejor el proyecto.
# - Git es esencial para control de versiones.
# ============================================================
