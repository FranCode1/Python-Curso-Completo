"""
Proyecto Módulo 6: Descargador y Procesador de Datos Concurrente
Demostración de asincronismo, hilos y procesos.
"""

import asyncio
import time
import threading
import multiprocessing
import requests
from queue import Queue

URLS = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3",
    "https://jsonplaceholder.typicode.com/todos/4",
    "https://jsonplaceholder.typicode.com/todos/5",
]


# --------------------------
# Simulación de descarga
# --------------------------
def descargar(url):
    """Descarga datos de una URL simulando operación de I/O."""
    resp = requests.get(url)
    return resp.json()


# --------------------------
# Procesamiento simulado
# --------------------------
def procesar(data):
    """Simula un cálculo pesado sobre los datos."""
    total = sum(ord(c) for c in str(data))  # Convierte a números y suma
    return total


# --------------------------
# Versión Asíncrona (asyncio)
# --------------------------
async def descargar_async(session, url):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, descargar, url)


async def main_async():
    import aiohttp
    async with aiohttp.ClientSession() as session:
        tareas = [descargar_async(session, url) for url in URLS]
        resultados = await asyncio.gather(*tareas)
        procesados = [procesar(r) for r in resultados]
        return procesados


# --------------------------
# Versión con Threads
# --------------------------
def worker_thread(url, queue):
    data = descargar(url)
    resultado = procesar(data)
    queue.put(resultado)


def main_threads():
    q = Queue()
    threads = []
    for url in URLS:
        t = threading.Thread(target=worker_thread, args=(url, q))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    resultados = []
    while not q.empty():
        resultados.append(q.get())
    return resultados


# --------------------------
# Versión con Multiprocessing
# --------------------------
def worker_process(url):
    data = descargar(url)
    return procesar(data)


def main_processes():
    with multiprocessing.Pool(processes=4) as pool:
        resultados = pool.map(worker_process, URLS)
    return resultados


# --------------------------
# Comparación de tiempos
# --------------------------
def comparar():
    print("⚡ Comparando técnicas de concurrencia\n")

    # Asyncio
    inicio = time.time()
    resultados_async = asyncio.run(main_async())
    print("Asyncio:", resultados_async, f"⏱ {time.time() - inicio:.2f}s")

    # Threads
    inicio = time.time()
    resultados_threads = main_threads()
    print("Threads:", resultados_threads, f"⏱ {time.time() - inicio:.2f}s")

    # Processes
    inicio = time.time()
    resultados_proc = main_processes()
    print("Processes:", resultados_proc, f"⏱ {time.time() - inicio:.2f}s")


if __name__ == "__main__":
    comparar()
