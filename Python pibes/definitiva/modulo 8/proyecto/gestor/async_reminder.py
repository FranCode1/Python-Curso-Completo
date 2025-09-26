import asyncio

async def recordatorio(mensaje, segundos):
    await asyncio.sleep(segundos)
    print(f"\n🔔 Recordatorio: {mensaje}")

async def main():
    print("⏳ Configurando recordatorios...")
    await asyncio.gather(
        recordatorio("Revisar tareas pendientes", 5),
        recordatorio("Completar tarea importante", 10)
    )

if __name__ == "__main__":
    asyncio.run(main())
