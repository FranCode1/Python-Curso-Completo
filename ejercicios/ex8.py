# ----------------------------------------------------------
# EJERCICIO 8 - Sumar del 1 hasta un número ingresado
# ----------------------------------------------------------
# Solicitar un número positivo y mostrar la suma entre 1 y ese número
# Ejemplo: si el número es 5, mostrar 1+2+3+4+5 = 15

# ========== MÉTODO 1: for con acumulador ==========
print("\n🔹 MÉTODO 1: for con acumulador")

num = int(input("Ingresá un número positivo: "))
total = 0
for i in range(1, num + 1):
    total += i
print(f"La suma de 1 a {num} es: {total}")


# ========== MÉTODO 2: usando la fórmula matemática ==========
print("\n🔹 MÉTODO 2: Fórmula suma de Gauss")

num2 = int(input("Número positivo: "))
suma = num2 * (num2 + 1) // 2  # // para asegurar entero
print(f"La suma de 1 a {num2} es: {suma}")


# ========== MÉTODO 3: función para sumar ==========
print("\n🔹 MÉTODO 3: Función personalizada")

def suma_rango(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

num3 = int(input("Número positivo: "))
print(f"La suma de 1 a {num3} es: {suma_rango(num3)}")


# ========== MÉTODO 4: usando sum() y range() ==========
print("\n🔹 MÉTODO 4: sum + range")

num4 = int(input("Número positivo: "))
resultado = sum(range(1, num4 + 1))
print(f"La suma de 1 a {num4} es: {resultado}")


# ========== MÉTODO 5: usando recursividad ==========
print("\n🔹 MÉTODO 5: recursivo")

def suma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + suma_recursiva(n - 1)

num5 = int(input("Número positivo: "))
print(f"La suma de 1 a {num5} es: {suma_recursiva(num5)}")
