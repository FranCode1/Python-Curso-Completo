# ----------------------------------------
# CLASE 38: MULTIPROCESAMIENTO CON MULTIPROCESSING
# ----------------------------------------

# 📌 Recordatorio:
# - Los hilos (threading) comparten la misma memoria → pueden tener condiciones de carrera.
# - Los procesos (multiprocessing) son independientes → cada proceso tiene su propia memoria.
# - Multiprocessing aprovecha varios núcleos del CPU → ideal para tareas pesadas de cálculo.
# - Conceptos clave: Process, Pool, Queue.

import multiprocessing
import time
import os


# ==========================
# 🔹 CREANDO UN PROCESO BÁSICO
# ==========================

def worker(nombre):
    print(f"👷 Proceso {nombre} ejecutándose en PID {os.getpid()}")
    time.sleep(2)
    print(f"✅ Proceso {nombre} terminado")

if __name__ == "__main__":
    proceso1 = multiprocessing.Process(target=worker, args=("A",))
    proceso2 = multiprocessing.Process(target=worker, args=("B",))

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

    print("✅ Procesos básicos terminados\n")


# ==========================
# 🔹 USANDO POOL PARALELAMENTE
# ==========================

def cuadrado(n):
    print(f"🔢 Calculando {n}^2 en PID {os.getpid()}")
    time.sleep(1)
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        numeros = [1, 2, 3, 4, 5]
        resultados = pool.map(cuadrado, numeros)
        print("Resultados:", resultados, "\n")


# ==========================
# 🔹 USANDO QUEUE PARA COMUNICACIÓN ENTRE PROCESOS
# ==========================

def productor(queue):
    for i in range(5):
        print(f"📤 Enviando {i}")
        queue.put(i)
        time.sleep(0.5)

def consumidor(queue):
    while True:
        item = queue.get()
        if item is None:  # señal de finalización
            break
        print(f"📥 Recibido {item}")

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=productor, args=(queue,))
    p2 = multiprocessing.Process(target=consumidor, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    queue.put(None)  # señal para terminar consumidor
    p2.join()

    print("✅ Comunicación con Queue finalizada\n")


# ==========================
# 🔹 COMPARACIÓN HILOS VS PROCESOS
# ==========================

# - Hilos:
#   ✔️ Ligeros, comparten memoria
#   ✔️ Buenos para tareas de I/O (espera en archivos/red)
#   ❌ Limitados por el GIL en Python (solo un hilo ejecuta bytecode a la vez)

# - Procesos:
#   ✔️ Ejecutan en paralelo real en múltiples núcleos
#   ✔️ Ideales para tareas intensivas en CPU (cálculos grandes)
#   ❌ Más pesados, no comparten memoria directamente (hay que usar Queue, Pipe, etc.)


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Calcular la suma de cuadrados de una lista muy grande usando multiprocessing

def suma_cuadrados(numeros, queue):
    total = sum(x*x for x in numeros)
    queue.put(total)

if __name__ == "__main__":
    lista = list(range(1, 1_000_01))
    mitad = len(lista) // 2

    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=suma_cuadrados, args=(lista[:mitad], queue))
    p2 = multiprocessing.Process(target=suma_cuadrados, args=(lista[mitad:], queue))

    inicio = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    total = queue.get() + queue.get()
    fin = time.time()

    print(f"🔢 Suma de cuadrados: {total}")
    print(f"⏱️ Tiempo total con multiprocessing: {fin - inicio:.4f} segundos")


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es el multiprocesamiento y cómo usar multiprocessing.Process
# - Cómo trabajar con Pool para ejecutar funciones en paralelo
# - Cómo comunicar procesos con Queue
# - Diferencias entre hilos y procesos en Python
# - Mini proyecto: cálculo en paralelo de suma de cuadrados
#
# Próxima clase: Programación funcional en Python (funciones puras, functools, reduce, etc).
