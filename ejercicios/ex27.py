# =====================================================================
# EJERCICIO 27: Calcular el doble de un número
# ---------------------------------------------------------------------
# Crear una función que reciba un número como parámetro y devuelva el doble
# Entrada: num_doble(4)
# Salida: 8
# =====================================================================

# ---------- Forma 1: función simple ----------
def doble1(num):
    return num * 2

# ---------- Forma 2: usando suma ----------
def doble2(num):
    return num + num

# ---------- Forma 3: usando operador bit shift (solo enteros) ----------
def doble3(num):
    if isinstance(num, int):
        return num << 1
    else:
        return num * 2

# ---------- Forma 4: usando una función lambda ----------
doble4 = lambda num: num * 2

# ---------- Forma 5: función con print dentro ----------
def doble5(num):
    resultado = num * 2
    print(f"El doble de {num} es {resultado}")
    return resultado

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    numero = float(input("Ingrese un número: "))

    print(doble1(numero))
    print(doble2(numero))
    print(doble3(numero))
    print(doble4(numero))
    doble5(numero)
