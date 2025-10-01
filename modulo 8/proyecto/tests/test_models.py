import unittest
from db import DBManager
from models import Gestor

class TestGestor(unittest.TestCase):
    def setUp(self):
        self.gestor = Gestor(DBManager())

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Test tarea")
        tareas = self.gestor.listar_tareas()
        self.assertTrue(any("Test tarea" in t for t in tareas))

if __name__ == "__main__":
    unittest.main()
