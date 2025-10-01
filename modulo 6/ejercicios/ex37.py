# ============================================================
# CLASE 38: MULTIPROCESAMIENTO CON MULTIPROCESSING - EJERCICIOS
# ============================================================

import multiprocessing
import time
import os
import math

# ------------------------------------------------------------
# EJERCICIO 1: Crear dos procesos que impriman mensajes
# ------------------------------------------------------------
def proceso_simple(nombre):
    print(f"👷 Proceso {nombre} ejecutándose en PID {os.getpid()}")
    time.sleep(1)
    print(f"✅ Proceso {nombre} terminado")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=proceso_simple, args=("A",))
    p2 = multiprocessing.Process(target=proceso_simple, args=("B",))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("✅ Ejercicio 1 completado\n")

# ------------------------------------------------------------
# EJERCICIO 2: Ejecutar una lista de números al cuadrado con Pool
# ------------------------------------------------------------
def cuadrado(n):
    print(f"🔢 Calculando {n}^2 en PID {os.getpid()}")
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(processes=3) as pool:
        numeros = [1, 2, 3, 4, 5]
        resultados = pool.map(cuadrado, numeros)
        print("Resultados:", resultados)
        print("✅ Ejercicio 2 completado\n")

# ------------------------------------------------------------
# EJERCICIO 3: Calcular factoriales con Pool
# ------------------------------------------------------------
def factorial(n):
    print(f"🧮 Calculando factorial({n}) en PID {os.getpid()}")
    return math.factorial(n)

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        numeros = [5, 7, 10, 12]
        resultados = pool.map(factorial, numeros)
        print("Factoriales:", resultados)
        print("✅ Ejercicio 3 completado\n")

# ------------------------------------------------------------
# EJERCICIO 4: Comunicación entre procesos con Queue
# ------------------------------------------------------------
def productor(queue):
    for i in range(5):
        print(f"📤 Produciendo {i}")
        queue.put(i)
        time.sleep(0.3)

def consumidor(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"📥 Consumido {item}")

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=productor, args=(q,))
    p2 = multiprocessing.Process(target=consumidor, args=(q,))

    p1.start()
    p2.start()
    p1.join()
    q.put(None)
    p2.join()
    print("✅ Ejercicio 4 completado\n")

# ------------------------------------------------------------
# EJERCICIO 5: Comparar ejecución secuencial vs multiproceso
# ------------------------------------------------------------
def tarea_pesada(n):
    suma = 0
    for i in range(1, n):
        suma += i * i
    return suma

if __name__ == "__main__":
    N = 5_000_00

    inicio = time.time()
    [tarea_pesada(N) for _ in range(4)]
    fin = time.time()
    print("⏱️ Tiempo secuencial:", fin - inicio)

    inicio = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(tarea_pesada, [N]*4)
    fin = time.time()
    print("⚡ Tiempo multiprocessing:", fin - inicio)
    print("✅ Ejercicio 5 completado\n")

# ------------------------------------------------------------
# EJERCICIO 6: Usar Pipe para comunicación entre procesos
# ------------------------------------------------------------
def enviar(conexion):
    conexion.send("Hola desde el proceso hijo 👋")
    conexion.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=enviar, args=(child_conn,))
    p.start()
    print("📨 Mensaje recibido:", parent_conn.recv())
    p.join()
    print("✅ Ejercicio 6 completado\n")

# ------------------------------------------------------------
# EJERCICIO 7: Contar números pares en paralelo
# ------------------------------------------------------------
def contar_pares(lista, queue):
    total = sum(1 for x in lista if x % 2 == 0)
    queue.put(total)

if __name__ == "__main__":
    lista = list(range(1, 1_000_01))
    mitad = len(lista) // 2
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=contar_pares, args=(lista[:mitad], q))
    p2 = multiprocessing.Process(target=contar_pares, args=(lista[mitad:], q))

    p1.start(); p2.start()
    p1.join(); p2.join()

    total = q.get() + q.get()
    print("🔢 Cantidad de pares:", total)
    print("✅ Ejercicio 7 completado\n")

# ------------------------------------------------------------
# EJERCICIO 8: Multiprocessing con argumentos múltiples
# ------------------------------------------------------------
def potencia(base, exp):
    print(f"{base}^{exp} en PID {os.getpid()}")
    return base ** exp

if __name__ == "__main__":
    datos = [(2, 5), (3, 4), (5, 3), (10, 2)]
    with multiprocessing.Pool(processes=2) as pool:
        resultados = pool.starmap(potencia, datos)
        print("Potencias:", resultados)
        print("✅ Ejercicio 8 completado\n")

# ------------------------------------------------------------
# EJERCICIO 9: Simulación de descargas en paralelo
# ------------------------------------------------------------
def descargar_archivo(nombre, tiempo):
    print(f"📥 Descargando {nombre} en PID {os.getpid()}")
    time.sleep(tiempo)
    print(f"✅ {nombre} descargado en {tiempo}s")

if __name__ == "__main__":
    archivos = [("video.mp4", 3), ("foto.png", 2), ("musica.mp3", 1)]
    procesos = [multiprocessing.Process(target=descargar_archivo, args=(n, t)) for n, t in archivos]

    for p in procesos: p.start()
    for p in procesos: p.join()
    print("✅ Ejercicio 9 completado\n")

# ------------------------------------------------------------
# EJERCICIO 10: Mini proyecto - Calcular suma de cuadrados en paralelo
# ------------------------------------------------------------
def suma_cuadrados(lista, queue):
    total = sum(x*x for x in lista)
    queue.put(total)

if __name__ == "__main__":
    lista = list(range(1, 500_001))
    mitad = len(lista) // 2
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=suma_cuadrados, args=(lista[:mitad], q))
    p2 = multiprocessing.Process(target=suma_cuadrados, args=(lista[mitad:], q))

    inicio = time.time()
    p1.start(); p2.start()
    p1.join(); p2.join()

    total = q.get() + q.get()
    fin = time.time()

    print(f"🔢 Suma de cuadrados: {total}")
    print(f"⏱️ Tiempo total: {fin - inicio:.4f} segundos")
    print("✅ Ejercicio 10 completado\n")

# ============================================================
# FIN DE LOS EJERCICIOS
# ============================================================
