# =====================================================================
# EJERCICIO 28: Devolver el mayor de dos números
# ---------------------------------------------------------------------
# Crear una función que reciba dos números como parámetro y devuelva el mayor
# Entrada: devuelve_mayor(4, 78)
# Salida: 78
# =====================================================================

# ---------- Forma 1: if-else simple ----------
def mayor1(a, b):
    if a > b:
        return a
    else:
        return b

# ---------- Forma 2: usando función max ----------
def mayor2(a, b):
    return max(a, b)

# ---------- Forma 3: usando operador ternario ----------
def mayor3(a, b):
    return a if a > b else b

# ---------- Forma 4: usando una lista y max ----------
def mayor4(a, b):
    numeros = [a, b]
    return max(numeros)

# ---------- Forma 5: función con print dentro ----------
def mayor5(a, b):
    resultado = a if a > b else b
    print(f"El mayor entre {a} y {b} es {resultado}")
    return resultado

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print(mayor1(num1, num2))
    print(mayor2(num1, num2))
    print(mayor3(num1, num2))
    print(mayor4(num1, num2))
    mayor5(num1, num2)
