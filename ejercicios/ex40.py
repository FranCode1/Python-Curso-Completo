# =====================================================================
# EJERCICIO 40: Contador de múltiplos de 3
# ---------------------------------------------------------------------
# Escribir una función que reciba dos números (inicio, fin) y cuente
# cuántos múltiplos de 3 hay en ese rango.
# Se deben usar range() y condicionales.
# =====================================================================

# ---------- Forma 1: con contador simple ----------
def mult3_1(inicio, fin):
    mults3 = 0
    for i in range(inicio, fin + 1):
        if i % 3 == 0:
            mults3 += 1
    print(f"Hay {mults3} múltiplos de 3 entre {inicio} y {fin}.")

# ---------- Forma 2: usando lista y len ----------
def mult3_2(inicio, fin):
    multiplos = [i for i in range(inicio, fin + 1) if i % 3 == 0]
    print(f"Hay {len(multiplos)} múltiplos de 3 entre {inicio} y {fin}.")

# ---------- Forma 3: usando while ----------
def mult3_3(inicio, fin):
    mults3 = 0
    i = inicio
    while i <= fin:
        if i % 3 == 0:
            mults3 += 1
        i += 1
    print(f"Hay {mults3} múltiplos de 3 entre {inicio} y {fin}.")

# ---------- Forma 4: usando contador acumulativo con paso 3 ----------
def mult3_4(inicio, fin):
    mults3 = 0
    # Ajustamos el inicio al primer múltiplo de 3 >= inicio
    if inicio % 3 != 0:
        inicio += 3 - inicio % 3
    for i in range(inicio, fin + 1, 3):
        mults3 += 1
    print(f"Hay {mults3} múltiplos de 3 entre {inicio} y {fin}.")

# ---------- Forma 5: usando función y sum con generador ----------
def mult3_5(inicio, fin):
    mults3 = sum(1 for i in range(inicio, fin + 1) if i % 3 == 0)
    print(f"Hay {mults3} múltiplos de 3 entre {inicio} y {fin}.")

# =====================================================================
# Ejecución del programa
# =====================================================================
if __name__ == "__main__":
    inicio = int(input("Ingrese el número de inicio: "))
    fin = int(input("Ingrese el número final: "))

    # Descomentar la función que quieras probar
    # mult3_1(inicio, fin)
    # mult3_2(inicio, fin)
    # mult3_3(inicio, fin)
    # mult3_4(inicio, fin)
    mult3_5(inicio, fin)
