# ============================================================
# CLASE 44: Bases de datos con sqlite3
# ============================================================
# En esta clase aprenderemos a usar SQLite desde Python con el módulo sqlite3.
# Veremos cómo:
# 1. Crear una base de datos y tablas.
# 2. Insertar datos.
# 3. Consultar información.
# 4. Actualizar y eliminar registros.
# ============================================================

import sqlite3

# ------------------------------------------------------------
# 1. Conexión y creación de tabla
# ------------------------------------------------------------
# Conectamos a una base de datos (se crea el archivo si no existe)
conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()

# Creamos una tabla de usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    email TEXT UNIQUE
)
""")
conn.commit()
print("Tabla creada correctamente.")

# ------------------------------------------------------------
# 2. Insertar datos
# ------------------------------------------------------------
usuarios = [
    ("Ana", 25, "ana@example.com"),
    ("Luis", 30, "luis@example.com"),
    ("Maria", 22, "maria@example.com")
]

# Insertar múltiples filas
cursor.executemany("INSERT OR IGNORE INTO usuarios (nombre, edad, email) VALUES (?, ?, ?)", usuarios)
conn.commit()
print("Datos insertados.")

# ------------------------------------------------------------
# 3. Consultar datos
# ------------------------------------------------------------
print("\n=== Consulta de usuarios ===")
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

# ------------------------------------------------------------
# 4. Consultar con condición
# ------------------------------------------------------------
print("\n=== Usuarios mayores de 24 años ===")
cursor.execute("SELECT nombre, edad FROM usuarios WHERE edad > 24")
for fila in cursor.fetchall():
    print(fila)

# ------------------------------------------------------------
# 5. Actualizar datos
# ------------------------------------------------------------
cursor.execute("UPDATE usuarios SET edad = 26 WHERE nombre = 'Ana'")
conn.commit()
print("\nUsuario 'Ana' actualizado.")

# ------------------------------------------------------------
# 6. Eliminar datos
# ------------------------------------------------------------
cursor.execute("DELETE FROM usuarios WHERE nombre = 'Luis'")
conn.commit()
print("Usuario 'Luis' eliminado.")

# ------------------------------------------------------------
# 7. Ver tabla final
# ------------------------------------------------------------
print("\n=== Estado final de la tabla ===")
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

# Cerramos la conexión
conn.close()
print("\nConexión cerrada.")

# ============================================================
# CONCLUSIÓN:
# - sqlite3 permite trabajar con bases de datos ligeras en archivos.
# - Aprendimos a crear tablas, insertar, consultar, actualizar y borrar datos.
# ============================================================
