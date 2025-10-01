# =====================================================================
# 📘 CLASE 40: Librerías estándar en Python - Ejercicios
# =====================================================================
# Este archivo contiene 10 ejercicios resueltos con consignas usando:
# - math
# - random
# - datetime
# - os
# - json
# =====================================================================

import math
import random
import os
import json
from datetime import datetime, timedelta

# ---------------------------------------------------------------------
# 🔹 EJERCICIO 1: Calcular área y circunferencia de un círculo
# Consigna: Usar math.pi y math.pow para calcular área y perímetro.
# ---------------------------------------------------------------------
def ejercicio1(radio):
    area = math.pi * math.pow(radio, 2)
    circunferencia = 2 * math.pi * radio
    print(f"Radio: {radio} → Área: {area:.2f}, Circunferencia: {circunferencia:.2f}")

ejercicio1(5)


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 2: Generar números aleatorios sin repetición
# Consigna: Usar random.sample para elegir 6 números de la lotería.
# ---------------------------------------------------------------------
def ejercicio2():
    numeros = random.sample(range(1, 50), 6)
    print("Números de lotería:", numeros)

ejercicio2()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 3: Simular lanzamiento de un dado
# Consigna: Usar random.randint para simular 10 lanzamientos.
# ---------------------------------------------------------------------
def ejercicio3():
    lanzamientos = [random.randint(1, 6) for _ in range(10)]
    print("Lanzamientos del dado:", lanzamientos)

ejercicio3()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 4: Calcular diferencia de días
# Consigna: Usar datetime para calcular cuántos días faltan para Año Nuevo.
# ---------------------------------------------------------------------
def ejercicio4():
    hoy = datetime.now()
    fin_anno = datetime(hoy.year, 12, 31)
    diferencia = (fin_anno - hoy).days
    print(f"Faltan {diferencia} días para Año Nuevo")

ejercicio4()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 5: Crear carpetas con nombres de días
# Consigna: Usar os.makedirs para crear 7 carpetas (Lunes a Domingo).
# ---------------------------------------------------------------------
def ejercicio5():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for d in dias:
        os.makedirs(d, exist_ok=True)
    print("✅ Carpetas de los días creadas.")
    # limpiar
    for d in dias:
        os.rmdir(d)
    print("🗑️ Carpetas eliminadas.")

ejercicio5()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 6: Guardar datos de un usuario en JSON
# Consigna: Usar json.dumps para serializar un diccionario.
# ---------------------------------------------------------------------
def ejercicio6():
    usuario = {"nombre": "Franco", "edad": 22, "lenguajes": ["Python", "JS"], "activo": True}
    json_str = json.dumps(usuario, indent=4)
    print("Usuario en formato JSON:")
    print(json_str)

ejercicio6()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 7: Leer temperaturas desde archivo JSON
# Consigna: Crear un archivo con temperaturas y leerlo con json.load.
# ---------------------------------------------------------------------
def ejercicio7():
    registro = []
    for i in range(3):
        fecha = (datetime.now() + timedelta(days=i)).strftime("%d/%m/%Y")
        temp = round(random.uniform(15, 30), 1)
        registro.append({"fecha": fecha, "temperatura": temp})

    with open("temp.json", "w") as f:
        json.dump(registro, f, indent=4)

    with open("temp.json", "r") as f:
        datos = json.load(f)
    print("📂 Datos de temperaturas leídos:", datos)
    os.remove("temp.json")

ejercicio7()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 8: Calcular factorial de varios números
# Consigna: Usar math.factorial en una lista de números.
# ---------------------------------------------------------------------
def ejercicio8():
    numeros = [3, 5, 7]
    factoriales = {n: math.factorial(n) for n in numeros}
    print("Factoriales:", factoriales)

ejercicio8()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 9: Simular una moneda al aire
# Consigna: Usar random.choice para elegir "Cara" o "Cruz".
# ---------------------------------------------------------------------
def ejercicio9():
    resultado = random.choice(["Cara", "Cruz"])
    print("Moneda:", resultado)

ejercicio9()


# ---------------------------------------------------------------------
# 🔹 EJERCICIO 10: Registro de eventos en JSON
# Consigna: Guardar 5 eventos con fecha y hora en un archivo JSON.
# ---------------------------------------------------------------------
def ejercicio10():
    eventos = []
    for i in range(5):
        evento = {
            "id": i + 1,
            "descripcion": f"Evento {i+1}",
            "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        eventos.append(evento)

    with open("eventos.json", "w") as f:
        json.dump(eventos, f, indent=4)

    print("✅ Archivo 'eventos.json' creado con eventos simulados.")
    os.remove("eventos.json")

ejercicio10()
