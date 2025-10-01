# =====================================================================
# 📘 Clase 39: Diferencias entre Asincronismo, Hilos y Procesos
# =====================================================================
# Este archivo contiene 10 ejercicios resueltos con consignas
# sobre asincronismo, multithreading y multiprocessing en Python.
# =====================================================================

import asyncio
import threading
import multiprocessing
import time
import random
import os

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 1: Uso básico de asyncio
# Consigna: Crear 3 tareas asíncronas que impriman mensajes con delay.
# ---------------------------------------------------------------------
async def tarea_async(nombre, segundos):
    print(f"[ASYNC] {nombre} empieza")
    await asyncio.sleep(segundos)
    print(f"[ASYNC] {nombre} termina")

async def ejercicio1():
    await asyncio.gather(
        tarea_async("Tarea 1", 1),
        tarea_async("Tarea 2", 2),
        tarea_async("Tarea 3", 3),
    )

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 2: Async simulando descargas
# Consigna: Simular 3 descargas con tiempos diferentes usando async.
# ---------------------------------------------------------------------
async def descargar_archivo(nombre, segundos):
    print(f"[DESCARGA] {nombre} iniciada...")
    await asyncio.sleep(segundos)
    print(f"[DESCARGA] {nombre} completada en {segundos}s")

async def ejercicio2():
    await asyncio.gather(
        descargar_archivo("Archivo A", 2),
        descargar_archivo("Archivo B", 4),
        descargar_archivo("Archivo C", 1),
    )

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 3: Multithreading básico
# Consigna: Crear 3 hilos que esperen 2s cada uno.
# ---------------------------------------------------------------------
def tarea_hilo(nombre, segundos):
    print(f"[THREAD] {nombre} empieza")
    time.sleep(segundos)
    print(f"[THREAD] {nombre} termina")

def ejercicio3():
    hilos = []
    for i in range(3):
        t = threading.Thread(target=tarea_hilo, args=(f"Hilo {i+1}", 2))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 4: Threads simulando consultas a BD
# Consigna: Simular 5 consultas a BD en paralelo con hilos.
# ---------------------------------------------------------------------
def consulta_bd(nombre, segundos):
    print(f"[BD] {nombre} ejecutando consulta...")
    time.sleep(segundos)
    print(f"[BD] {nombre} terminó en {segundos}s")

def ejercicio4():
    hilos = []
    for i in range(5):
        segundos = random.randint(1, 3)
        t = threading.Thread(target=consulta_bd, args=(f"Consulta {i+1}", segundos))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 5: Multiprocessing básico
# Consigna: Crear 3 procesos que hagan una pausa de 2s.
# ---------------------------------------------------------------------
def tarea_proceso(nombre, segundos):
    print(f"[PROC {os.getpid()}] {nombre} empieza")
    time.sleep(segundos)
    print(f"[PROC {os.getpid()}] {nombre} termina")

def ejercicio5():
    procesos = []
    for i in range(3):
        p = multiprocessing.Process(target=tarea_proceso, args=(f"Proceso {i+1}", 2))
        procesos.append(p)
        p.start()
    for p in procesos:
        p.join()

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 6: Procesos para cálculos pesados
# Consigna: Calcular cuadrados de una lista en paralelo con procesos.
# ---------------------------------------------------------------------
def calcular_cuadrado(n):
    print(f"[PROC {os.getpid()}] calculando {n}^2")
    time.sleep(1)
    return n*n

def ejercicio6():
    with multiprocessing.Pool(processes=4) as pool:
        numeros = [1, 2, 3, 4, 5]
        resultados = pool.map(calcular_cuadrado, numeros)
        print("Resultados:", resultados)

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 7: Comparar tiempos entre async y threads
# Consigna: Ejecutar 5 tareas de espera con async y con threads y medir tiempo.
# ---------------------------------------------------------------------
async def tarea_async_tiempo(i):
    await asyncio.sleep(1)

def tarea_thread_tiempo(i):
    time.sleep(1)

async def ejercicio7_async():
    inicio = time.time()
    await asyncio.gather(*[tarea_async_tiempo(i) for i in range(5)])
    print("Async total:", time.time() - inicio, "segundos")

def ejercicio7_threads():
    inicio = time.time()
    hilos = []
    for i in range(5):
        t = threading.Thread(target=tarea_thread_tiempo, args=(i,))
        hilos.append(t)
        t.start()
    for t in hilos:
        t.join()
    print("Threads total:", time.time() - inicio, "segundos")

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 8: Herencia de hilos
# Consigna: Crear una clase que herede de Thread y ejecute una tarea.
# ---------------------------------------------------------------------
class MiHilo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        print(f"[MiHilo] {self.nombre} en ejecución...")
        time.sleep(2)
        print(f"[MiHilo] {self.nombre} terminó.")

def ejercicio8():
    h = MiHilo("Hilo personalizado")
    h.start()
    h.join()

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 9: Cola de procesos
# Consigna: Usar multiprocessing.Queue para comunicar procesos.
# ---------------------------------------------------------------------
def productor(q):
    for i in range(5):
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
    q.put(-1)  # señal de fin
    p2.join()

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 10: Async + Threads + Procesos juntos
# Consigna: Ejecutar 1 tarea async, 1 con hilo y 1 con proceso en paralelo.
# ---------------------------------------------------------------------
async def tarea_async_mix():
    await asyncio.sleep(1)
    print("[MIX] Async completado")

def tarea_thread_mix():
    time.sleep(2)
    print("[MIX] Thread completado")

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
    print("\n=== Ejercicio 1: Async básico ===")
    asyncio.run(ejercicio1())

    print("\n=== Ejercicio 2: Descargas async ===")
    asyncio.run(ejercicio2())

    print("\n=== Ejercicio 3: Threads básicos ===")
    ejercicio3()

    print("\n=== Ejercicio 4: Consultas BD con hilos ===")
    ejercicio4()

    print("\n=== Ejercicio 5: Procesos básicos ===")
    ejercicio5()

    print("\n=== Ejercicio 6: Cálculo paralelo con procesos ===")
    ejercicio6()

    print("\n=== Ejercicio 7: Comparación tiempos ===")
    asyncio.run(ejercicio7_async())
    ejercicio7_threads()

    print("\n=== Ejercicio 8: Clase heredada de Thread ===")
    ejercicio8()

    print("\n=== Ejercicio 9: Comunicación con cola de procesos ===")
    ejercicio9()

    print("\n=== Ejercicio 10: Async + Threads + Procesos ===")
    ejercicio10()
