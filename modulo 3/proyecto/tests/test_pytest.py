import pytest
from models.task import Task

@pytest.fixture
def tarea():
    return Task(1, "Test Pytest", "Descripción")

def test_crear_tarea(tarea):
    assert tarea.title == "Test Pytest"

def test_marcar_completada(tarea):
    tarea.mark_completed()
    assert tarea.completed is True
