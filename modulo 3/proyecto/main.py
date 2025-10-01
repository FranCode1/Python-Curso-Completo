"""
Gestor de Tareas - Proyecto del Módulo 3
Uso de módulos, excepciones, manejo de archivos y pruebas.
"""

from models.task import Task
from utils.file_manager import load_tasks, save_tasks

FILENAME = "tareas.json"

def main():
    # Crear algunas tareas
    tareas = [
        Task(1, "Estudiar Python", "Repasar módulos y excepciones"),
        Task(2, "Hacer ejercicio", "Salir a correr 30 minutos"),
        Task(3, "Leer un libro", "Continuar con novela de ciencia ficción")
    ]

    # Guardar en archivo
    save_tasks(FILENAME, tareas)
    print("✅ Tareas guardadas en JSON.")

    # Cargar desde archivo
    tareas_cargadas = load_tasks(FILENAME)
    print("\n📂 Tareas cargadas:")
    for t in tareas_cargadas:
        print(f"- {t.title} ({'✔️' if t.completed else '❌'})")

if __name__ == "__main__":
    main()
