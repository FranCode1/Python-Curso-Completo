# ================================================
# Proyecto Módulo 1: Gestor de Tareas en Consola
# ================================================

# Lista de tareas: cada tarea es un diccionario {"titulo": str, "completada": bool}
tareas = []

# Set para controlar títulos únicos
titulos_existentes = set()

# Lista de historial (cada entrada es una tupla: (titulo, estado))
historial_eliminadas = []

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Ver historial de eliminadas")
    print("6. Salir")

def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")

    if titulo in titulos_existentes:
        print("⚠️ Esa tarea ya existe. Intenta con otro título.")
        return

    tarea = {"titulo": titulo, "completada": False}
    tareas.append(tarea)
    titulos_existentes.add(titulo)  # Se agrega al set
    print(f"Tarea '{titulo}' agregada.")

def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            estado = "✔️" if tarea["completada"] else "❌"
            print(f"{i}. {tarea['titulo']} - {estado}")

def completar_tarea():
    listar_tareas()
    try:
        num = int(input("Ingrese el número de la tarea a completar: "))
        tareas[num - 1]["completada"] = True
        print("Tarea marcada como completada.")
    except (ValueError, IndexError):
        print("Número inválido.")

def eliminar_tarea():
    listar_tareas()
    try:
        num = int(input("Ingrese el número de la tarea a eliminar: "))
        tarea_eliminada = tareas.pop(num - 1)
        titulos_existentes.remove(tarea_eliminada["titulo"])  # Se quita del set

        # Guardar historial como tupla (titulo, estado)
        historial_eliminadas.append(
            (tarea_eliminada["titulo"], tarea_eliminada["completada"])
        )

        print(f"Tarea '{tarea_eliminada['titulo']}' eliminada.")
    except (ValueError, IndexError, KeyError):
        print("Número inválido.")

def ver_historial():
    if not historial_eliminadas:
        print("No hay tareas eliminadas.")
    else:
        print("\n--- HISTORIAL DE ELIMINADAS ---")
        for i, tarea in enumerate(historial_eliminadas, start=1):
            titulo, estado = tarea  # Desempaquetar tupla
            estado_txt = "✔️ completada" if estado else "❌ pendiente"
            print(f"{i}. {titulo} - {estado_txt}")

# --- Programa principal ---
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        ver_historial()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intente nuevamente.")
