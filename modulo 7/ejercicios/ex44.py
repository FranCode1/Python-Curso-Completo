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

# Conectamos (se crea el archivo si no existe)
conn = sqlite3.connect("clase44.db")
cursor = conn.cursor()

# ============================================================
# 1. Crear tabla "usuarios"
# ============================================================
# Consigna: Crea una tabla "usuarios" con id, nombre, edad y email.
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    email TEXT UNIQUE
)
""")
conn.commit()
print("Ejercicio 1: Tabla 'usuarios' creada.")

# ============================================================
# 2. Insertar registros
# ============================================================
# Consigna: Inserta 3 usuarios en la tabla.
usuarios = [
    ("Ana", 25, "ana@example.com"),
    ("Luis", 30, "luis@example.com"),
    ("Maria", 22, "maria@example.com")
]
cursor.executemany("INSERT OR IGNORE INTO usuarios (nombre, edad, email) VALUES (?, ?, ?)", usuarios)
conn.commit()
print("Ejercicio 2: Datos insertados en 'usuarios'.")

# ============================================================
# 3. Consultar todos los usuarios
# ============================================================
# Consigna: Muestra todos los registros de la tabla usuarios.
print("\nEjercicio 3: Todos los usuarios")
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

# ============================================================
# 4. Consultar con condición
# ============================================================
# Consigna: Muestra los usuarios mayores de 24 años.
print("\nEjercicio 4: Usuarios mayores de 24 años")
cursor.execute("SELECT nombre, edad FROM usuarios WHERE edad > 24")
for fila in cursor.fetchall():
    print(fila)

# ============================================================
# 5. Actualizar datos
# ============================================================
# Consigna: Cambia la edad de Ana a 26.
cursor.execute("UPDATE usuarios SET edad = 26 WHERE nombre = 'Ana'")
conn.commit()
print("\nEjercicio 5: Edad de Ana actualizada.")

# ============================================================
# 6. Eliminar registros
# ============================================================
# Consigna: Elimina al usuario con nombre 'Luis'.
cursor.execute("DELETE FROM usuarios WHERE nombre = 'Luis'")
conn.commit()
print("Ejercicio 6: Usuario 'Luis' eliminado.")

# ============================================================
# 7. Consultar con ordenamiento
# ============================================================
# Consigna: Muestra los usuarios ordenados por edad de menor a mayor.
print("\nEjercicio 7: Usuarios ordenados por edad")
cursor.execute("SELECT nombre, edad FROM usuarios ORDER BY edad ASC")
for fila in cursor.fetchall():
    print(fila)

# ============================================================
# 8. Uso de funciones de agregación
# ============================================================
# Consigna: Calcula la edad promedio de los usuarios.
print("\nEjercicio 8: Edad promedio")
cursor.execute("SELECT AVG(edad) FROM usuarios")
print("Promedio de edad:", cursor.fetchone()[0])

# ============================================================
# 9. Crear tabla relacionada
# ============================================================
# Consigna: Crea una tabla "ordenes" relacionada con usuarios (FK).
cursor.execute("""
CREATE TABLE IF NOT EXISTS ordenes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto TEXT NOT NULL,
    cantidad INTEGER,
    usuario_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
""")
conn.commit()
print("\nEjercicio 9: Tabla 'ordenes' creada.")

# Insertamos órdenes
ordenes = [
    ("Laptop", 1, 1),   # Ana
    ("Celular", 2, 3)   # Maria
]
cursor.executemany("INSERT INTO ordenes (producto, cantidad, usuario_id) VALUES (?, ?, ?)", ordenes)
conn.commit()

# ============================================================
# 10. JOIN entre tablas
# ============================================================
# Consigna: Muestra el nombre de los usuarios junto con sus órdenes.
print("\nEjercicio 10: JOIN usuarios y ordenes")
cursor.execute("""
SELECT usuarios.nombre, ordenes.producto, ordenes.cantidad
FROM usuarios
JOIN ordenes ON usuarios.id = ordenes.usuario_id
""")
for fila in cursor.fetchall():
    print(fila)

# Cerramos conexión
conn.close()
print("\nConexión cerrada.")

# ============================================================
# CONCLUSIÓN:
# - Aprendimos a crear tablas, insertar, consultar, actualizar, eliminar.
# - Usamos ordenamiento, funciones de agregación y relaciones entre tablas.
# - sqlite3 es ideal para bases de datos ligeras en archivos.
# ============================================================
