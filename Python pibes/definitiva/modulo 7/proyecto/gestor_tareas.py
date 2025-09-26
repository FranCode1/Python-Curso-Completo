"""
Gestor de Tareas - Proyecto Módulo 7
Demostración de librerías estándar, SQLite, JSON, requests y buenas prácticas.
"""

import sys
from db import crear_tabla, agregar_tarea, listar_tareas
from utils import exportar_json, obtener_frase_motivacional

def mostrar_menu():
    print("\n📌 Gestor de Tareas")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Exportar a JSON")
    print("4. Frase motivacional")
    print("5. Salir")

def main():
    crear_tabla()  # Asegura que la BD exista

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título de la tarea: ")
            agregar_tarea(titulo)
            print("✅ Tarea agregada.")
        elif opcion == "2":
            tareas = listar_tareas()
            for t in tareas:
                print(f"[{t[0]}] {t[1]} - {t[2]}")
        elif opcion == "3":
            exportar_json()
        elif opcion == "4":
            print("💡", obtener_frase_motivacional())
        elif opcion == "5":
            print("👋 Saliendo...")
            sys.exit()
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    main()
