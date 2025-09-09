# =====================================================================
# EJERCICIO 56: Control de Notas y Estadísticas de Alumnos
# ---------------------------------------------------------------------
# Se pide un programa que lea las notas de 10 alumnos, cada uno con 3 exámenes. El programa debe:
# • Determinar cuántos alumnos promocionan (promedio ≥ 7 y sin desaprobados).
# • Determinar cuántos alumnos aprueban (promedio ≥ 4 y con hasta 1 desaprobado).
# • Determinar cuántos alumnos desaprueban (promedio < 4 o con 2 o más desaprobados).
# • Indicar el promedio más alto y el más bajo del curso.
# • Indicar la cantidad de alumnos que desaprobaron los tres exámenes.
# =====================================================================

# ---------- Forma 0: Versión normal ----------

promocion = 0
aprobado = 0
desaprobado = 0
promedio = 0
desTresExamenes = 0
for i in range(1,11):
    
    cantMenorCuatro = 0 #En esta variable controlo cuanto desaprobados tuvo el alumno
    print("Alumno: ",i)
    
    nota1 = int(input("Ingrese la nota 1: "))                
    if nota1 < 4:
        cantMenorCuatro += 1
        
    nota2 = int(input("Ingrese la nota 2: "))
    if nota2 < 4:
        cantMenorCuatro += 1

    nota3 = int(input("Ingrese la nota 3: "))
    if nota3 < 4:
        cantMenorCuatro += 1

    promedio = (nota1+nota2+nota3) / 3

    #Llevo la cuento de promocion, aprobado y desaprobado
    if promedio >= 7 and cantMenorCuatro == 0:
        promocion += 1
    if promedio >= 4 and cantMenorCuatro <= 1:
        aprobado += 1
    if promedio < 4 or cantMenorCuatro >= 2:
        desaprobado += 1

    #Control promedio mas bajo y alto
    if i == 1:
        #La primera vez no comparo
        mayPromedio = promedio
        menPromedio = promedio
    else:
        if promedio > mayPromedio:
            mayPromedio = promedio
        if promedio < menPromedio:
            menPromedio = promedio

    #Cantidad de alumnos que desaprobaron los 3 examenes
    if cantMenorCuatro == 3:
        desTresExamenes += 1

print("---------------------------------------------")
print("Cantidad de Promocionados: ", promocion)
print("Cantidad de Aprobados: ", aprobado)
print("Cantidad de Desaprobados: ",desaprobado)
print("")
print("---------------------------------------------")
print("Promedio mas alto: ",mayPromedio)
print("Promedio mas bajo: ",menPromedio)
print("")
print("---------------------------------------------")
print("Cantidad de alumnos que desaprobaron los tres examenes: ",desTresExamenes)

# ---------- Forma 1: Versión clásica ----------

promocionados = aprobados = desaprobados = 0
promedio_max = promedio_min = None
desaprobados_tres = 0

for i in range(1, 11):
    print(f"\nAlumno {i}:")
    notas = [int(input(f"Ingrese la nota {j+1}: ")) for j in range(3)]
    cant_menor_4 = sum(1 for n in notas if n < 4)
    promedio = sum(notas) / 3

    if promedio >= 7 and cant_menor_4 == 0:
        promocionados += 1
    elif promedio >= 4 and cant_menor_4 <= 1:
        aprobados += 1
    else:
        desaprobados += 1

    if promedio_max is None or promedio > promedio_max:
        promedio_max = promedio
    if promedio_min is None or promedio < promedio_min:
        promedio_min = promedio

    if cant_menor_4 == 3:
        desaprobados_tres += 1

print("\n--- RESULTADOS ---")
print("Promocionados:", promocionados)
print("Aprobados:", aprobados)
print("Desaprobados:", desaprobados)
print("Promedio más alto:", promedio_max)
print("Promedio más bajo:", promedio_min)
print("Desaprobados en los 3 exámenes:", desaprobados_tres)


# ---------- Forma 2: Con funciones ----------

def clasificar_alumno(notas):
    cant_menor_4 = sum(1 for n in notas if n < 4)
    promedio = sum(notas) / len(notas)

    if promedio >= 7 and cant_menor_4 == 0:
        return "promocion"
    elif promedio >= 4 and cant_menor_4 <= 1:
        return "aprobado"
    else:
        return "desaprobado"

