# =====================================================================
# 📘 CLASE 39: Casos de uso prácticos
# =====================================================================
# Este archivo contiene 10 ejercicios resueltos con consignas
# sobre CUÁNDO conviene usar Asyncio, Threads o Multiprocessing.
# =====================================================================

import asyncio
import threading
import multiprocessing
import time
import random
import os

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 1: Scraping con asyncio
# Consigna: Simular la descarga de 5 páginas web en paralelo usando async.
# ---------------------------------------------------------------------
async def descargar_pagina(nombre):
    print(f"[ASYNC] Descargando {nombre}...")
    await asyncio.sleep(random.uniform(1, 3))
    print(f"[ASYNC] {nombre} descargada")

async def ejercicio1():
    await asyncio.gather(*(descargar_pagina(f"Página {i+1}") for i in range(5)))


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 2: Consultas a API con asyncio
# Consigna: Simular 3 peticiones a API con tiempos de respuesta distintos.
# ---------------------------------------------------------------------
async def consulta_api(nombre, segundos):
    print(f"[API] {nombre} iniciada")
    await asyncio.sleep(segundos)
    print(f"[API] {nombre} completada en {segundos}s")

async def ejercicio2():
    await asyncio.gather(
        consulta_api("API Usuarios", 2),
        consulta_api("API Productos", 3),
        consulta_api("API Ventas", 1),
    )


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 3: Operaciones de disco con Threads
# Consigna: Simular la escritura de 3 archivos en paralelo usando hilos.
# ---------------------------------------------------------------------
def escribir_archivo(nombre):
    print(f"[THREAD] Escribiendo en {nombre}...")
    time.sleep(random.uniform(1, 3))
    print(f"[THREAD] {nombre} listo")

def ejercicio3():
    hilos = []
    for i in range(3):
        t = threading.Thread(target=escribir_archivo, args=(f"Archivo_{i+1}.txt",))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 4: Lectura de sensores con Threads
# Consigna: Simular lectura de 4 sensores en paralelo con threads.
# ---------------------------------------------------------------------
def leer_sensor(nombre):
    print(f"[SENSOR] {nombre} leyendo...")
    time.sleep(random.uniform(1, 2))
    print(f"[SENSOR] {nombre} valor recibido")

def ejercicio4():
    hilos = []
    for i in range(4):
        t = threading.Thread(target=leer_sensor, args=(f"Sensor {i+1}",))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 5: Cálculo pesado con procesos
# Consigna: Calcular la suma de cuadrados de 10 millones de números.
# ---------------------------------------------------------------------
def calcular_suma(nombre, n):
    print(f"[PROC {os.getpid()}] {nombre} calculando...")
    total = sum(i * i for i in range(n))
    print(f"[PROC {os.getpid()}] {nombre} completado: {total}")

def ejercicio5():
    procesos = []
    for i in range(2):  # 2 procesos
        p = multiprocessing.Process(target=calcular_suma, args=(f"Proceso {i+1}", 10_000_000))
        procesos.append(p)
        p.start()
    for p in procesos:
        p.join()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 6: Procesamiento de imágenes simulado con procesos
# Consigna: Procesar 3 "imágenes" en paralelo con multiprocessing.
# ---------------------------------------------------------------------
def procesar_imagen(nombre):
    print(f"[PROC {os.getpid()}] Procesando {nombre}...")
    time.sleep(2)
    print(f"[PROC {os.getpid()}] {nombre} lista")

def ejercicio6():
    procesos = []
    for i in range(3):
        p = multiprocessing.Process(target=procesar_imagen, args=(f"Imagen_{i+1}.jpg",))
        procesos.append(p)
        p.start()
    for p in procesos:
        p.join()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 7: Comparar tiempos entre async y threads
# Consigna: Ejecutar 5 tareas de espera y medir tiempo en async y threads.
# ---------------------------------------------------------------------
async def tarea_async_tiempo(i):
    await asyncio.sleep(1)

def tarea_thread_tiempo(i):
    time.sleep(1)

async def ejercicio7_async():
    inicio = time.time()
    await asyncio.gather(*(tarea_async_tiempo(i) for i in range(5)))
    print("⏱️ Tiempo total (async):", time.time() - inicio, "s")

def ejercicio7_threads():
    inicio = time.time()
    hilos = []
    for i in range(5):
        t = threading.Thread(target=tarea_thread_tiempo, args=(i,))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()
    print("⏱️ Tiempo total (threads):", time.time() - inicio, "s")


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 8: Clase personalizada de Thread
# Consigna: Crear una clase que herede de Thread y simule tarea de backup.
# ---------------------------------------------------------------------
class BackupThread(threading.Thread):
    def __init__(self, archivo):
        super().__init__()
        self.archivo = archivo

    def run(self):
        print(f"[BACKUP] Copiando {self.archivo}...")
        time.sleep(2)
        print(f"[BACKUP] {self.archivo} copiado con éxito")

def ejercicio8():
    h = BackupThread("base_datos.db")
    h.start()
    h.join()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 9: Comunicación entre procesos
# Consigna: Usar multiprocessing.Queue para enviar datos entre procesos.
# ---------------------------------------------------------------------
def productor(q):
    for i in range(3):
        print(f"[Productor] enviando {i}")
        q.put(i)
        time.sleep(1)

def consumidor(q):
    while True:
        valor = q.get()
        print(f"[Consumidor] recibió {valor}")
        if valor == -1:
            break

def ejercicio9():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=productor, args=(q,))
    p2 = multiprocessing.Process(target=consumidor, args=(q,))
    p1.start(); p2.start()
    p1.join()
    q.put(-1)
    p2.join()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 10: Mezcla de async + threads + procesos
# Consigna: Ejecutar al mismo tiempo:
# - Una tarea async
# - Una tarea en un thread
# - Una tarea en un proceso
# ---------------------------------------------------------------------
async def tarea_async_mix():
    await asyncio.sleep(1)
    print("[MIX] Async completada")

def tarea_thread_mix():
    time.sleep(2)
    print("[MIX] Thread completada")

def tarea_proceso_mix():
    time.sleep(3)
    print("[MIX] Proceso completado")

def ejercicio10():
    loop = asyncio.get_event_loop()
    hilo = threading.Thread(target=tarea_thread_mix)
    proceso = multiprocessing.Process(target=tarea_proceso_mix)

    hilo.start()
    proceso.start()
    loop.run_until_complete(tarea_async_mix())

    hilo.join()
    proceso.join()


# ---------------------------------------------------------------------
# 🚀 MAIN
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("\n=== Ejercicio 1: Scraping con asyncio ===")
    asyncio.run(ejercicio1())

    print("\n=== Ejercicio 2: Consultas a API con asyncio ===")
    asyncio.run(ejercicio2())

    print("\n=== Ejercicio 3: Escritura de archivos con Threads ===")
    ejercicio3()

    print("\n=== Ejercicio 4: Lectura de sensores con Threads ===")
    ejercicio4()

    print("\n=== Ejercicio 5: Cálculo pesado con Procesos ===")
    ejercicio5()

    print("\n=== Ejercicio 6: Procesamiento de imágenes con Procesos ===")
    ejercicio6()

    print("\n=== Ejercicio 7: Comparación tiempos ===")
    asyncio.run(ejercicio7_async())
    ejercicio7_threads()

    print("\n=== Ejercicio 8: Clase personalizada de Thread ===")
    ejercicio8()

    print("\n=== Ejercicio 9: Comunicación entre procesos ===")
    ejercicio9()

    print("\n=== Ejercicio 10: Async + Threads + Procesos ===")
    ejercicio10()
