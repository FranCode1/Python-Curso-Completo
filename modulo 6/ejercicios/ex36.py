# ============================================================
# CLASE 37: CONCURRENCIA CON THREADING - EJERCICIOS RESUELTOS
# ============================================================

import threading
import time
import random

# ------------------------------------------------------------
# EJERCICIO 1: Crear dos hilos que impriman mensajes con delay
# ------------------------------------------------------------
def imprimir_mensaje(mensaje, delay):
    time.sleep(delay)
    print(mensaje)

hilo1 = threading.Thread(target=imprimir_mensaje, args=("Hola desde el hilo 1", 2))
hilo2 = threading.Thread(target=imprimir_mensaje, args=("Hola desde el hilo 2", 1))

hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()

print("✅ Ejercicio 1 completado\n")

# ------------------------------------------------------------
# EJERCICIO 2: Condición de carrera sin Lock
# ------------------------------------------------------------
contador = 0

def incrementar():
    global contador
    for _ in range(100000):
        contador += 1

h1 = threading.Thread(target=incrementar)
h2 = threading.Thread(target=incrementar)

h1.start()
h2.start()
h1.join()
h2.join()

print("Contador sin Lock:", contador)
print("✅ Ejercicio 2 completado\n")

# ------------------------------------------------------------
# EJERCICIO 3: Resolver la condición de carrera con Lock
# ------------------------------------------------------------
contador = 0
lock = threading.Lock()

def incrementar_seguro():
    global contador
    for _ in range(100000):
        with lock:
            contador += 1

h1 = threading.Thread(target=incrementar_seguro)
h2 = threading.Thread(target=incrementar_seguro)

h1.start()
h2.start()
h1.join()
h2.join()

print("Contador con Lock:", contador)
print("✅ Ejercicio 3 completado\n")

# ------------------------------------------------------------
# EJERCICIO 4: Simular descargas en paralelo
# ------------------------------------------------------------
def descargar_archivo(nombre, tiempo):
    print(f"📥 Descargando {nombre}...")
    time.sleep(tiempo)
    print(f"✅ {nombre} descargado en {tiempo}s")

archivos = [("archivo1.zip", 3), ("archivo2.zip", 2), ("archivo3.zip", 1)]
hilos = [threading.Thread(target=descargar_archivo, args=(n, t)) for n, t in archivos]

for h in hilos: h.start()
for h in hilos: h.join()

print("✅ Ejercicio 4 completado\n")

# ------------------------------------------------------------
# EJERCICIO 5: Temporizador con varios hilos
# ------------------------------------------------------------
def temporizador(nombre, segundos):
    print(f"⏳ {nombre} empezó ({segundos}s)")
    time.sleep(segundos)
    print(f"⌛ {nombre} terminó")

tareas = [("Timer1", 2), ("Timer2", 4), ("Timer3", 3)]
hilos = [threading.Thread(target=temporizador, args=(n, t)) for n, t in tareas]

for h in hilos: h.start()
for h in hilos: h.join()

print("✅ Ejercicio 5 completado\n")

# ------------------------------------------------------------
# EJERCICIO 6: Simulación de banco con Lock
# ------------------------------------------------------------
class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        self.lock = threading.Lock()

    def depositar(self, cantidad):
        with self.lock:
            saldo_anterior = self.saldo
            time.sleep(0.1)
            self.saldo = saldo_anterior + cantidad
            print(f"💰 Depositado {cantidad}, nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        with self.lock:
            if self.saldo >= cantidad:
                saldo_anterior = self.saldo
                time.sleep(0.1)
                self.saldo = saldo_anterior - cantidad
                print(f"🏧 Retirado {cantidad}, nuevo saldo: {self.saldo}")
            else:
                print("❌ Fondos insuficientes")

cuenta = CuentaBancaria(100)
hilos = [
    threading.Thread(target=cuenta.depositar, args=(50,)),
    threading.Thread(target=cuenta.retirar, args=(30,)),
    threading.Thread(target=cuenta.retirar, args=(150,))
]

for h in hilos: h.start()
for h in hilos: h.join()

print(f"Saldo final: {cuenta.saldo}")
print("✅ Ejercicio 6 completado\n")

# ------------------------------------------------------------
# EJERCICIO 7: Hilos con argumentos aleatorios
# ------------------------------------------------------------
def tarea_random(num):
    tiempo = random.randint(1, 3)
    print(f"Tarea {num} trabajando {tiempo}s")
    time.sleep(tiempo)
    print(f"Tarea {num} finalizada")

hilos = [threading.Thread(target=tarea_random, args=(i,)) for i in range(1, 6)]

for h in hilos: h.start()
for h in hilos: h.join()

print("✅ Ejercicio 7 completado\n")

# ------------------------------------------------------------
# EJERCICIO 8: Sumar números en paralelo con Lock
# ------------------------------------------------------------
suma_total = 0
lock = threading.Lock()

def sumar_rango(inicio, fin):
    global suma_total
    parcial = sum(range(inicio, fin))
    with lock:
        suma_total += parcial
    print(f"Suma parcial {inicio}-{fin}: {parcial}")

rangos = [(1, 10001), (10001, 20001), (20001, 30001)]
hilos = [threading.Thread(target=sumar_rango, args=r) for r in rangos]

for h in hilos: h.start()
for h in hilos: h.join()

print("Suma total:", suma_total)
print("✅ Ejercicio 8 completado\n")

# ------------------------------------------------------------
# EJERCICIO 9: Productor - Consumidor con Lock
# ------------------------------------------------------------
buffer = []
lock = threading.Lock()

def productor():
    for i in range(5):
        with lock:
            buffer.append(i)
            print(f"🍎 Producido: {i}")
        time.sleep(1)

def consumidor():
    for _ in range(5):
        time.sleep(2)
        with lock:
            if buffer:
                item = buffer.pop(0)
                print(f"🍽️ Consumido: {item}")

h1 = threading.Thread(target=productor)
h2 = threading.Thread(target=consumidor)

h1.start()
h2.start()
h1.join()
h2.join()

print("✅ Ejercicio 9 completado\n")

# ------------------------------------------------------------
# EJERCICIO 10: Simulación de tráfico con semáforo
# ------------------------------------------------------------
semaforo = threading.Semaphore(3)

def coche(nombre):
    with semaforo:
        print(f"🚗 {nombre} entrando al puente")
        time.sleep(2)
        print(f"🚗 {nombre} saliendo del puente")

hilos = [threading.Thread(target=coche, args=(f"Coche{i}",)) for i in range(1, 8)]

for h in hilos: h.start()
for h in hilos: h.join()

print("✅ Ejercicio 10 completado\n")

# ============================================================
# FIN DE LOS EJERCICIOS
# ============================================================
