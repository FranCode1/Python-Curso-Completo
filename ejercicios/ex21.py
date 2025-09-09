# =====================================================================
# EJERCICIO 21: Determinar ciclo escolar
# ---------------------------------------------------------------------
# Pedir la edad del alumno e indicar a qué ciclo corresponde:
# - Jardín (3 a 5 años)
# - Primaria (6 a 11 años)
# - Secundario (12 a 17 años)
# - Otro (fuera de rango)
# =====================================================================

# ---------- Forma 1: usando if/elif ----------
def ciclo1():
    edad = int(input("Ingresar edad del alumno: "))
    if 3 <= edad <= 5:
        print("El estudiante corresponde al ciclo de jardín")
    elif 6 <= edad <= 11:
        print("El estudiante corresponde al ciclo de primaria")
    elif 12 <= edad <= 17:
        print("El estudiante corresponde al ciclo de secundario")
    else:
        print("Edad fuera de rango")

# ---------- Forma 2: usando diccionario con rangos ----------
def ciclo2():
    edad = int(input("Ingresar edad del alumno: "))
    ciclos = {
        range(3, 6): "Jardín",
        range(6, 12): "Primaria",
        range(12, 18): "Secundario"
    }
    for r, nombre in ciclos.items():
        if edad in r:
            print(f"El estudiante corresponde al ciclo de {nombre}")
            break
    else:
        print("Edad fuera de rango")

# ---------- Forma 3: usando lista de tuplas ----------
def ciclo3():
    edad = int(input("Ingresar edad del alumno: "))
    ciclos = [(3,5,"Jardín"), (6,11,"Primaria"), (12,17,"Secundario")]
    for inicio, fin, nombre in ciclos:
        if inicio <= edad <= fin:
            print(f"El estudiante corresponde al ciclo de {nombre}")
            break
    else:
        print("Edad fuera de rango")

# ---------- Forma 4: usando match/case (Python 3.10+) ----------
def ciclo4():
    edad = int(input("Ingresar edad del alumno: "))
    match edad:
        case edad if 3 <= edad <= 5:
            print("El estudiante corresponde al ciclo de jardín")
        case edad if 6 <= edad <= 11:
            print("El estudiante corresponde al ciclo de primaria")
        case edad if 12 <= edad <= 17:
            print("El estudiante corresponde al ciclo de secundario")
        case _:
            print("Edad fuera de rango")

# ---------- Forma 5: usando operador ternario ----------
def ciclo5():
    edad = int(input("Ingresar edad del alumno: "))
    print("Jardín" if 3 <= edad <=5 else "Primaria" if 6<=edad<=11 else "Secundario" if 12<=edad<=17 else "Edad fuera de rango")

# =====================================================================
# Ejecución
# =====================================================================
if __name__ == "__main__":
    # Descomentar la función que quieras probar
    # ciclo1()
    # ciclo2()
    # ciclo3()
    # ciclo4()
    ciclo5()
