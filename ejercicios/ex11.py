# ----------------------------------------------------------
# EJERCICIO 11 - Control de Asistencia
# ----------------------------------------------------------
# Pedir el nombre de varios alumnos y si asistieron (Sí/No)
# Al final mostrar:
# - Cantidad de alumnos presentes y ausentes
# - Porcentaje de asistencia
# - Nombres de los que asistieron y los que no


# ========== MÉTODO 1: clásico con listas ==========
print("\n🔹 MÉTODO 1: Listas y contador")

alumnos_asistidos = 0
alumnos_ausentes = 0
nombre_alumnos = []
presentes = []
ausentes = []

for i in range(6):
    nombre = input("Ingrese el nombre del alumno: ")
    asistencia = input("¿Asistió? (Si/No): ").strip().lower()
    nombre_alumnos.append(nombre)

    if asistencia == "si":
        alumnos_asistidos += 1
        presentes.append(nombre)
    else:
        alumnos_ausentes += 1
        ausentes.append(nombre)

porcentaje = (alumnos_asistidos / len(nombre_alumnos)) * 100

print("\n✅ Estadísticas:")
print(f"Asistieron: {alumnos_asistidos}")
print(f"No asistieron: {alumnos_ausentes}")
print(f"Porcentaje de asistencia: {porcentaje:.2f}%")
print("Alumnos presentes:", presentes)
print("Alumnos ausentes:", ausentes)


# ========== MÉTODO 2: usando diccionarios ==========
print("\n🔹 MÉTODO 2: Diccionario nombre → asistencia")

asistencia_dict = {}

for i in range(6):
    nombre = input("Nombre del alumno: ")
    presente = input("¿Asistió? (si/no): ").lower()
    asistencia_dict[nombre] = presente

presentes2 = [n for n, a in asistencia_dict.items() if a == "si"]
ausentes2 = [n for n, a in asistencia_dict.items() if a != "si"]

print(f"\nAsistieron: {len(presentes2)}")
print(f"No asistieron: {len(ausentes2)}")
print(f"Porcentaje: {(len(presentes2) / len(asistencia_dict)) * 100:.2f}%")
print("Presentes:", presentes2)
print("Ausentes:", ausentes2)


# ========== MÉTODO 3: función y validación ==========
print("\n🔹 MÉTODO 3: Función con validación")

def control_asistencia(cantidad):
    presentes = []
    ausentes = []
    for _ in range(cantidad):
        nombre = input("Nombre del alumno: ")
        while True:
            asistencia = input("¿Asistió? (si/no): ").strip().lower()
            if asistencia in ["si", "no"]:
                break
            print("Respuesta inválida. Escriba 'si' o 'no'.")
        if asistencia == "si":
            presentes.append(nombre)
        else:
            ausentes.append(nombre)
    return presentes, ausentes

pres, aus = control_asistencia(6)
print(f"\nAsistieron: {len(pres)}")
print(f"No asistieron: {len(aus)}")
print(f"Porcentaje: {(len(pres)/6)*100:.2f}%")
print("Presentes:", pres)
print("Ausentes:", aus)


# ========== MÉTODO 4: uso de tuplas ==========
print("\n🔹 MÉTODO 4: Tuplas y estadísticas finales")

alumnos = []

for _ in range(6):
    nombre = input("Nombre: ")
    estado = input("¿Presente? (si/no): ").strip().lower()
    alumnos.append((nombre, estado))

asistentes = [n for n, e in alumnos if e == "si"]
faltantes = [n for n, e in alumnos if e != "si"]

print(f"\nPresentes: {len(asistentes)}")
print(f"Ausentes: {len(faltantes)}")
print(f"Asistencia: {(len(asistentes)/len(alumnos))*100:.2f}%")
print("Lista de presentes:", asistentes)
print("Lista de ausentes:", faltantes)


# ========== MÉTODO 5: con clase Alumno ==========
print("\n🔹 MÉTODO 5: Programación orientada a objetos")

class Alumno:
    def __init__(self, nombre, presente):
        self.nombre = nombre
        self.presente = presente

alumnos5 = []
for _ in range(6):
    nombre = input("Nombre: ")
    asistio = input("¿Presente? (si/no): ").lower() == "si"
    alumnos5.append(Alumno(nombre, asistio))

pres5 = [a.nombre for a in alumnos5 if a.presente]
aus5 = [a.nombre for a in alumnos5 if not a.presente]

print(f"\nTotal presentes: {len(pres5)}")
print(f"Total ausentes: {len(aus5)}")
print(f"Porcentaje asistencia: {(len(pres5)/len(alumnos5))*100:.2f}%")
print("Asistieron:", pres5)
print("No asistieron:", aus5)
