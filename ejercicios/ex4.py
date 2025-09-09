# ----------------------------------------
# EJERCICIO 4 - Adivinar el número 10
# ----------------------------------------
# El usuario ingresa números al azar hasta acertar el número 10.
# Al acertar, se muestra "Ganaste" y la cantidad de intentos.

# ========== MÉTODO 1: while clásico ==========
print("\n🔹 MÉTODO 1: while clásico")

intentos = 0
numero = 0

while numero != 10:
    numero = int(input("Ingrese un número: "))
    intentos += 1

print(f"Ganaste en {intentos} intento(s)!")


# ========== MÉTODO 2: función que encapsula la lógica ==========
print("\n🔹 MÉTODO 2: función con retorno de intentos")

def adivinar_10():
    contador = 0
    while True:
        valor = int(input("Número: "))
        contador += 1
        if valor == 10:
            return contador

intentos2 = adivinar_10()
print(f"Ganaste en {intentos2} intento(s)!")


# ========== MÉTODO 3: usando break ==========
print("\n🔹 MÉTODO 3: while con break")

intentos3 = 0

while True:
    intento = int(input("Probá un número: "))
    intentos3 += 1
    if intento == 10:
        break

print(f"Ganaste en {intentos3} intento(s)!")


# ========== MÉTODO 4: recursividad ==========
print("\n🔹 MÉTODO 4: recursividad")

def juego_recursivo(contador=1):
    intento = int(input("Adiviná el número: "))
    if intento == 10:
        return contador
    return juego_recursivo(contador + 1)

print(f"Ganaste en {juego_recursivo()} intento(s)!")


# ========== MÉTODO 5: usando match-case (Python 3.10+) ==========
print("\n🔹 MÉTODO 5: match-case")

intentos5 = 0
numero5 = 0

while True:
    numero5 = int(input("Número: "))
    intentos5 += 1

    match numero5:
        case 10:
            print(f"Ganaste en {intentos5} intento(s)!")
            break
        case _:
            continue
