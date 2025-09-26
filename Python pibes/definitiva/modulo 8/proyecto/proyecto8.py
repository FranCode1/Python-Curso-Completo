# 🏁 Proyecto Final – Gestor de Tareas Avanzado (CLI + API local)

# 📌 Objetivo:
# Construir un **gestor de tareas avanzado** con:

# * **Clases y POO** para representar tareas y el gestor.
# * **Persistencia en SQLite** y exportación a JSON/CSV.
# * **Manejo de errores** robusto.
# * **Pruebas unitarias y con pytest**.
# * **Automatización con scripts**.
# * **Asincronismo** (ejemplo: recordatorios de tareas con `asyncio`).
# * **Organización en módulos**.
# * **Buenas prácticas (PEP8, docstrings, modularidad, Git)**.

# ---

# ## 📂 Estructura de archivos

# ```
# proyecto_final/
# │── gestor/
# │   │── __init__.py
# │   │── models.py        # Clases (Tarea, Gestor)
# │   │── db.py            # Manejo de SQLite
# │   │── utils.py         # Exportar JSON/CSV, logs, helpers
# │   │── async_reminder.py # Recordatorios asincrónicos
# │── tests/
# │   │── test_models.py
# │   │── test_db.py
# │── main.py              # Script CLI
# │── requirements.txt
# │── README.md
# ```
