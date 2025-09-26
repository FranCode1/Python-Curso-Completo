import unittest
from models.task import Task

class TestTask(unittest.TestCase):
    def test_mark_completed(self):
        tarea = Task(1, "Prueba", "Descripción")
        tarea.mark_completed()
        self.assertTrue(tarea.completed)

if __name__ == "__main__":
    unittest.main()
