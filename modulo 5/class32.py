# ----------------------------------------
# CLASE 33: CONTEXT MANAGERS (with, __enter__, __exit__)
# ----------------------------------------

# 📌 ¿Qué es un context manager?
# - Es un objeto que define un contexto de ejecución controlado.
# - Se usa con la palabra clave "with".
# - Permite manejar recursos (archivos, conexiones, locks) de forma segura,
#   asegurando que se liberen correctamente (incluso si hay errores).

# Ejemplo típico: abrir un archivo.
with open("ejemplo.txt", "w") as f:
    f.write("Hola, mundo!")
# El archivo se cierra automáticamente al salir del bloque "with".


# ==========================
# 🔹 CREAR UN CONTEXT MANAGER PERSONALIZADO
# ==========================

class GestorArchivo:
    def __init__(self, nombre, modo):
        self.nombre = nombre
        self.modo = modo
        self.archivo = None

    def __enter__(self):
        print("📂 Abriendo archivo...")
        self.archivo = open(self.nombre, self.modo, encoding="utf-8")
        return self.archivo  # Lo que devuelve __enter__ es lo que recibe "as"

    def __exit__(self, tipo, valor, traceback):
        print("📁 Cerrando archivo...")
        if self.archivo:
            self.archivo.close()
        # Si devolvemos True, se "suprime" la excepción.
        # Si devolvemos False o None, la excepción se propaga.
        return False

# Uso
with GestorArchivo("archivo_prueba.txt", "w") as f:
    f.write("Esto es un archivo manejado con un context manager personalizado.")


# ==========================
# 🔹 USANDO CONTEXTLIB
# ==========================

# Python incluye el módulo `contextlib` para crear context managers fácilmente.

from contextlib import contextmanager

@contextmanager
def gestor_simple(nombre):
    print("➡ Entrando al contexto")
    f = open(nombre, "w", encoding="utf-8")
    try:
        yield f  # Aquí se ejecuta el bloque "with"
    finally:
        f.close()
        print("⬅ Saliendo del contexto")

# Uso
with gestor_simple("archivo_contextlib.txt") as archivo:
    archivo.write("Texto dentro de un context manager con contextlib.")


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Crear un context manager que mida el tiempo de ejecución de un bloque de código.

import time

class Timer:
    def __enter__(self):
        self.inicio = time.time()
        print("⏱️ Iniciando temporizador...")
        return self

    def __exit__(self, tipo, valor, traceback):
        fin = time.time()
        duracion = fin - self.inicio
        print(f"⏱️ Duración: {duracion:.4f} segundos")

# Uso
with Timer():
    suma = sum([i**2 for i in range(10_000)])
    print("Suma calculada:", suma)


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es un context manager y para qué sirve
# - Cómo usar "with" para manejar archivos
# - Cómo implementar __enter__ y __exit__ en clases
# - Cómo usar contextlib para simplificar context managers
# - Mini proyecto: context manager que mide el tiempo de ejecución

# Próxima clase: Programación funcional en Python (map, filter, reduce, functools, etc.)
