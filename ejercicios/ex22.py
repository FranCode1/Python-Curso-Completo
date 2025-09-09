# =====================================================================
# EJERCICIO 22: Suma y promedio de números
# ---------------------------------------------------------------------
# Solicitar una lista de números hasta que el usuario ingrese 'FIN'.
# Al finalizar mostrar:
# - La suma de los números ingresados
# - El promedio de los números ingresados
# =====================================================================

# ---------- Forma 1: usando while ----------
def suma_promedio1():
    suma = 0
    cantidad = 0
    while True:
        entrada = input("Ingrese un número (o 'FIN' para terminar): ")
        if entrada.upper() == "FIN":
            break
        try:
            num = float(entrada)
            suma += num
            cantidad += 1
        except ValueError:
            print("❌ Ingrese un número válido.")
    if cantidad > 0:
        print(f"Suma: {suma}, Promedio: {suma/cantidad}")
    else:
        print("No se ingresaron números.")

# ---------- Forma 2: usando lista ----------
def suma_promedio2():
    numeros = []
    while True:
        entrada = input("Ingrese un número (o 'FIN' para terminar): ")
        if entrada.upper() == "FIN":
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print("❌ Ingrese un número válido.")
    if numeros:
        print(f"Suma: {sum(numeros)}, Promedio: {sum(numeros)/len(numeros)}")
    else:
        print("No se ingresaron números.")

# ---------- Forma 3: usando for infinito ----------
def suma_promedio3():
    numeros = []
    for _ in iter(int, 1):  # bucle infinito
        entrada = input("Ingrese un número (o 'FIN' para terminar): ")
        if entrada.upper() == "FIN":
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print("❌ Ingrese un número válido.")
    print(f"Suma: {sum(numeros)}, Promedio: {sum(numeros)/len(numeros) if numeros else 0}")

# ---------- Forma 4: usando función auxiliar ----------
def obtener_numeros():
    numeros = []
    while True:
        entrada = input("Ingrese un número (o 'FIN' para terminar): ")
        if entrada.upper() == "FIN":
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print("❌ Ingrese un número válido.")
    return numeros

def suma_promedio4():
    numeros = obtener_numeros()
    if numeros:
        print(f"Suma: {sum(numeros)}, Promedio: {sum(numeros)/len(numeros)}")
    else:
        print("No se ingresaron números.")

# ---------- Forma 5: usando map() y split() para ingresar múltiples números ----------
def suma_promedio5():
    entrada = input("Ingrese números separados por espacio: ")
    try:
        numeros = list(map(float, entrada.split()))
        print(f"Suma: {sum(numeros)}, Promedio: {sum(numeros)/len(numeros) if numeros else 0}")
    except ValueError:
        print("❌ Ingrese solo números válidos.")

# =====================================================================
# Ejecución
# =====================================================================
if __name__ == "__main__":
    # Descomentar la función que quieras probar
    # suma_promedio1()
    # suma_promedio2()
    # suma_promedio3()
    # suma_promedio4()
    suma_promedio5()
