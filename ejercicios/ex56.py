# =====================================================================
# EJERCICIO 56: Aproximación de Pi usando la serie de Leibniz
# ---------------------------------------------------------------------
# Calcular x usando la siguiente suma infinita:
# x = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
# La entrada del programa es un número entero que indica
# cuántos términos se usarán en la suma.
# =====================================================================

# ---------- Forma 1: Con contador y bucle for ----------
def pi_1():
    n = int(input("Ingrese la cantidad de términos: "))
    suma = 0
    contador = 1
    for i in range(1, n * 2, 2):
        if contador % 2 == 0:
            suma -= 1 / i
        else:
            suma += 1 / i
        contador += 1
    resultado = 4 * suma
    print(f"[Forma 1] Aproximación de Pi: {resultado}")

# ---------- Forma 2: Usando signo alternante ----------
def pi_2():
    n = int(input("Ingrese la cantidad de términos: "))
    suma = 0
    for i in range(n):
        signo = (-1) ** i
        suma += signo / (2 * i + 1)
    resultado = 4 * suma
    print(f"[Forma 2] Aproximación de Pi: {resultado}")

# ---------- Forma 3: Usando while ----------
def pi_3():
    n = int(input("Ingrese la cantidad de términos: "))
    suma = 0
    i = 0
    while i < n:
        if i % 2 == 0:
            suma += 1 / (2 * i + 1)
        else:
            suma -= 1 / (2 * i + 1)
        i += 1
    resultado = 4 * suma
    print(f"[Forma 3] Aproximación de Pi: {resultado}")

# ---------- Forma 4: Función auxiliar ----------
def termino_leibniz(i):
    signo = (-1) ** i
    return signo / (2 * i + 1)

def pi_4():
    n = int(input("Ingrese la cantidad de términos: "))
    suma = sum(termino_leibniz(i) for i in range(n))
    resultado = 4 * suma
    print(f"[Forma 4] Aproximación de Pi: {resultado}")

# ---------- Forma 5: Con map y lambda ----------
def pi_5():
    n = int(input("Ingrese la cantidad de términos: "))
    indices = list(range(n))
    suma = sum(map(lambda i: ((-1) ** i) / (2 * i + 1), indices))
    resultado = 4 * suma
    print(f"[Forma 5] Aproximación de Pi: {resultado}")

# =====================================================
# Ejecución de las funciones
# =====================================================
if __name__ == "__main__":
    # Puedes descomentar la que quieras probar:
    # pi_1()
    # pi_2()
    # pi_3()
    # pi_4()
    pi_5()
