# =====================================================================
# 📘 CLASE 39: Casos de uso prácticos
# =====================================================================
# En esta clase veremos CUÁNDO conviene usar cada técnica:
#
# 🔹 Asincronismo (async/await, asyncio)
#   - Ideal para operaciones I/O no bloqueantes:
#     * Peticiones HTTP (scraping, APIs)
#     * Leer/escribir sockets
#     * Muchas conexiones simultáneas
#
# 🔹 Multithreading (threading)
#   - Ideal para operaciones I/O bloqueantes:
#     * Lectura/escritura de archivos
#     * Descargas que usan librerías bloqueantes
#     * Interacción con dispositivos (teclado, cámaras)
#
# 🔹 Multiprocessing (multiprocessing)
#   - Ideal para tareas CPU-intensivas:
#     * Procesamiento de imágenes
#     * Cálculos matemáticos grandes
#     * Entrenamiento de modelos de ML
#
# =====================================================================

import asyncio
import threading
import multiprocessing
import time
import random

# ---------------------------------------------------------------------
# 🔹 Ejemplo 1: Operaciones I/O con ASYNCIO
# ---------------------------------------------------------------------
# Simulamos scraping de páginas web con asyncio.
# Cada "descarga" es solo un sleep con tiempo aleatorio.
# ---------------------------------------------------------------------

async def descargar_pagina(nombre):
    print(f"[ASYNC] Descargando {nombre}...")
    await asyncio.sleep(random.uniform(1, 3))  # Simula espera de red
    print(f"[ASYNC] {nombre} descargada")

async def scraping_async():
    await asyncio.gather(
        descargar_pagina("Página 1"),
        descargar_pagina("Página 2"),
        descargar_pagina("Página 3"),
    )


# ---------------------------------------------------------------------
# 🔹 Ejemplo 2: Operaciones I/O bloqueantes con THREADS
# ---------------------------------------------------------------------
# Simulamos lectura/escritura en disco con time.sleep
# Usamos threads para que varias tareas ocurran "en paralelo".
# ---------------------------------------------------------------------

def escribir_archivo(nombre):
    print(f"[THREAD] Escribiendo en {nombre}...")
    time.sleep(random.uniform(1, 3))  # Simula operación de disco lenta
    print(f"[THREAD] {nombre} listo")

def operaciones_disco_threads():
    hilos = []
    for i in range(3):
        t = threading.Thread(target=escribir_archivo, args=(f"Archivo_{i+1}.txt",))
        hilos.append(t)
        t.start()

    for t in hilos:
        t.join()


# ---------------------------------------------------------------------
# 🔹 Ejemplo 3: Tareas CPU intensivas con MULTIPROCESSING
# ---------------------------------------------------------------------
# Simulamos cálculos pesados (sumatoria de muchos números).
# ---------------------------------------------------------------------

def calcular_suma(nombre, n):
    print(f"[PROC] {nombre} calculando...")
    total = sum(i * i for i in range(n))  # Tarea CPU-intensiva
    print(f"[PROC] {nombre} completado: {total}")

def calculos_pesados_processes():
    procesos = []
    for i in range(3):
        p = multiprocessing.Process(target=calcular_suma, args=(f"Proceso {i+1}", 5_000_000))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()


# ---------------------------------------------------------------------
# 🔹 Comparación práctica
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("\n=== Scraping con ASYNCIO (I/O no bloqueante) ===")
    inicio = time.time()
    asyncio.run(scraping_async())
    print(f"⏱️ Tiempo total (async): {time.time() - inicio:.2f} seg\n")

    print("=== Operaciones de disco con THREADS (I/O bloqueante) ===")
    inicio = time.time()
    operaciones_disco_threads()
    print(f"⏱️ Tiempo total (threads): {time.time() - inicio:.2f} seg\n")

    print("=== Cálculos pesados con PROCESOS (CPU intensivo) ===")
    inicio = time.time()
    calculos_pesados_processes()
    print(f"⏱️ Tiempo total (procesos): {time.time() - inicio:.2f} seg\n")


# =====================================================================
# 📌 Conclusiones:
# - ASYNCIO: ideal para miles de tareas I/O simultáneas (ej. scraping web masivo).
# - THREADS: útil con I/O bloqueante (archivos, cámaras, dispositivos).
# - PROCESSES: mejor opción para cálculos pesados y aprovechar múltiples núcleos.
# =====================================================================