def pedir_notas():
    return [int(input(f"Ingrese nota {i+1}: ")) for i in range(3)]

resultados = {"promocion": 0, "aprobado": 0, "desaprobado": 0}
promedios = []
desaprobados_tres = 0

for i in range(1, 11):
    print(f"\nAlumno {i}:")
    notas = pedir_notas()
    categoria = clasificar_alumno(notas)
    resultados[categoria] += 1
    promedios.append(sum(notas) / 3)
    if all(n < 4 for n in notas):
        desaprobados_tres += 1

print("\n--- RESULTADOS ---")
print(resultados)
print("Promedio más alto:", max(promedios))
print("Promedio más bajo:", min(promedios))
print("Desaprobados en los 3 exámenes:", desaprobados_tres)


# ---------- Forma 3: Con listas y comprensiones ----------

alumnos = []

for i in range(1, 11):
    print(f"\nAlumno {i}:")
    notas = [int(input(f"Ingrese nota {j+1}: ")) for j in range(3)]
    alumnos.append(notas)

promedios = [sum(n)/3 for n in alumnos]
desaprobados_tres = sum(1 for n in alumnos if all(x < 4 for x in n))

promocionados = sum(1 for n in alumnos if sum(n)/3 >= 7 and all(x >= 4 for x in n))
aprobados = sum(1 for n in alumnos if sum(n)/3 >= 4 and sum(1 for x in n if x < 4) <= 1)
desaprobados = 10 - (promocionados + aprobados)

print("\n--- RESULTADOS ---")
print("Promocionados:", promocionados)
print("Aprobados:", aprobados)
print("Desaprobados:", desaprobados)
print("Promedio más alto:", max(promedios))
print("Promedio más bajo:", min(promedios))
print("Desaprobados en los 3 exámenes:", desaprobados_tres)


# ---------- Forma 4: Con diccionarios y estadísticas ----------

import statistics as stats

alumnos = []

for i in range(1, 11):
    print(f"\nAlumno {i}:")
    notas = [int(input(f"Ingrese nota {j+1}: ")) for j in range(3)]
    alumnos.append({"id": i, "notas": notas, "promedio": stats.mean(notas)})

promocionados = sum(1 for a in alumnos if a["promedio"] >= 7 and all(n >= 4 for n in a["notas"]))
aprobados = sum(1 for a in alumnos if a["promedio"] >= 4 and sum(1 for n in a["notas"] if n < 4) <= 1)
desaprobados = len(alumnos) - (promocionados + aprobados)
desaprobados_tres = sum(1 for a in alumnos if all(n < 4 for n in a["notas"]))
promedios = [a["promedio"] for a in alumnos]

print("\n--- RESULTADOS ---")
print("Promocionados:", promocionados)
print("Aprobados:", aprobados)
print("Desaprobados:", desaprobados)
print("Promedio más alto:", max(promedios))
print("Promedio más bajo:", min(promedios))
print("Desaprobados en los 3 exámenes:", desaprobados_tres)


# ---------- Forma 5: Con pandas (modo pro, orientado a datos) ----------

import pandas as pd

datos = []

for i in range(1, 11):
    print(f"\nAlumno {i}:")
    notas = [int(input(f"Ingrese nota {j+1}: ")) for j in range(3)]
    datos.append({"Alumno": i, "Nota1": notas[0], "Nota2": notas[1], "Nota3": notas[2]})

df = pd.DataFrame(datos)
df["Promedio"] = df[["Nota1", "Nota2", "Nota3"]].mean(axis=1)
df["Menores4"] = df[["Nota1", "Nota2", "Nota3"]].lt(4).sum(axis=1)

df["Estado"] = df.apply(lambda x: 
    "Promocion" if x["Promedio"] >= 7 and x["Menores4"] == 0 else
    "Aprobado" if x["Promedio"] >= 4 and x["Menores4"] <= 1 else
    "Desaprobado", axis=1)

print("\n--- RESULTADOS ---")
print(df["Estado"].value_counts())
print("Promedio más alto:", df["Promedio"].max())
print("Promedio más bajo:", df["Promedio"].min())
print("Desaprobados en los 3 exámenes:", (df["Menores4"] == 3).sum())
