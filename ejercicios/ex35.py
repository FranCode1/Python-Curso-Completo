# =====================================================================
# EJERCICIO 35: Pirámide de asteriscos
# ---------------------------------------------------------------------
# Pedir un número y crear una pirámide de asteriscos con esa cantidad
# de pisos.
# Entrada: 5
# Salida:
# *
# **
# ***
# ****
# *****
# =====================================================================

# ---------- Forma 1: bucles for ----------
def piramide1(num):
    for i in range(1, num + 1):
        print('*' * i)

# ---------- Forma 2: bucle while ----------
def piramide2(num):
    i = 1
    while i <= num:
        print('*' * i)
        i += 1

# ---------- Forma 3: usando recursion ----------
def piramide3(num, i=1):
    if i > num:
        return
    print('*' * i)
    piramide3(num, i + 1)

# ---------- Forma 4: usando lista y join ----------
def piramide4(num):
    for i in range(1, num + 1):
        print(''.join(['*' for _ in range(i)]))

# ---------- Forma 5: usando formato con center para pirámide centrada ----------
def piramide5(num):
    for i in range(1, num + 1):
        print(('*' * i).center(num))

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    numero_input = int(input("Ingrese un número de pisos para la pirámide: "))

    print("\nForma 1:")
    piramide1(numero_input)

    print("\nForma 2:")
    piramide2(numero_input)

    print("\nForma 3:")
    piramide3(numero_input)

    print("\nForma 4:")
    piramide4(numero_input)

    print("\nForma 5 (centrada):")
    piramide5(numero_input)
