import datetime

class Tarea:
    def __init__(self, titulo, descripcion="", estado="pendiente", fecha=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.fecha = fecha or datetime.date.today()

    def completar(self):
        self.estado = "completada"

    def __repr__(self):
        return f"<Tarea {self.titulo} - {self.estado}>"

class Gestor:
    def __init__(self, db_manager):
        self.db = db_manager

    def agregar_tarea(self, titulo, descripcion=""):
        self.db.insertar_tarea(titulo, descripcion)

    def listar_tareas(self):
        return self.db.obtener_tareas()

    def completar_tarea(self, tarea_id):
        self.db.marcar_completada(tarea_id)
