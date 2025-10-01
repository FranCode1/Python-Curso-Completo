# ============================================================
# CLASE 46: PROYECTO INTEGRADOR - EJERCICIOS RESUELTOS
# ============================================================
# 🎯 Objetivo:
# Practicar ampliaciones y mejoras sobre el proyecto "Gestor de Tareas"
# aplicando:
# - Clases y herencia
# - Funciones
# - Archivos JSON
# - Excepciones
# - Organización modular simulada
# - Pruebas con unittest
# ============================================================

import json
import os
import unittest

ARCHIVO_TAREAS = "tareas.json"


# ------------------------------------------------------------
# 📌 Clase base: Tarea
# ------------------------------------------------------------
class Tarea:
    """Representa una tarea de la lista ToDo."""

    def __init__(self, titulo, descripcion="", prioridad="Media"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self.completada = True

    def __str__(self):
        estado = "✔" if self.completada else "✗"
        return f"[{estado}] {self.titulo} - {self.descripcion} (Prioridad: {self.prioridad})"


# ============================================================
# 📌 EJERCICIO 1: Subclase TareaUrgente
# ------------------------------------------------------------
# Consigna: Crear una clase hija de Tarea llamada "TareaUrgente"
# que tenga un atributo extra "tiempo_limite" (string) y reemplace
# el método __str__ para mostrar el límite.
# ============================================================
class TareaUrgente(Tarea):
    def __init__(self, titulo, descripcion, tiempo_limite):
        super().__init__(titulo, descripcion, prioridad="Alta")
        self.tiempo_limite = tiempo_limite

    def __str__(self):
        estado = "✔" if self.completada else "✗"
        return f"[{estado}] URGENTE: {self.titulo} - {self.descripcion} | Límite: {self.tiempo_limite}"


# ============================================================
# 📌 EJERCICIO 2: Guardar y cargar tareas (persistencia)
# ------------------------------------------------------------
# Consigna: Crear funciones para guardar y cargar tareas desde un
# archivo JSON, manejando posibles errores.
# ============================================================
def guardar_tareas(tareas):
    try:
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
            json.dump([t.__dict__ for t in tareas], f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"⚠ Error al guardar: {e}")


def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            data = json.load(f)
            tareas = []
            for t in data:
                if "tiempo_limite" in t:
                    tarea = TareaUrgente(t["titulo"], t["descripcion"], t["tiempo_limite"])
                else:
                    tarea = Tarea(t["titulo"], t["descripcion"], t.get("prioridad", "Media"))
                tarea.completada = t["completada"]
                tareas.append(tarea)
            return tareas
    except Exception as e:
        print(f"⚠ Error al cargar: {e}")
        return []


# ============================================================
# 📌 EJERCICIO 3: Buscar tarea por título
# ------------------------------------------------------------
# Consigna: Implementar una función que busque una tarea en la lista
# por su título y la devuelva.
# ============================================================
def buscar_tarea(tareas, titulo):
    for t in tareas:
        if t.titulo.lower() == titulo.lower():
            return t
    return None


# ============================================================
# 📌 EJERCICIO 4: Eliminar tarea
# ------------------------------------------------------------
# Consigna: Implementar una función que elimine una tarea de la lista
# según su título.
# ============================================================
def eliminar_tarea(tareas, titulo):
    tarea = buscar_tarea(tareas, titulo)
    if tarea:
        tareas.remove(tarea)
        return True
    return False


# ============================================================
# 📌 EJERCICIO 5: Filtrar tareas completadas
# ------------------------------------------------------------
# Consigna: Crear una función que devuelva solo las tareas completadas.
# ============================================================
def tareas_completadas(tareas):
    return [t for t in tareas if t.completada]


# ============================================================
# 📌 EJERCICIO 6: Filtrar tareas pendientes
# ------------------------------------------------------------
# Consigna: Crear una función que devuelva solo las tareas pendientes.
# ============================================================
def tareas_pendientes(tareas):
    return [t for t in tareas if not t.completada]


# ============================================================
# 📌 EJERCICIO 7: Contar tareas por prioridad
# ------------------------------------------------------------
# Consigna: Crear una función que devuelva un diccionario con la
# cantidad de tareas por cada nivel de prioridad.
# ============================================================
def contar_por_prioridad(tareas):
    conteo = {}
    for t in tareas:
        conteo[t.prioridad] = conteo.get(t.prioridad, 0) + 1
    return conteo


# ============================================================
# 📌 EJERCICIO 8: Mostrar tareas con índice
# ------------------------------------------------------------
# Consigna: Crear una función que muestre todas las tareas numeradas.
# ============================================================
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
        return
    for i, t in enumerate(tareas, start=1):
        print(f"{i}. {t}")


# ============================================================
# 📌 EJERCICIO 9: Menú interactivo
# ------------------------------------------------------------
# Consigna: Crear un menú simple para probar las funciones anteriores.
# ============================================================
def menu():
    tareas = cargar_tareas()

    while True:
        print("\n=== 📋 GESTOR DE TAREAS ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Guardar y salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            titulo = input("Título: ")
            desc = input("Descripción: ")
            tareas.append(Tarea(titulo, desc))
            print("✅ Tarea agregada.")
        elif opcion == "3":
            titulo = input("Título de la tarea a completar: ")
            tarea = buscar_tarea(tareas, titulo)
            if tarea:
                tarea.marcar_completada()
                print("✅ Tarea completada.")
            else:
                print("⚠ No encontrada.")
        elif opcion == "4":
            titulo = input("Título de la tarea a eliminar: ")
            if eliminar_tarea(tareas, titulo):
                print("🗑️ Tarea eliminada.")
            else:
                print("⚠ No encontrada.")
        elif opcion == "5":
            guardar_tareas(tareas)
            print("💾 Tareas guardadas. ¡Hasta luego!")
            break
        else:
            print("⚠ Opción inválida.")


# ============================================================
# 📌 EJERCICIO 10: Pruebas con unittest
# ------------------------------------------------------------
# Consigna: Crear pruebas unitarias para la clase Tarea y las funciones.
# ============================================================
class TestTareas(unittest.TestCase):
    def test_crear_tarea(self):
        t = Tarea("Estudiar", "Repasar OOP")
        self.assertEqual(t.titulo, "Estudiar")
        self.assertFalse(t.completada)

    def test_marcar_completada(self):
        t = Tarea("Escribir código")
        t.marcar_completada()
        self.assertTrue(t.completada)

    def test_buscar_tarea(self):
        lista = [Tarea("A"), Tarea("B")]
        self.assertIsNotNone(buscar_tarea(lista, "A"))
        self.assertIsNone(buscar_tarea(lista, "X"))

    def test_eliminar_tarea(self):
        lista = [Tarea("A"), Tarea("B")]
        self.assertTrue(eliminar_tarea(lista, "A"))
        self.assertFalse(eliminar_tarea(lista, "X"))


# ------------------------------------------------------------
# 📌 EJECUCIÓN DEL ARCHIVO
# ------------------------------------------------------------
if __name__ == "__main__":
    # Ejecutar menú interactivo
    # menu()

    # Ejecutar pruebas
    print("\n🧪 Ejecutando pruebas...")
    unittest.main(exit=False)
