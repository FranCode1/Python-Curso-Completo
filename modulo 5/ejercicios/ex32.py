# ----------------------------------------
# CLASE 33: CONTEXT MANAGERS (with, __enter__, __exit__)
# ----------------------------------------

# ============================================================
# EJERCICIO 1: Context Manager para abrir y cerrar archivos
# ============================================================
# Consigna:
# Crea un context manager que abra un archivo en modo escritura y lo cierre automáticamente.

class GestorArchivo:
    def __init__(self, nombre, modo):
        self.nombre = nombre
        self.modo = modo
        self.archivo = None

    def __enter__(self):
        print("📂 Abriendo archivo...")
        self.archivo = open(self.nombre, self.modo, encoding="utf-8")
        return self.archivo

    def __exit__(self, tipo, valor, traceback):
        print("📁 Cerrando archivo...")
        if self.archivo:
            self.archivo.close()
        return False

with GestorArchivo("ej1.txt", "w") as f:
    f.write("Ejercicio 1: Hola desde un context manager personalizado.\n")


# ============================================================
# EJERCICIO 2: Medir tiempo de ejecución
# ============================================================
# Consigna:
# Implementa un context manager que mida cuánto tarda en ejecutarse un bloque de código.

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

with Timer():
    suma = sum([i**2 for i in range(100000)])
    print("Suma calculada:", suma)


# ============================================================
# EJERCICIO 3: Context Manager con contextlib
# ============================================================
# Consigna:
# Usa @contextmanager de contextlib para crear un gestor simple de archivos.

from contextlib import contextmanager

@contextmanager
def gestor_simple(nombre):
    print("➡ Entrando al contexto")
    f = open(nombre, "w", encoding="utf-8")
    try:
        yield f
    finally:
        f.close()
        print("⬅ Saliendo del contexto")

with gestor_simple("ej3.txt") as archivo:
    archivo.write("Ejercicio 3: Usando contextlib.\n")


# ============================================================
# EJERCICIO 4: Suprimir excepciones
# ============================================================
# Consigna:
# Crea un context manager que capture excepciones y no las deje propagarse.

class SuprimirErrores:
    def __enter__(self):
        return self

    def __exit__(self, tipo, valor, traceback):
        if tipo:
            print(f"⚠️ Error suprimido: {valor}")
            return True  # Evita que la excepción se propague

with SuprimirErrores():
    print("Antes del error")
    1 / 0
    print("Después del error (no se ejecuta)")


# ============================================================
# EJERCICIO 5: Context Manager para conexión simulada
# ============================================================
# Consigna:
# Simula una conexión a base de datos que se abre y cierra automáticamente.

class ConexionBD:
    def __enter__(self):
        print("🔌 Conectando a la base de datos...")
        return "conexion_activa"

    def __exit__(self, tipo, valor, traceback):
        print("❌ Cerrando conexión a la base de datos...")

with ConexionBD() as conn:
    print("Usando:", conn)


# ============================================================
# EJERCICIO 6: Cambiar temporalmente el directorio de trabajo
# ============================================================
# Consigna:
# Crea un context manager que cambie al directorio "temp" durante el bloque "with" y luego regrese.

import os

class CambiarDirectorio:
    def __init__(self, nuevo):
        self.nuevo = nuevo
        self.viejo = os.getcwd()

    def __enter__(self):
        print(f"📂 Cambiando a: {self.nuevo}")
        os.makedirs(self.nuevo, exist_ok=True)
        os.chdir(self.nuevo)
        return os.getcwd()

    def __exit__(self, tipo, valor, traceback):
        os.chdir(self.viejo)
        print(f"↩ Volviendo a: {self.viejo}")

with CambiarDirectorio("temp"):
    print("Directorio actual:", os.getcwd())

print("Directorio final:", os.getcwd())


# ============================================================
# EJERCICIO 7: Capturar logs en un archivo
# ============================================================
# Consigna:
# Haz un context manager que escriba logs en un archivo automáticamente.

class Logger:
    def __init__(self, archivo):
        self.archivo = archivo

    def __enter__(self):
        self.f = open(self.archivo, "a", encoding="utf-8")
        return self.f

    def __exit__(self, tipo, valor, traceback):
        self.f.close()
        print("📖 Log guardado en", self.archivo)

with Logger("ej7.log") as log:
    log.write("Ejercicio 7: Nuevo log registrado.\n")


# ============================================================
# EJERCICIO 8: Context Manager para listas temporales
# ============================================================
# Consigna:
# Crea un context manager que cree una lista temporal y se limpie al salir.

class ListaTemporal:
    def __enter__(self):
        print("📋 Creando lista temporal...")
        self.lista = []
        return self.lista

    def __exit__(self, tipo, valor, traceback):
        print("🗑️ Eliminando lista temporal")
        del self.lista

with ListaTemporal() as l:
    l.extend([1, 2, 3])
    print("Lista dentro del contexto:", l)


# ============================================================
# EJERCICIO 9: Medir memoria usada (simulado)
# ============================================================
# Consigna:
# Haz un context manager que imprima el uso de memoria antes y después (simulación con números).

import random

class Memoria:
    def __enter__(self):
        self.memoria_inicial = random.randint(50, 100)
        print(f"💾 Memoria inicial: {self.memoria_inicial}MB")
        return self

    def __exit__(self, tipo, valor, traceback):
        memoria_final = self.memoria_inicial + random.randint(1, 20)
        print(f"💾 Memoria final: {memoria_final}MB")

with Memoria():
    suma = sum([i for i in range(1000)])


# ============================================================
# EJERCICIO 10: Context Manager para abrir múltiples archivos
# ============================================================
# Consigna:
# Implementa un context manager que maneje varios archivos a la vez.

class MultiArchivo:
    def __init__(self, *nombres):
        self.nombres = nombres
        self.archivos = []

    def __enter__(self):
        for nombre in self.nombres:
            f = open(nombre, "w", encoding="utf-8")
            self.archivos.append(f)
        return self.archivos

    def __exit__(self, tipo, valor, traceback):
        for f in self.archivos:
            f.close()
        print("📂 Todos los archivos cerrados.")

with MultiArchivo("ej10a.txt", "ej10b.txt") as archivos:
    archivos[0].write("Archivo A\n")
    archivos[1].write("Archivo B\n")
