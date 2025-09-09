# =====================================================================
# EJERCICIO 24: Serie de Fibonacci
# ---------------------------------------------------------------------
# Solicitar al usuario la cantidad de elementos o hasta qué valor 
# desea visualizar de la serie de Fibonacci.
# =====================================================================

# ---------- Forma 1: iterativa con dos variables ----------
def fibonacci1(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=", " if i < n-1 else "\n")
        a, b = b, a + b

# ---------- Forma 2: usando lista y append ----------
def fibonacci2(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    print(", ".join(map(str, fib[:n])))

# ---------- Forma 3: usando recursión ----------
def fibonacci_rec(n):
    def fib_rec(i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            return fib_rec(i-1) + fib_rec(i-2)
    serie = [fib_rec(i) for i in range(n)]
    print(", ".join(map(str, serie)))

# ---------- Forma 4: usando while ----------
def fibonacci4(n):
    a, b = 0, 1
    i = 0
    while i < n:
        print(a, end=", " if i < n-1 else "\n")
        a, b = b, a + b
        i += 1

# ---------- Forma 5: hasta alcanzar un valor máximo ----------
def fibonacci5(max_val):
    a, b = 0, 1
    while a <= max_val:
        print(a, end=", " if a != b else "\n")
        a, b = b, a + b

# =====================================================================
# Ejecución
# =====================================================================
if __name__ == "__main__":
    n = int(input("Ingrese cuántos elementos de la serie de Fibonacci desea ver: "))
    # Descomentar la función que quieras probar
    # fibonacci1(n)
    # fibonacci2(n)
    # fibonacci_rec(n)
    # fibonacci4(n)
    # fibonacci5(n)  # en este caso pedir un valor máximo en vez de cantidad
