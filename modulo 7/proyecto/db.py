import sqlite3

DB_NAME = "tareas.db"

def crear_tabla():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            estado TEXT DEFAULT 'pendiente'
        )
    """)
    conn.commit()
    conn.close()

def agregar_tarea(titulo):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO tareas (titulo) VALUES (?)", (titulo,))
    conn.commit()
    conn.close()

def listar_tareas():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, titulo, estado FROM tareas")
    tareas = cur.fetchall()
    conn.close()
    return tareas
