# ----------------------------------------
# CLASE 37: CONCURRENCIA CON THREADING
# ----------------------------------------

# 📌 Recordatorio:
# - Concurrencia = ejecutar múltiples tareas al mismo tiempo (aparentemente).
# - En Python, los hilos se manejan con el módulo `threading`.
# - Útil para tareas que esperan mucho tiempo de I/O (descargas, lectura de archivos).
# - Problema: las condiciones de carrera, cuando varios hilos acceden a la misma variable.
# - Solución: usar `Lock` para sincronizar.

import threading
import time

# ==========================
# 🔹 CREANDO HILOS BÁSICOS
# ==========================

def imprimir_mensaje(mensaje, delay):
    time.sleep(delay)
    print(mensaje)

# Crear hilos
hilo1 = threading.Thread(target=imprimir_mensaje, args=("Hola desde el hilo 1", 2))
hilo2 = threading.Thread(target=imprimir_mensaje, args=("Hola desde el hilo 2", 1))

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar a que terminen
hilo1.join()
hilo2.join()

print("✅ Hilos terminados")


# ==========================
# 🔹 PROBLEMA: CONDICIONES DE CARRERA
# ==========================

contador = 0

def incrementar():
    global contador
    for _ in range(100000):
        contador += 1

# Dos hilos modificando la misma variable
hilo_a = threading.Thread(target=incrementar)
hilo_b = threading.Thread(target=incrementar)

hilo_a.start()
hilo_b.start()
hilo_a.join()
hilo_b.join()

print("Contador sin Lock:", contador)  # Resultado inesperado (condición de carrera)


# ==========================
# 🔹 USANDO LOCK PARA EVITAR ERRORES
# ==========================

contador = 0
lock = threading.Lock()

def incrementar_seguro():
    global contador
    for _ in range(100000):
        with lock:  # Bloquea el acceso hasta que termine
            contador += 1

hilo_a = threading.Thread(target=incrementar_seguro)
hilo_b = threading.Thread(target=incrementar_seguro)

hilo_a.start()
hilo_b.start()
hilo_a.join()
hilo_b.join()

print("Contador con Lock:", contador)  # Resultado correcto


# ==========================
# 🔹 USANDO THREADS PARA SIMULAR DESCARGAS
# ==========================

def descargar_archivo(nombre, tiempo):
    print(f"📥 Descargando {nombre}...")
    time.sleep(tiempo)
    print(f"✅ {nombre} descargado en {tiempo}s")

archivos = [("archivo1.zip", 3), ("archivo2.zip", 2), ("archivo3.zip", 1)]

hilos = [threading.Thread(target=descargar_archivo, args=(nombre, t)) for nombre, t in archivos]

# Iniciar todos los hilos
for h in hilos:
    h.start()

# Esperar a que terminen
for h in hilos:
    h.join()

print("✅ Todas las descargas completadas")


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Simulación de banco con múltiples hilos accediendo a una cuenta bancaria.

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        self.lock = threading.Lock()

    def depositar(self, cantidad):
        with self.lock:
            print(f"💰 Depositando {cantidad}...")
            saldo_anterior = self.saldo
            time.sleep(0.1)
            self.saldo = saldo_anterior + cantidad
            print(f"Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        with self.lock:
            if self.saldo >= cantidad:
                print(f"🏧 Retirando {cantidad}...")
                saldo_anterior = self.saldo
                time.sleep(0.1)
                self.saldo = saldo_anterior - cantidad
                print(f"Nuevo saldo: {self.saldo}")
            else:
                print("❌ Fondos insuficientes")

# Crear cuenta y hilos
cuenta = CuentaBancaria(100)
hilos = [
    threading.Thread(target=cuenta.depositar, args=(50,)),
    threading.Thread(target=cuenta.retirar, args=(30,)),
    threading.Thread(target=cuenta.retirar, args=(150,)),
]

for h in hilos:
    h.start()
for h in hilos:
    h.join()

print(f"Saldo final: {cuenta.saldo}")


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué son los hilos y cómo crearlos con threading.Thread
# - Problema de condiciones de carrera
# - Uso de Lock para evitar errores en concurrencia
# - Mini proyecto: cuenta bancaria protegida con Lock
#
# Próxima clase: Multiprocessing en Python – usar múltiples procesos para tareas pesadas de CPU.
