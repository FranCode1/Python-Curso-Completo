# ============================================
# EJERCICIO 49 - Validar mes y año
# Verificar que:
# - El mes solo tenga letras y empiece en mayúscula
# - El año solo tenga números
# - El año esté entre 1900 y el actual
# ============================================

# 🔹 MÉTODO 1: Validación con flags y estructura clara

from datetime import datetime

def validar_mes_y_año_1():
    año_actual = datetime.now().year

    while True:
        mes = input("Ingrese el mes: ").strip()
        año = input("Ingrese el año: ").strip()
        errores = False

        if not mes or not mes.isalpha() or not mes[0].isupper():
            print("❌ El mes debe comenzar con mayúscula y contener solo letras.")
            errores = True

        if not año.isdigit() or not (1900 <= int(año) <= año_actual):
            print(f"❌ El año debe estar entre 1900 y {año_actual}, y contener solo números.")
            errores = True

        if not errores:
            print(f"✅ Mes y año válidos: {mes.title()} {año}")
            break
        print("🔁 Intentá de nuevo.\n")

# validar_mes_y_año_1()


# 🔹 MÉTODO 2: Más modular, separa cada validación

def validar_mes(mes):
    return mes and mes.isalpha() and mes[0].isupper()

def validar_año(año):
    año_actual = datetime.now().year
    return año.isdigit() and 1900 <= int(año) <= año_actual

def validar_mes_y_año_2():
    while True:
        mes = input("Ingrese el mes: ").strip()
        año = input("Ingrese el año: ").strip()

        if not validar_mes(mes):
            print("❌ El mes debe comenzar con mayúscula y tener solo letras.")
        elif not validar_año(año):
            print("❌ El año debe ser numérico y estar entre 1900 y el actual.")
        else:
            print(f"✅ Mes y año válidos: {mes.title()} {año}")
            break
        print("🔁 Intentá de nuevo.\n")

# validar_mes_y_año_2()


# 🔹 MÉTODO 3: Estilo early-return para claridad

def validar_mes_y_año_3():
    año_actual = datetime.now().year
    while True:
        mes = input("Mes: ").strip()
        if not mes or not mes.isalpha() or not mes[0].isupper():
            print("❌ Mes inválido.")
            continue

        año = input("Año: ").strip()
        if not año.isdigit():
            print("❌ El año debe ser numérico.")
            continue

        año = int(año)
        if año < 1900 or año > año_actual:
            print(f"❌ Año fuera de rango (1900-{año_actual})")
            continue

        print(f"✅ Mes y año válidos: {mes.title()} {año}")
        break

# validar_mes_y_año_3()


# 🔹 MÉTODO 4: Guarda errores y los muestra juntos

def validar_mes_y_año_4():
    año_actual = datetime.now().year
    while True:
        errores = []

        mes = input("Mes: ").strip()
        año = input("Año: ").strip()

        if not mes:
            errores.append("El mes no puede estar vacío.")
        elif not mes.isalpha():
            errores.append("El mes solo debe tener letras.")
        elif not mes[0].isupper():
            errores.append("El mes debe comenzar con mayúscula.")

        if not año:
            errores.append("El año no puede estar vacío.")
        elif not año.isdigit():
            errores.append("El año debe tener solo números.")
        else:
            año_int = int(año)
            if not (1900 <= año_int <= año_actual):
                errores.append(f"El año debe estar entre 1900 y {año_actual}.")

        if not errores:
            print(f"✅ Mes y año válidos: {mes.title()} {año}")
            break
        else:
            for error in errores:
                print("❌", error)
            print("🔁 Intentá nuevamente.\n")

# validar_mes_y_año_4()


# 🔹 MÉTODO 5: Con match-case (estructura moderna)

def validar_mes_y_año_5():
    año_actual = datetime.now().year
    while True:
        mes = input("Mes: ").strip()
        año = input("Año: ").strip()

        match (mes.isalpha(), mes[0].isupper() if mes else False, año.isdigit()):
            case (True, True, True):
                año = int(año)
                if 1900 <= año <= año_actual:
                    print(f"✅ Mes y año válidos: {mes.title()} {año}")
                    break
                else:
                    print(f"❌ El año debe estar entre 1900 y {año_actual}.")
            case _:
                print("❌ Datos inválidos. El mes debe ser solo letras, comenzar con mayúscula y el año debe ser numérico.")
        print("🔁 Intentá nuevamente.\n")

# validar_mes_y_año_5()
