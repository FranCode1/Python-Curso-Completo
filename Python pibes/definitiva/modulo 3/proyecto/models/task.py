"""
Módulo que define la clase Task para representar una tarea.
"""

class Task:
    """
    Clase que representa una tarea en el gestor de tareas.
    """
    def __init__(self, task_id: int, title: str, description: str, completed: bool = False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        """Marca la tarea como completada"""
        self.completed = True

    def to_dict(self) -> dict:
        """Convierte la tarea en un diccionario (para guardar en JSON)"""
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data: dict):
        """Crea un objeto Task a partir de un diccionario"""
        return Task(
            task_id=data["id"],
            title=data["title"],
            description=data["description"],
            completed=data["completed"]
        )
