"""
Proyecto Módulo 5: Gestor de Tareas Avanzado
Aplicando programación avanzada en Python.
"""

import json
import time
from functools import reduce, lru_cache, partial
from datetime import datetime


# --------------------------
# Decorador avanzado: medir tiempo de ejecución
# --------------------------
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱ {func.__name__} ejecutado en {fin - inicio:.4f}s")
        return resultado
    return wrapper


# --------------------------
# Context Manager: Manejo de archivo JSON
# --------------------------
class GestorArchivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def __enter__(self):
        try:
            with open(self.nombre_archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []  # Lista vacía si no existe el archivo

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("⚠️ Error gestionado:", exc_value)
        return True


# --------------------------
# Iterador personalizado
# --------------------------
class IteradorPendientes:
    def __init__(self, tareas):
        self.tareas = [t for t in tareas if not t["completada"]]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.tareas):
            raise StopIteration
        tarea = self.tareas[self.index]
        self.index += 1
        return tarea


# --------------------------
# Funciones funcionales puras
# --------------------------
def agregar_tarea(lista, descripcion):
    """Agrega una nueva tarea (función pura: devuelve nueva lista)."""
    nueva = {"descripcion": descripcion, "completada": False, "creada": datetime.now().isoformat()}
    return lista + [nueva]  # No muta la lista original


def completar_tarea(lista, indice):
    """Marca una tarea como completada (nueva lista)."""
    return [
        {**t, "completada": True} if i == indice else t
        for i, t in enumerate(lista)
    ]


def contar_completadas(lista):
    """Reduce para contar tareas completadas."""
    return reduce(lambda acc, t: acc + (1 if t["completada"] else 0), lista, 0)


# --------------------------
# Uso del sistema
# --------------------------
@medir_tiempo
def main():
    archivo = "tareas.json"

    # Cargar tareas previas
    with GestorArchivo(archivo) as tareas:
        print("📂 Tareas cargadas:", len(tareas))

    # Agregar nuevas tareas
    tareas = agregar_tarea(tareas, "Estudiar Python Avanzado")
    tareas = agregar_tarea(tareas, "Practicar con proyectos")
    tareas = agregar_tarea(tareas, "Leer documentación oficial")

    # Completar la segunda tarea
    tareas = completar_tarea(tareas, 1)

    # Mostrar pendientes con iterador
    print("\n📌 Tareas pendientes:")
    for t in IteradorPendientes(tareas):
        print("-", t["descripcion"])

    # Estadísticas funcionales
    print("\n✅ Completadas:", contar_completadas(tareas))
    print("🟡 Pendientes:", len([t for t in tareas if not t["completada"]]))

    # Guardar en JSON (usando context manager manualmente)
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
