
# ======================================================
# Ejercicio #2 - Sistema de precios (5 formas distintas)

#2. Sistema de precios.
# Escribir un programa que solicite al usuario los precios de un producto de almacen de distintos comercios hasta que introduzca un precio negativo. Luego el programa debe imprimir el promedio, el precio mas bajo y el precio mas bajo y el precio mas alto.

# Autor: Franco Lugo
# ======================================================

# ---------- Forma 1: Usando lista y funciones básicas ----------
def sistema_precios_lista():
    precios = []
    while True:
        precio = float(input("Ingrese un precio (negativo para terminar): "))
        if precio < 0:
            break
        precios.append(precio)
    if precios:
        print("\n[Forma 1]")
        print("Promedio:", sum(precios) / len(precios))
        print("Mínimo:", min(precios))
        print("Máximo:", max(precios))

# ---------- Forma 2: Usando variables acumuladoras ----------
def sistema_precios_acumuladores():
    suma = 0
    contador = 0
    minimo = float("inf")
    maximo = float("-inf")
    while True:
        precio = float(input("Ingrese un precio (negativo para terminar): "))
        if precio < 0:
            break
        suma += precio
        contador += 1
        if precio < minimo:
            minimo = precio
        if precio > maximo:
            maximo = precio
    if contador > 0:
        print("\n[Forma 2]")
        print("Promedio:", suma / contador)
        print("Mínimo:", minimo)
        print("Máximo:", maximo)

# ---------- Forma 3: Usando while con try/except ----------
def sistema_precios_try():
    precios = []
    while True:
        try:
            precio = float(input("Ingrese un precio (negativo para terminar): "))
            if precio < 0:
                break
            precios.append(precio)
        except ValueError:
            print("Error: ingrese un número válido.")
    if precios:
        print("\n[Forma 3]")
        print("Promedio:", sum(precios) / len(precios))
        print("Mínimo:", min(precios))
        print("Máximo:", max(precios))

# ---------- Forma 4: Usando funciones separadas ----------
def pedir_precios():
    precios = []
    while True:
        precio = float(input("Ingrese un precio (negativo para terminar): "))
        if precio < 0:
            break
        precios.append(precio)
    return precios

def calcular_resultados(precios):
    return sum(precios) / len(precios), min(precios), max(precios)

def sistema_precios_funciones():
    precios = pedir_precios()
    if precios:
        promedio, minimo, maximo = calcular_resultados(precios)
        print("\n[Forma 4]")
        print("Promedio:", promedio)
        print("Mínimo:", minimo)
        print("Máximo:", maximo)

# ---------- Forma 5: Usando lista por comprensión ----------
def sistema_precios_comprehension():
    print("\n[Forma 5]")
    precios = []
    precio = 0
    while precio >= 0:
        precio = float(input("Ingrese un precio (negativo para terminar): "))
        if precio >= 0:
            precios.append(precio)
    if precios:
        promedio = sum(precios) / len(precios)
        minimo = min(precios)
        maximo = max(precios)
        print("Promedio:", promedio)
        print("Mínimo:", minimo)
        print("Máximo:", maximo)

# ======================================================
# Ejecución del programa
# ======================================================
if __name__ == "__main__":
    sistema_precios_lista()
    sistema_precios_acumuladores()
    sistema_precios_try()
    sistema_precios_funciones()
    sistema_precios_comprehension()
