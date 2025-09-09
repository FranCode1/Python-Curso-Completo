#2. Analisis de Notas:
# Ingresa las notas de 5 alumnos (3 por alumno). Por cada uno:
# - Calcula el promedio.
# - Determina si esta aprobado (>=7).
# - Mostra el promedio general del curso y el mayor promedio individual.


def calcular_promedio(notas):
    return sum(notas) / len(notas)

def notas():
    orden = ["primera", "segunda", "tercera"]
    promedios_curso = []
    alumnos_aprobados = 0
    alumnos_desaprobados = 0

    alumnos_cantidad = int(input("Ingrese la cantidad de alumnos: "))

    mejor_promedio = -1
    mejor_alumno = ""

    for i in range(alumnos_cantidad):
        nombre = input(f"\nIngrese el nombre del alumno {i+1}: ")
        notas_alumno = []

        # Ingresar 3 notas válidas
        while len(notas_alumno) < 3:
            try:
                nota = float(input(f"Ingrese la {orden[len(notas_alumno)]} nota de {nombre}: "))
                if 0 <= nota <= 10:
                    notas_alumno.append(nota)
                else:
                    print("❌ Nota inválida. Debe estar entre 0 y 10.")
            except ValueError:
                print("⚠️ Ingrese un número válido.")

        promedio = calcular_promedio(notas_alumno)
        promedios_curso.append(promedio)

        # Mostrar promedio de cada alumno
        print(f"📊 El promedio de {nombre} es {promedio:.2f} {'✔️ Aprobado' if promedio >= 6 else '❌ Desaprobado'}")

        if promedio >= 6:
            alumnos_aprobados += 1
        else:
            alumnos_desaprobados += 1

        # Guardar el mejor alumno
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_alumno = nombre

    # Resultados finales
    print("\n📊 RESULTADOS FINALES:")
    print(f"✔️ Alumnos aprobados: {alumnos_aprobados}")
    print(f"❌ Alumnos desaprobados: {alumnos_desaprobados}")
    print(f"📈 Promedio general del curso: {sum(promedios_curso) / alumnos_cantidad:.2f}")
    print(f"🏆 Mejor promedio: {mejor_promedio:.2f} (Alumno: {mejor_alumno})")
    print(f"📉 Promedio más bajo: {min(promedios_curso):.2f}")

# Ejecutar el programa
notas()
