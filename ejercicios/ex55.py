# =====================================================================
# EJERCICIO 55: Secuencia de Collatz
# ---------------------------------------------------------------------
# Pedir al usuario un número y generar la sucesión de Collatz:
# - Si el número es par, se divide entre 2.
# - Si el número es impar, se multiplica por 3 y se le suma 1.
# - La sucesión termina cuando llega al número 1.
#
# Variantes implementadas:
#   1. collatz0 -> Versión con mensajes explicativos paso a paso.
#   2. collatz1 -> Versión simple que imprime la secuencia en línea.
#   3. collatz2 -> Versión con lista de asteriscos (modo gráfico).
#   4. collatz3 -> Versión pirámide que muestra la secuencia de
#                  todos los números desde 1 hasta el ingresado.
# =====================================================================

def collatz0():
    """Versión detallada con explicación de cada paso"""
    num = int(input("Ingrese un número: "))
    while True:
        print(f"El número actual es {num}")
        if num == 1:
            print("✅ Secuencia de Collatz terminada")
            break
        elif num % 2 == 0:
            print(f"{num} es par → se divide entre 2")
            num //= 2
        else:
            print(f"{num} es impar → se multiplica por 3 y se suma 1")
            num = num * 3 + 1

def collatz1():
    """Versión simple que muestra la secuencia en línea"""
    num = int(input("Ingrese un número: "))
    print(f"Secuencia de Collatz para {num}:")
    while True:
        print(num, end=", ")
        if num == 1:
            print("✅ Terminada")
            break
        elif num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1

def collatz2():
    """Versión con lista de asteriscos (representación gráfica)"""
    num = int(input("Ingrese un número: "))
    piramide = []
    while True:
        piramide.append("*")
        if num == 1:
            print(f"Secuencia gráfica: {''.join(piramide)}")
            print("✅ Secuencia de Collatz terminada")
            break
        elif num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1

def collatz3():
    """Versión pirámide: muestra la secuencia de todos los números
       desde 1 hasta el ingresado"""
    numeroIng = int(input("Ingrese un número: "))
    for i in range(1, numeroIng + 1):
        print(i, end=": ")
        numero = i
        while numero != 1:
            print("*", end=" ")
            if numero % 2 == 0:
                numero //= 2
            else:
                numero = numero * 3 + 1
        print("*")

# =====================================================
# Ejecución de las funciones
# (puedes comentar/descomentar la que quieras probar)
# =====================================================

# collatz0()
# collatz1()
# collatz2()
collatz3()
