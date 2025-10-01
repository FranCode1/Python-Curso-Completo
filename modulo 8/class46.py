# ============================================================
# CLASE 46: PROYECTO INTEGRADOR
# ============================================================
# 🎯 Objetivo:
# Crear un pequeño sistema de gestión de tareas (ToDo list)
# que integre todo lo aprendido:
#
# - Funciones y clases
# - Manejo de archivos (guardar y cargar tareas)
# - Manejo de errores y excepciones
# - Organización modular (simulada en un solo archivo.py)
# - Pruebas básicas con unittest
# ============================================================


# ------------------------------------------------------------
# 📌 Módulo: models.py (simulado aquí)
# ------------------------------------------------------------
class Tarea:
    """Representa una tarea de la lista ToDo."""

    def __init__(self, titulo, descripcion=""):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True

    def __str__(self):
        estado = "✔" if self.completada else "✗"
        return f"[{estado}] {self.titulo} - {self.descripcion}"


# ------------------------------------------------------------
# 📌 Módulo: utils.py (simulado aquí)
# ------------------------------------------------------------
import json
import os


ARCHIVO_TAREAS = "tareas.json"


def guardar_tareas(tareas):
    """Guarda la lista de tareas en un archivo JSON."""
    try:
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
            json.dump([t.__dict__ for t in tareas], f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"⚠ Error al guardar tareas: {e}")


def cargar_tareas():
    """Carga las tareas desde un archivo JSON."""
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Tarea(**t) for t in data]
    except Exception as e:
        print(f"⚠ Error al cargar tareas: {e}")
        return []


# ------------------------------------------------------------
# 📌 Módulo: main.py (simulado aquí)
# ------------------------------------------------------------
def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=== 📋 Gestor de Tareas ===")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Guardar y salir")


def ver_tareas(tareas):
    """Muestra todas las tareas."""
    if not tareas:
        print("No hay tareas.")
        return
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")


def agregar_tarea(tareas):
    """Agrega una nueva tarea a la lista."""
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción (opcional): ")
    tarea = Tarea(titulo, descripcion)
    tareas.append(tarea)
    print("✅ Tarea agregada.")


def completar_tarea(tareas):
    """Marca una tarea como completada."""
    ver_tareas(tareas)
    try:
        num = int(input("Número de tarea a completar: "))
        tareas[num - 1].marcar_completada()
        print("✅ Tarea completada.")
    except (ValueError, IndexError):
        print("⚠ Número inválido.")


def main():
    """Función principal del programa."""
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            ver_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            guardar_tareas(tareas)
            print("💾 Tareas guardadas. ¡Hasta luego!")
            break
        else:
            print("⚠ Opción inválida.")


# ------------------------------------------------------------
# 📌 Módulo: test_app.py (simulado aquí con unittest)
# ------------------------------------------------------------
import unittest


class TestTarea(unittest.TestCase):
    def test_crear_tarea(self):
        tarea = Tarea("Estudiar Python", "Repasar OOP")
        self.assertEqual(tarea.titulo, "Estudiar Python")
        self.assertFalse(tarea.completada)

    def test_marcar_completada(self):
        tarea = Tarea("Escribir código")
        tarea.marcar_completada()
        self.assertTrue(tarea.completada)


# ------------------------------------------------------------
# 📌 Ejecución del programa y pruebas
# ------------------------------------------------------------
if __name__ == "__main__":
    # Ejecutar el gestor de tareas
    # main()

    # Ejecutar las pruebas
    print("\n🧪 Ejecutando pruebas...")
    unittest.main(exit=False)

# ============================================================
# CONCLUSIÓN
# ✅ En este proyecto integrador aplicamos:
# - Clases (Tarea)
# - Funciones con responsabilidades claras
# - Manejo de archivos (tareas.json)
# - Excepciones (try/except al guardar y cargar)
# - Organización modular (models, utils, main, tests simulados en un solo archivo)
# - Testing con unittest
# ============================================================