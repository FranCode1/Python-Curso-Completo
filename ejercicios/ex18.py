# =====================================================================
# EJERCICIO 18: Comparar tres números
# ---------------------------------------------------------------------
# Pedir al usuario tres números y mostrar:
# - Cuál es el mayor
# - Si hay números iguales, indicar cuáles
# =====================================================================

# ---------- Forma 1: usando if/elif/else clásico ----------
def comparar1():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))

    if a > b and a > c:
        print("El primer número es el mayor")
    elif b > a and b > c:
        print("El segundo número es el mayor")
    elif c > a and c > b:
        print("El tercer número es el mayor")
    elif a == b == c:
        print("Los tres números son iguales")
    elif a == b and a > c:
        print("El primer y segundo número son los mayores")
    elif b == c and b > a:
        print("El segundo y tercer número son los mayores")
    elif a == c and a > b:
        print("El primer y tercer número son los mayores")
    else:
        print("Valores ingresados incorrectos")

# ---------- Forma 2: usando max y listas ----------
def comparar2():
    numeros = [float(input("Ingrese el primer número: ")),
               float(input("Ingrese el segundo número: ")),
               float(input("Ingrese el tercer número: "))]
    mayor = max(numeros)
    indices = [i+1 for i, n in enumerate(numeros) if n == mayor]

    if len(set(numeros)) == 1:
        print("Los tres números son iguales")
    elif len(indices) == 1:
        print(f"El número {indices[0]} es el mayor")
    else:
        print(f"Los números {', '.join(map(str, indices))} son los mayores")

# ---------- Forma 3: usando sorted ----------
def comparar3():
    numeros = [float(input(f"Ingrese el número {i+1}: ")) for i in range(3)]
    ordenados = sorted(numeros, reverse=True)

    if ordenados[0] == ordenados[1] == ordenados[2]:
        print("Los tres números son iguales")
    elif ordenados[0] == ordenados[1]:
        print("Hay un empate en el mayor entre dos números")
    else:
        print(f"El mayor número es {ordenados[0]}")

# ---------- Forma 4: usando diccionario ----------
def comparar4():
    nums = {'a': float(input("Ingrese el primer número: ")),
            'b': float(input("Ingrese el segundo número: ")),
            'c': float(input("Ingrese el tercer número: "))}

    mayor = max(nums.values())
    ganadores = [k for k, v in nums.items() if v == mayor]

    if len(set(nums.values())) == 1:
        print("Los tres números son iguales")
    elif len(ganadores) == 1:
        print(f"El número {ganadores[0]} es el mayor")
    else:
        print(f"Los números {', '.join(ganadores)} son los mayores")

# ---------- Forma 5: usando funciones y operadores ternarios ----------
def comparar5():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))

    mayor = a if a >= b and a >= c else (b if b >= a and b >= c else c)
    iguales = []
    if a == mayor: iguales.append("primer")
    if b == mayor: iguales.append("segundo")
    if c == mayor: iguales.append("tercer")

    if len(iguales) == 3:
        print("Los tres números son iguales")
    elif len(iguales) == 1:
        print(f"El {iguales[0]} número es el mayor")
    else:
        print(f"Los números {', '.join(iguales)} son los mayores")

# =====================================================================
# Ejecución
# =====================================================================
if __name__ == "__main__":
    # Descomentar la función que quieras probar
    # comparar1()
    # comparar2()
    # comparar3()
    # comparar4()
    comparar5()
