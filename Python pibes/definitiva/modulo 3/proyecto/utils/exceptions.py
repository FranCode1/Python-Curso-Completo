"""
Módulo con excepciones personalizadas.
"""

class TaskError(Exception):
    """Excepción base para errores en el gestor de tareas."""
    pass

class FileError(TaskError):
    """Error relacionado con el manejo de archivos."""
    pass
