import sqlite3

DB_NAME = "tareas_final.db"

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self._crear_tabla()

    def _crear_tabla(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                estado TEXT DEFAULT 'pendiente',
                fecha TEXT
            )
        """)
        self.conn.commit()

    def insertar_tarea(self, titulo, descripcion):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO tareas (titulo, descripcion, fecha) VALUES (?, ?, date('now'))",
                    (titulo, descripcion))
        self.conn.commit()

    def obtener_tareas(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, titulo, descripcion, estado, fecha FROM tareas")
        return cur.fetchall()

    def marcar_completada(self, tarea_id):
        cur = self.conn.cursor()
        cur.execute("UPDATE tareas SET estado='completada' WHERE id=?", (tarea_id,))
        self.conn.commit()
