# ----------------------------------------
# CLASE 19: DISTRIBUCIÓN DE CÓDIGO EN PYTHON
# ----------------------------------------

# 📌 ¿Qué significa distribuir código?
# - Preparar tu código para ser utilizado como script ejecutable o como módulo reutilizable.
# - Organizar el proyecto para que sea mantenible, escalable y profesional.


# ==========================
# 🔹 if __name__ == "__main__"
# ==========================

# Este bloque permite que un archivo se ejecute directamente, pero no se ejecute cuando se lo importa.

# --- archivo.py ---
def saludar():
    print("Hola desde la función")

if __name__ == "__main__":
    print("Este archivo se ejecuta directamente")
    saludar()

# Si importás `archivo` desde otro archivo, **no** se ejecutará el bloque `if __name__ == "__main__"`.


# ==========================
# 🔹 ESTRUCTURA DE PROYECTO RECOMENDADA
# ==========================

# ├── mi_proyecto/
# │   ├── main.py              # punto de entrada del programa
# │   ├── __init__.py          # marca que es un paquete
# │   ├── modulo1.py           # lógica 1
# │   ├── modulo2.py           # lógica 2
# │   ├── utils/
# │   │   ├── __init__.py
# │   │   └── helpers.py       # funciones auxiliares
# │   ├── tests/
# │   │   └── test_modulo1.py  # pruebas automáticas
# │   └── README.md            # descripción del proyecto


# ==========================
# 🔹 EJEMPLO PRÁCTICO DE USO DE __main__
# ==========================

# --- operaciones.py ---
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

if __name__ == "__main__":
    print("Probando funciones de operaciones:")
    print(sumar(5, 3))  # 8
    print(restar(5, 2))  # 3


# --- main.py ---
from operaciones import sumar

resultado = sumar(10, 20)
print(f"Resultado final: {resultado}")


# ==========================
# 🔹 VENTAJAS DE ESTA ORGANIZACIÓN
# ==========================

# ✅ Permite reutilizar módulos en otros proyectos fácilmente
# ✅ Hace que el código sea más mantenible y testeable
# ✅ Separa lógica, utilidades, entradas y pruebas


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Objetivo: Crear una pequeña calculadora estructurada profesionalmente

# Estructura:
# calculadora/
# ├── main.py
# ├── operaciones.py
# ├── utils/
# │   └── mensajes.py
# └── tests/
#     └── test_operaciones.py

# --- operaciones.py ---
# def sumar(a, b):
#     return a + b

# def restar(a, b):
#     return a - b

# if __name__ == "__main__":
#     print("Modo test:")
#     print(sumar(1, 2))

# --- main.py ---
# from operaciones import sumar
# print("Resultado:", sumar(7, 3))


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Cómo usar `if __name__ == "__main__"` para controlar ejecución
# - Cómo estructurar un proyecto Python de forma profesional
# - Cómo separar la lógica principal de las utilidades
# - Cómo preparar tu código para pruebas y reutilización

# Próxima clase: Manejo de errores y excepciones.
