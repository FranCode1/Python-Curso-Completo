# =====================================================================
# 📘 Clase 39: Diferencias entre Asincronismo, Hilos y Procesos
# =====================================================================
# En Python existen 3 formas principales de manejar tareas concurrentes:
# 1. Asincronismo (async/await, asyncio)
# 2. Multithreading (hilos)
# 3. Multiprocessing (procesos)
#
# Cada una tiene ventajas y desventajas:
# - async/await → I/O no bloqueante, un solo hilo, muy eficiente en conexiones
# - threading   → I/O bloqueante, varios hilos, limitado por el GIL
# - multiprocessing → CPU intensivo, varios procesos, aprovecha múltiples núcleos
#
# Regla rápida:
# - async: muchas conexiones, I/O no bloqueante
# - threads: I/O bloqueante, pero varias tareas
# - multiprocessing: cálculos pesados en CPU
# =====================================================================

import asyncio
import threading
import multiprocessing
import time


# ---------------------------------------------------------------------
# 🔹 1. Asincronismo (async/await)
# ---------------------------------------------------------------------
async def tarea_async(nombre, segundos):
    print(f"[ASYNC] {nombre} empieza")
    await asyncio.sleep(segundos)  # Simula espera I/O
    print(f"[ASYNC] {nombre} termina")

async def ejemplo_async():
    await asyncio.gather(
        tarea_async("A", 2),
        tarea_async("B", 3),
        tarea_async("C", 1)
    )


# ---------------------------------------------------------------------
# 🔹 2. Multithreading (hilos)
# ---------------------------------------------------------------------
def tarea_hilo(nombre, segundos):
    print(f"[THREAD] {nombre} empieza")
    time.sleep(segundos)  # Simula espera bloqueante
    print(f"[THREAD] {nombre} termina")

def ejemplo_threads():
    hilos = []
    for i in range(3):
        t = threading.Thread(target=tarea_hilo, args=(f"Hilo {i+1}", 2))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()


# ---------------------------------------------------------------------
# 🔹 3. Multiprocessing (procesos)
# ---------------------------------------------------------------------
def tarea_proceso(nombre, segundos):
    print(f"[PROC] {nombre} empieza")
    time.sleep(segundos)  # Simula cálculo pesado
    print(f"[PROC] {nombre} termina")

def ejemplo_procesos():
    procesos = []
    for i in range(3):
        p = multiprocessing.Process(target=tarea_proceso, args=(f"Proceso {i+1}", 2))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()


# ---------------------------------------------------------------------
# 🔹 Comparación en ejecución
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("\n=== Ejemplo con Asincronismo ===")
    asyncio.run(ejemplo_async())

    print("\n=== Ejemplo con Threads ===")
    ejemplo_threads()

    print("\n=== Ejemplo con Procesos ===")
    ejemplo_procesos()

# =====================================================================
# Observaciones:
# - Async usa un solo hilo, pero cambia de tarea cuando hay espera I/O.
# - Threads ejecutan varias tareas en paralelo, pero comparten memoria.
# - Procesos ejecutan realmente en paralelo (aprovechan varios núcleos).
# =====================================================================
