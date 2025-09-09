# =====================================================================
# EJERCICIO 34: Número a asteriscos
# ---------------------------------------------------------------------
# Crear una función que reciba un número y devuelva una cadena
# formada por esa cantidad de asteriscos.
# Entrada: 5
# Salida: "*****"
# =====================================================================

# ---------- Forma 1: usando multiplicación de strings ----------
def num_a_asteric1(num):
    return '*' * num

# ---------- Forma 2: usando un bucle for ----------
def num_a_asteric2(num):
    resultado = ''
    for _ in range(num):
        resultado += '*'
    return resultado

# ---------- Forma 3: usando join con list comprehension ----------
def num_a_asteric3(num):
    return ''.join(['*' for _ in range(num)])

# ---------- Forma 4: usando while ----------
def num_a_asteric4(num):
    resultado = ''
    contador = 0
    while contador < num:
        resultado += '*'
        contador += 1
    return resultado

# ---------- Forma 5: usando recursion ----------
def num_a_asteric5(num):
    if num <= 0:
        return ''
    return '*' + num_a_asteric5(num - 1)

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    numero_input = int(input("Ingrese un número: "))

    print("\nForma 1:", num_a_asteric1(numero_input))
    print("Forma 2:", num_a_asteric2(numero_input))
    print("Forma 3:", num_a_asteric3(numero_input))
    print("Forma 4:", num_a_asteric4(numero_input))
    print("Forma 5:", num_a_asteric5(numero_input))
