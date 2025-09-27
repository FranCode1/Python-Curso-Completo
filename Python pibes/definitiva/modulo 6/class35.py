# ----------------------------------------
# CLASE 36: PROGRAMACIÓN ASÍNCRONA (ASYNC, AWAIT, ASYNCIO)
# ----------------------------------------

# 📌 Recordatorio:
# - La programación asíncrona permite ejecutar múltiples tareas concurrentemente
#   sin bloquear el programa.
# - Se usa principalmente para operaciones de I/O (lectura de archivos, red, APIs).
# - Palabras clave: `async`, `await`.
# - Módulo principal: `asyncio`.

import asyncio
import time


# ==========================
# 🔹 FUNCIÓN ASÍNCRONA BÁSICA
# ==========================

async def saludar():
    print("Hola...")
    await asyncio.sleep(1)  # simula una operación que tarda
    print("...Mundo!")

# Para ejecutar una corrutina se necesita un loop de asyncio
asyncio.run(saludar())


# ==========================
# 🔹 VARIAS TAREAS CONCURRENTES
# ==========================

async def tarea(nombre, duracion):
    print(f"⏳ Iniciando tarea {nombre}")
    await asyncio.sleep(duracion)
    print(f"✅ Tarea {nombre} completada")

async def main():
    # Ejecutar tareas al mismo tiempo
    await asyncio.gather(
        tarea("A", 2),
        tarea("B", 1),
        tarea("C", 3),
    )

asyncio.run(main())


# ==========================
# 🔹 CREAR Y ESPERAR TAREAS
# ==========================

async def ejemplo_task():
    print("Iniciando tarea con create_task...")
    await asyncio.sleep(2)
    print("Terminó tarea con create_task")

async def main_tasks():
    task = asyncio.create_task(ejemplo_task())
    print("➡ Task creada, sigue el programa...")
    await task

asyncio.run(main_tasks())


# ==========================
# 🔹 COMBINAR CÓDIGO SINCRÓNICO Y ASÍNCRONO
# ==========================

async def esperar_y_sumar(a, b):
    print(f"Sumando {a} + {b} ...")
    await asyncio.sleep(1)
    return a + b

async def operaciones():
    resultado = await esperar_y_sumar(5, 7)
    print(f"Resultado: {resultado}")

asyncio.run(operaciones())


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Descargar datos simulados de múltiples URLs de forma concurrente

async def descargar(url, tiempo):
    print(f"📥 Descargando {url} ...")
    await asyncio.sleep(tiempo)
    print(f"✅ {url} descargado en {tiempo}s")
    return f"Datos de {url}"

async def gestor_descargas():
    urls = [
        ("https://api1.com/data", 2),
        ("https://api2.com/data", 3),
        ("https://api3.com/data", 1),
    ]
    resultados = await asyncio.gather(*(descargar(url, t) for url, t in urls))
    print("Resultados:", resultados)

asyncio.run(gestor_descargas())


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es la programación asíncrona y cuándo usarla
# - Uso de async, await y asyncio.run
# - Crear y ejecutar múltiples tareas concurrentes
# - Uso de asyncio.gather y create_task
# - Mini proyecto: simulación de descargas concurrentes
#
# Próxima clase: Concurrencia y Multiprocessing en Python (threading, multiprocessing).
