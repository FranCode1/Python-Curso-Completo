# =====================================================================
# EJERCICIO 31: Tabla de multiplicar
# ---------------------------------------------------------------------
# Crear una función que reciba un número y muestre su tabla de multiplicar
# del 1 al 10.
# Entrada: 7
# Salida: 7 x 1 = 7 ... 7 x 10 = 70
# =====================================================================

# ---------- Forma 1: función básica ----------
def tabla1(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# ---------- Forma 2: con while ----------
def tabla2(num):
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

# ---------- Forma 3: con lista y join ----------
def tabla3(num):
    resultados = [f"{num} x {i} = {num * i}" for i in range(1, 11)]
    print("\n".join(resultados))

# ---------- Forma 4: usando función lambda ----------
tabla4 = lambda num: [print(f"{num} x {i} = {num * i}") for i in range(1, 11)]

# ---------- Forma 5: devolver como string ----------
def tabla5(num):
    salida = ""
    for i in range(1, 11):
        salida += f"{num} x {i} = {num * i}\n"
    print(salida)
    return salida

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

    print("\nForma 1:")
    tabla1(numero)
    print("\nForma 2:")
    tabla2(numero)
    print("\nForma 3:")
    tabla3(numero)
    print("\nForma 4:")
    tabla4(numero)
    print("\nForma 5:")
    tabla5(numero)
