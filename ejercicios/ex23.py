# =====================================================================
# EJERCICIO 23: Número más grande y más chico
# ---------------------------------------------------------------------
# Solicitar 5 números al usuario y mostrar:
# - El número más grande
# - El número más chico
# =====================================================================

# ---------- Forma 1: usando lista y max()/min() ----------
def mayor_menor1():
    numeros = []
    for i in range(5):
        numeros.append(float(input(f"Ingrese el número {i+1}: ")))
    print(f"Números ingresados: {numeros}")
    print(f"Mayor: {max(numeros)}, Menor: {min(numeros)}")

# ---------- Forma 2: usando variables independientes ----------
def mayor_menor2():
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))
    n3 = float(input("Ingrese el tercer número: "))
    n4 = float(input("Ingrese el cuarto número: "))
    n5 = float(input("Ingrese el quinto número: "))
    mayor = max(n1, n2, n3, n4, n5)
    menor = min(n1, n2, n3, n4, n5)
    print(f"Mayor: {mayor}, Menor: {menor}")

# ---------- Forma 3: usando bucle con variables temporales ----------
def mayor_menor3():
    mayor = float('-inf')
    menor = float('inf')
    for i in range(5):
        num = float(input(f"Ingrese el número {i+1}: "))
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
    print(f"Mayor: {mayor}, Menor: {menor}")

# ---------- Forma 4: usando lista y sorted() ----------
def mayor_menor4():
    numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(5)]
    numeros_ordenados = sorted(numeros)
    print(f"Números ingresados: {numeros}")
    print(f"Menor: {numeros_ordenados[0]}, Mayor: {numeros_ordenados[-1]}")

# ---------- Forma 5: usando diccionario con etiquetas ----------
def mayor_menor5():
    etiquetas = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
    numeros = {}
    for etiqueta in etiquetas:
        numeros[etiqueta] = float(input(f"Ingrese el {etiqueta} número: "))
    max_etiqueta = max(numeros, key=numeros.get)
    min_etiqueta = min(numeros, key=numeros.get)
    print(f"Números ingresados: {numeros}")
    print(f"Mayor: {numeros[max_etiqueta]} ({max_etiqueta})")
    print(f"Menor: {numeros[min_etiqueta]} ({min_etiqueta})")

# =====================================================================
# Ejecución
# =====================================================================
if __name__ == "__main__":
    # Descomentar la función que quieras probar
    # mayor_menor1()
    # mayor_menor2()
    # mayor_menor3()
    # mayor_menor4()
    mayor_menor5()
