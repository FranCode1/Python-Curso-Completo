from db import DBManager
from models import Gestor
from utils import exportar_json, exportar_csv

def mostrar_menu():
    print("\n📌 Gestor de Tareas Avanzado")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Exportar JSON")
    print("5. Exportar CSV")
    print("6. Salir")

def main():
    gestor = Gestor(DBManager())

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            desc = input("Descripción: ")
            gestor.agregar_tarea(titulo, desc)
            print("✅ Tarea agregada.")
        elif opcion == "2":
            for t in gestor.listar_tareas():
                print(f"[{t[0]}] {t[1]} - {t[3]} ({t[4]})")
        elif opcion == "3":
            tid = int(input("ID de la tarea a completar: "))
            gestor.completar_tarea(tid)
            print("✅ Tarea completada.")
        elif opcion == "4":
            exportar_json()
        elif opcion == "5":
            exportar_csv()
        elif opcion == "6":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    main()
