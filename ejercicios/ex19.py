# =====================================================================
# EJERCICIO 19: Clasificación de triángulos
# ---------------------------------------------------------------------
# Pedir al usuario tres lados de un triángulo y mostrar si es:
# - Equilátero (todos iguales)
# - Isósceles (dos iguales)
# - Escaleno (todos diferentes)
# =====================================================================

# ---------- Forma 1: usando if/elif clásico ----------
def triangulo1():
    a = float(input("Ingresar primer lado: "))
    b = float(input("Ingresar segundo lado: "))
    c = float(input("Ingresar tercer lado: "))

    if a == b == c:
        print("Es un triángulo equilátero")
    elif a == b or a == c or b == c:
        print("Es un triángulo isósceles")
    elif a != b and a != c and b != c:
        print("Es un triángulo escaleno")
    else:
        print("Valores ingresados incorrectos")

# ---------- Forma 2: usando sets ----------
def triangulo2():
    lados = [float(input(f"Ingresar lado {i+1}: ")) for i in range(3)]
    tipos = {len(set(lados)): "equilátero" if len(set(lados)) == 1 else "isósceles" if len(set(lados)) == 2 else "escaleno"}
    print(f"Es un triángulo {tipos[len(set(lados))]}")

# ---------- Forma 3: usando listas y contadores ----------
def triangulo3():
    lados = [float(input(f"Ingresar lado {i+1}: ")) for i in range(3)]
    repeticiones = [lados.count(lado) for lado in lados]

    if max(repeticiones) == 3:
        print("Es un triángulo equilátero")
    elif max(repeticiones) == 2:
        print("Es un triángulo isósceles")
    else:
        print("Es un triángulo escaleno")

# ---------- Forma 4: usando diccionario ----------
def triangulo4():
    lados = {"a": float(input("Lado a: ")),
             "b": float(input("Lado b: ")),
             "c": float(input("Lado c: "))}

    valores = list(lados.values())
    if valores[0] == valores[1] == valores[2]:
        print("Es un triángulo equilátero")
    elif valores[0] == valores[1] or valores[0] == valores[2] or valores[1] == valores[2]:
        print("Es un triángulo isósceles")
    else:
        print("Es un triángulo escaleno")

# ---------- Forma 5: usando operadores ternarios ----------
def triangulo5():
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))

    tipo = "equilátero" if a == b == c else "isósceles" if a == b or a == c or b == c else "escaleno"
    print(f"Es un triángulo {tipo}")

# =====================================================================
# Ejecución
# =====================================================================
if __name__ == "__main__":
    # Descomentar la función que quieras probar
    # triangulo1()
    # triangulo2()
    # triangulo3()
    # triangulo4()
    triangulo5()
