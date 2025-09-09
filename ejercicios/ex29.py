# =====================================================================
# EJERCICIO 29: Par o Impar
# ---------------------------------------------------------------------
# Crear una función que reciba un número y devuelva 'Par' si es par
# o 'Impar' si no lo es
# Entrada: 4
# Salida: "4 es Par"
# =====================================================================

# ---------- Forma 1: if-else simple ----------
def par_impar1(num):
    if num % 2 == 0:
        return f"{num} es Par"
    else:
        return f"{num} es Impar"

# ---------- Forma 2: operador ternario ----------
def par_impar2(num):
    return f"{num} es {'Par' if num % 2 == 0 else 'Impar'}"

# ---------- Forma 3: usando diccionario ----------
def par_impar3(num):
    return {True: f"{num} es Par", False: f"{num} es Impar"}[num % 2 == 0]

# ---------- Forma 4: con función interna ----------
def par_impar4(num):
    def tipo(n):
        if n % 2 == 0:
            return "Par"
        else:
            return "Impar"
    return f"{num} es {tipo(num)}"

# ---------- Forma 5: usando print dentro ----------
def par_impar5(num):
    resultado = "Par" if num % 2 == 0 else "Impar"
    print(f"{num} es {resultado}")
    return resultado

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))

    print(par_impar1(numero))
    print(par_impar2(numero))
    print(par_impar3(numero))
    print(par_impar4(numero))
    par_impar5(numero)
