# ----------------------------------------------------------
# EJERCICIO 10 - Serie de Fibonacci
# ----------------------------------------------------------
# La serie comienza con 0 y 1, y cada número es la suma de los dos anteriores.
# Ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

# El usuario puede:
# A) Elegir cuántos elementos ver
# B) Ver todos los números hasta cierto valor máximo


# ============================================
# MÉTODO 1: Usando for para mostrar N elementos
# ============================================
print("\n🔹 MÉTODO 1: Mostrar N elementos (for)")

def fibonacci_n_elementos(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=", " if i < n - 1 else "\n")
        a, b = b, a + b

n1 = int(input("¿Cuántos elementos querés ver?: "))
fibonacci_n_elementos(n1)


# ============================================
# MÉTODO 2: Usando while hasta un valor máximo
# ============================================
print("\n🔹 MÉTODO 2: Hasta cierto valor (while)")

def fibonacci_hasta_valor(limite):
    a, b = 0, 1
    while a <= limite:
        print(a, end=", ")
        a, b = b, a + b
    print()  # salto de línea

limite = int(input("¿Hasta qué número mostrar la serie?: "))
fibonacci_hasta_valor(limite)


# ============================================
# MÉTODO 3: Usando listas (almacenar y mostrar)
# ============================================
print("\n🔹 MÉTODO 3: Guardar en una lista")

def fibonacci_lista(n):
    serie = []
    a, b = 0, 1
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    print("Serie:", serie)

n2 = int(input("Cantidad de elementos: "))
fibonacci_lista(n2)


# ============================================
# MÉTODO 4: Recursivo (cuidado con n > 30)
# ============================================
print("\n🔹 MÉTODO 4: Recursivo (mostrar cada valor)")

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

n3 = int(input("¿Cuántos elementos querés ver? (≤30): "))
for i in range(n3):
    print(fibonacci_recursivo(i), end=", ")
print()


# ============================================
# MÉTODO 5: Generador (uso de yield)
# ============================================
print("\n🔹 MÉTODO 5: Generador con yield")

def generar_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n4 = int(input("Número de elementos a generar: "))
print("Serie:", list(generar_fibonacci(n4)))
