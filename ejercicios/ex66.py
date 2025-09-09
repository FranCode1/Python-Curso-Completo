# Pedir al usuario cantidad de alumnos de un curso.
# Para cada alumno pedir el porcentaje de asistencias y guardarla en una lista
# Recorrer la lista, calcular y mostrar:
# - promedio de inasistencias
# - posicion del alumno con mayor inasistencia
# - cantidad de alumnos libres(inasistencia mayor a 40%)



# =====================================================================
# EJERCICIO 46: Análisis de notas de alumnos
# ---------------------------------------------------------------------
# Un profesor debe procesar las notas de varios alumnos:
# 1. Pedir cuántos alumnos hay.
# 2. Para cada alumno, pedir 3 notas (entre 0 y 10).
# 3. Calcular el promedio de cada alumno.
# Luego mostrar:
# - Cuántos alumnos aprobaron (promedio ≥ 6) y desaprobaron.
# - Promedio general del curso.
# - Promedio más alto y más bajo entre todos los alumnos.
# =====================================================================

# ---------- Forma 1: Bucle for clásico ----------
def notas_1():
    n = int(input("Ingrese cantidad de alumnos: "))
    promedio_curso = []
    asistieron = 0
    no_asistieron = 0
    alumnos = []

    for i in range(n):
        suma = 0
        for j in range(3):
            while True:
                asistencia = input("el alumno asistio?")
                if asistencia == "si" or asistencia == "no":
                    break
                print("No respondio correctamente")
            if asistencia == "si":
                suma += 1
            #elif asistencia == "no":
            #suma += asistencia
        promedio = suma / 3
        promedio_curso.append(promedio)
        if promedio >= 6:
            asistieron += 1
        else:
            no_asistieron += 1

    print(f"[Forma 1] Asistieron: {asistieron}, libres: {no_asistieron}")
    print(f"Promedio general: {sum(promedio_curso)/n:.2f}")
    print(f"Promedio más alto: {max(promedio_curso):.2f}")
    print(f"Promedio más bajo: {min(promedio_curso):.2f}")


# ---------- Forma 4: Usando lista de listas ----------
def notas_4():
    n = int(input("Cantidad de alumnos: "))
    alumnos = []

    for i in range(n):
        notas = []
        for j in range(3):
            while True:
                nota = float(input(f"Alumno {i+1}, nota {j+1}: "))
                if 0 <= nota <= 10:
                    break
                print("Nota inválida")
            notas.append(nota)
        alumnos.append(notas)

    promedios = [sum(al)/3 for al in alumnos]
    aprobados = sum(1 for p in promedios if p >= 6)
    desaprobados = n - aprobados

    print(f"[Forma 4] Aprobados: {aprobados}, Desaprobados: {desaprobados}")
    print(f"Promedio general: {sum(promedios)/n:.2f}")
    print(f"Promedio más alto: {max(promedios):.2f}")
    print(f"Promedio más bajo: {min(promedios):.2f}")





# Pedir al usuario cantidad de alumnos de un curso. [LISTO ]
# Para cada alumno pedir el porcentaje de asistencias y guardarla en una lista[LISTO]
# Recorrer la lista, calcular y mostrar:
# - promedio de inasistencias
# - posicion del alumno con mayor inasistencia
# - cantidad de alumnos libres(inasistencia mayor a 40%)


cantidad_alumnos = int(input("Ingrese la cantidad de Alumnos: "))
alumnos = []

# for i in range(len(cantidad_alumnos)):
#     alumnoTemporal = int(input("Ingrese el porcentaje de asistencias del alumno: "))
#     alumnos.append(alumnoTemporal)

#     if alumnoTemporal < 40