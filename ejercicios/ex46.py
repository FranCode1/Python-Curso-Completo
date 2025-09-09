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
    aprobados = 0
    desaprobados = 0

    for i in range(n):
        suma = 0
        for j in range(3):
            while True:
                nota = float(input(f"Alumno {i+1}, nota {j+1}: "))
                if 0 <= nota <= 10:
                    break
                print("Nota inválida, ingrese un número entre 0 y 10.")
            suma += nota
        promedio = suma / 3
        promedio_curso.append(promedio)
        if promedio >= 6:
            aprobados += 1
        else:
            desaprobados += 1

    print(f"[Forma 1] Aprobados: {aprobados}, Desaprobados: {desaprobados}")
    print(f"Promedio general: {sum(promedio_curso)/n:.2f}")
    print(f"Promedio más alto: {max(promedio_curso):.2f}")
    print(f"Promedio más bajo: {min(promedio_curso):.2f}")

# ---------- Forma 2: Usando función auxiliar ----------
def promedio_lista(notas):
    return sum(notas) / len(notas)

def notas_2():
    n = int(input("Cantidad de alumnos: "))
    promedio_curso = []
    aprobados = desaprobados = 0

    for i in range(n):
        notas_alumno = []
        for j in range(3):
            while True:
                nota = float(input(f"Alumno {i+1}, nota {j+1}: "))
                if 0 <= nota <= 10:
                    break
                print("Nota inválida")
            notas_alumno.append(nota)
        promedio = promedio_lista(notas_alumno)
        promedio_curso.append(promedio)
        if promedio >= 6:
            aprobados += 1
        else:
            desaprobados += 1

    print(f"[Forma 2] Aprobados: {aprobados}, Desaprobados: {desaprobados}")
    print(f"Promedio general: {sum(promedio_curso)/n:.2f}")
    print(f"Promedio más alto: {max(promedio_curso):.2f}")
    print(f"Promedio más bajo: {min(promedio_curso):.2f}")

# ---------- Forma 3: Usando while para ingresar notas ----------
def notas_3():
    n = int(input("Cantidad de alumnos: "))
    promedio_curso = []
    aprobados = desaprobados = 0

    for i in range(n):
        notas_alumno = []
        while len(notas_alumno) < 3:
            nota = float(input(f"Alumno {i+1}, nota {len(notas_alumno)+1}: "))
            if 0 <= nota <= 10:
                notas_alumno.append(nota)
            else:
                print("Nota inválida")
        promedio = sum(notas_alumno)/3
        promedio_curso.append(promedio)
        if promedio >= 6:
            aprobados += 1
        else:
            desaprobados += 1

    print(f"[Forma 3] Aprobados: {aprobados}, Desaprobados: {desaprobados}")
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

# ---------- Forma 5: Usando map y sum ----------
def notas_5():
    n = int(input("Cantidad de alumnos: "))
    promedios = []
    for i in range(n):
        notas = []
        for j in range(3):
            while True:
                nota = float(input(f"Alumno {i+1}, nota {j+1}: "))
                if 0 <= nota <= 10:
                    break
                print("Nota inválida")
            notas.append(nota)
        promedio = sum(notas)/len(notas)
        promedios.append(promedio)

    aprobados = len(list(filter(lambda x: x >= 6, promedios)))
    desaprobados = n - aprobados

    print(f"[Forma 5] Aprobados: {aprobados}, Desaprobados: {desaprobados}")
    print(f"Promedio general: {sum(promedios)/n:.2f}")
    print(f"Promedio más alto: {max(promedios):.2f}")
    print(f"Promedio más bajo: {min(promedios):.2f}")

# =====================================================
# Ejecución del programa
# =====================================================
if __name__ == "__main__":
    # Descomentar la versión que quieras probar
    # notas_1()
    # notas_2()
    # notas_3()
    # notas_4()
    notas_5()
