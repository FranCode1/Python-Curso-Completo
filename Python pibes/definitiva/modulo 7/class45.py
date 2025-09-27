# ============================================================
# CLASE 45: Buenas prácticas en Python
# ============================================================
# En esta clase veremos:
# 1. Estilo PEP8
# 2. Código limpio y legible
# 3. Modularidad (organización en módulos y funciones)
# 4. Uso básico de Git para control de versiones
# ============================================================


# ------------------------------------------------------------
# 1. PEP8 (Estilo de código en Python)
# ------------------------------------------------------------
# 📌 Reglas importantes:
# - Nombres de variables y funciones en snake_case.
# - Clases en PascalCase.
# - Líneas de máximo 79 caracteres.
# - Espacios alrededor de operadores (=, +, -, etc.).
# - 2 líneas en blanco entre funciones y clases.

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b


resultado = suma(10, 20)
print(f"Resultado: {resultado}")


# ------------------------------------------------------------
# 2. Código limpio
# ------------------------------------------------------------
# 📌 Consejos:
# - Usar nombres descriptivos.
# - Evitar duplicar código.
# - Comentar solo cuando el código no sea autoexplicativo.
# - Funciones cortas y con una sola responsabilidad.

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    import math
    return math.pi * radio**2


print(f"Área del círculo: {calcular_area_circulo(5):.2f}")


# ------------------------------------------------------------
# 3. Modularidad
# ------------------------------------------------------------
# 📌 Separar el código en archivos (módulos) y carpetas (paquetes).
# Ejemplo de estructura de proyecto:
#
# mi_proyecto/
# ├── main.py
# ├── utils.py
# └── models/
#     └── persona.py
#
# En utils.py podríamos tener funciones auxiliares:
# def saludar(nombre): return f"Hola {nombre}"
#
# Y luego importarlas en main.py:
# from utils import saludar
#
# print(saludar("Franco"))


# ------------------------------------------------------------
# 4. Git: control de versiones
# ------------------------------------------------------------
# 📌 Git permite llevar historial de cambios en proyectos.
# Comandos básicos:
#
# git init                   # Inicia un repositorio
# git status                 # Muestra cambios
# git add archivo.py         # Añade un archivo al "staging"
# git commit -m "mensaje"    # Guarda los cambios en el historial
# git log                    # Muestra el historial de commits
# git branch nueva-rama      # Crea una rama
# git checkout nueva-rama    # Cambia de rama
# git merge otra-rama        # Fusiona ramas
# git push origin main       # Sube cambios a GitHub


# ------------------------------------------------------------
# 🧪 MINI PROYECTO
# ------------------------------------------------------------
# 🎯 Crear un mini script modular con buenas prácticas.

def es_par(numero: int) -> bool:
    """Verifica si un número es par."""
    return numero % 2 == 0


def mostrar_pares(lista):
    """Filtra y muestra los números pares de una lista."""
    pares = [n for n in lista if es_par(n)]
    print("Números pares:", pares)


if __name__ == "__main__":
    numeros = list(range(1, 11))
    mostrar_pares(numeros)


# ============================================================
# CONCLUSIÓN
# - PEP8 garantiza un estilo consistente.
# - Código limpio = más fácil de mantener y entender.
# - Modularidad evita duplicación y mejora la organización.
# - Git es esencial para colaborar y guardar historial.
# ============================================================
