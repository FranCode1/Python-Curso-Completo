"""
Módulo para manejar la persistencia de datos en JSON.
"""

import json
from models.task import Task
from utils.exceptions import FileError

def load_tasks(filename: str) -> list[Task]:
    """Carga tareas desde un archivo JSON"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    except FileNotFoundError:
        raise FileError(f"Archivo '{filename}' no encontrado.")
    except json.JSONDecodeError:
        raise FileError(f"Error al leer el archivo '{filename}'.")

def save_tasks(filename: str, tasks: list[Task]) -> None:
    """Guarda tareas en un archivo JSON"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)
    except Exception as e:
        raise FileError(f"Error al guardar el archivo: {e}")
