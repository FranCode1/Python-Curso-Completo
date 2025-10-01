# ----------------------------------------
# CLASE 36: PROGRAMACIÓN ASÍNCRONA (ASYNC, AWAIT, ASYNCIO)
# ----------------------------------------

import asyncio
import time

# ============================================================
# EJERCICIO 1: Corrutina básica
# ============================================================
# Consigna:
# Crea una función asíncrona que imprima "Hola" y luego "Mundo"
# con 1 segundo de espera entre ambos mensajes.

async def hola_mundo():
    print("Hola")
    await asyncio.sleep(1)
    print("Mundo")

asyncio.run(hola_mundo())


# ============================================================
# EJERCICIO 2: Ejecutar varias tareas concurrentes
# ============================================================
# Consigna:
# Lanza tres tareas concurrentes con diferentes tiempos de espera
# y verifica que se ejecutan al mismo tiempo.

async def tarea(nombre, duracion):
    print(f"⏳ Iniciando tarea {nombre}")
    await asyncio.sleep(duracion)
    print(f"✅ Tarea {nombre} completada")

async def main_concurrente():
    await asyncio.gather(
        tarea("A", 2),
        tarea("B", 1),
        tarea("C", 3)
    )

asyncio.run(main_concurrente())


# ============================================================
# EJERCICIO 3: Uso de create_task
# ============================================================
# Consigna:
# Crea una tarea con create_task() y permite que el programa
# siga ejecutándose mientras la tarea corre en segundo plano.

async def ejemplo_task():
    print("Iniciando tarea en segundo plano...")
    await asyncio.sleep(2)
    print("Terminó tarea en segundo plano")

async def main_task():
    task = asyncio.create_task(ejemplo_task())
    print("➡ Task creada, programa sigue...")
    await task

asyncio.run(main_task())


# ============================================================
# EJERCICIO 4: Devolver resultados desde corrutinas
# ============================================================
# Consigna:
# Crea una corrutina que sume dos números con retardo simulado
# y devuelva el resultado.

async def sumar(a, b):
    await asyncio.sleep(1)
    return a + b

async def main_sumar():
    resultado = await sumar(4, 6)
    print("✅ Ejercicio 4:", resultado)

asyncio.run(main_sumar())


# ============================================================
# EJERCICIO 5: Correr tareas en orden secuencial
# ============================================================
# Consigna:
# Ejecuta varias corrutinas de forma secuencial usando `await`.

async def proceso(nombre):
    print(f"Iniciando {nombre}")
    await asyncio.sleep(1)
    print(f"Finalizando {nombre}")

async def main_secuencial():
    await proceso("Primero")
    await proceso("Segundo")
    await proceso("Tercero")

asyncio.run(main_secuencial())


# ============================================================
# EJERCICIO 6: Correr tareas en paralelo con gather
# ============================================================
# Consigna:
# Descarga datos de varias "URLs" simuladas de forma concurrente.

async def descargar(url, t):
    print(f"📥 Descargando {url}...")
    await asyncio.sleep(t)
    print(f"✅ Descarga completa: {url}")
    return f"Datos de {url}"

async def main_descargas():
    urls = [("api1.com", 2), ("api2.com", 1), ("api3.com", 3)]
    resultados = await asyncio.gather(*(descargar(url, t) for url, t in urls))
    print("✅ Ejercicio 6:", resultados)

asyncio.run(main_descargas())


# ============================================================
# EJERCICIO 7: Cancelar tareas
# ============================================================
# Consigna:
# Inicia una tarea que tarda en completarse y cancélala antes de que termine.

async def tarea_larga():
    try:
        print("Iniciando tarea larga...")
        await asyncio.sleep(5)
        print("Tarea larga completada")
    except asyncio.CancelledError:
        print("❌ Tarea cancelada!")

async def main_cancelar():
    task = asyncio.create_task(tarea_larga())
    await asyncio.sleep(2)
    task.cancel()
    await task

asyncio.run(main_cancelar())


# ============================================================
# EJERCICIO 8: Mezclar código sincrónico y asíncrono
# ============================================================
# Consigna:
# Ejecuta una operación sincrónica y otra asíncrona dentro de la misma función.

def operacion_sincrona():
    time.sleep(1)
    print("⚡ Operación sincrónica completada")

async def operacion_asincrona():
    await asyncio.sleep(1)
    print("⚡ Operación asíncrona completada")

async def main_mixto():
    operacion_sincrona()
    await operacion_asincrona()

asyncio.run(main_mixto())


# ============================================================
# EJERCICIO 9: Simulación de múltiples usuarios
# ============================================================
# Consigna:
# Simula que varios usuarios se conectan al mismo tiempo con diferentes retrasos.

async def usuario(nombre, espera):
    print(f"👤 {nombre} conectando...")
    await asyncio.sleep(espera)
    print(f"✅ {nombre} conectado!")

async def main_usuarios():
    await asyncio.gather(
        usuario("Alice", 1),
        usuario("Bob", 3),
        usuario("Charlie", 2)
    )

asyncio.run(main_usuarios())


# ============================================================
# EJERCICIO 10: Pipeline de operaciones asíncronas
# ============================================================
# Consigna:
# Simula un pipeline: descargar → procesar → guardar datos, usando async.

async def descargar_datos():
    print("⬇ Descargando datos...")
    await asyncio.sleep(2)
    return [1, 2, 3]

async def procesar_datos(datos):
    print("⚙ Procesando datos...")
    await asyncio.sleep(1)
    return [x * 2 for x in datos]

async def guardar_datos(datos):
    print("💾 Guardando datos...")
    await asyncio.sleep(1)
    print("✅ Datos guardados:", datos)

async def main_pipeline():
    datos = await descargar_datos()
    procesados = await procesar_datos(datos)
    await guardar_datos(procesados)

asyncio.run(main_pipeline())
