# =====================================================================
# EJERCICIO 41: Juego Adivinar Número
# ---------------------------------------------------------------------
# Crear un juego donde la computadora elija un número entre 1 y 10 (usar random)
# y el usuario tenga 3 intentos. Por cada intento, mostrar si el número ingresado
# es mayor o menor que el número secreto. Opcionalmente, indicar si se acerca o se aleja.
# Todo encapsulado en funciones.
# =====================================================================

import random

# ---------- Forma 1: básica ----------
def adivinar_1():
    numero_secreto = random.randint(1, 10)
    intentos = 3

    for i in range(intentos):
        try:
            num_user = int(input(f"Intento {i+1}/{intentos}: "))
            if num_user == numero_secreto:
                print(f"🎉 ¡Felicidades! Era {numero_secreto}.")
                break
            elif num_user > numero_secreto:
                print("❌ Tu número es mayor.")
            else:
                print("❌ Tu número es menor.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")
    else:
        print(f"😢 Se acabaron los intentos. Número secreto: {numero_secreto}.")

# ---------- Forma 2: con pistas de cercanía ----------
def adivinar_2():
    numero_secreto = random.randint(1, 10)
    intentos = 3
    ultimo_intento = None

    for i in range(intentos):
        try:
            num_user = int(input(f"Intento {i+1}/{intentos}: "))
            if num_user == numero_secreto:
                print(f"🎉 ¡Correcto! Era {numero_secreto}.")
                break
            elif num_user > numero_secreto:
                print("❌ Mayor que el número secreto.")
            else:
                print("❌ Menor que el número secreto.")

            if ultimo_intento is not None:
                if abs(numero_secreto - num_user) < abs(numero_secreto - ultimo_intento):
                    print("🔥 Estás más cerca.")
                elif abs(numero_secreto - num_user) > abs(numero_secreto - ultimo_intento):
                    print("❄️ Estás más lejos.")
            ultimo_intento = num_user
        except ValueError:
            print("⚠️ Número inválido.")
    else:
        print(f"😢 Intentos agotados. Número secreto: {numero_secreto}.")

# ---------- Forma 3: usando función para pista ----------
def dar_pista(secreto, intento):
    if intento > secreto:
        return "❌ Mayor"
    elif intento < secreto:
        return "❌ Menor"
    else:
        return "🎉 Correcto"

def adivinar_3():
    numero_secreto = random.randint(1, 10)
    intentos = 3
    ultimo_intento = None

    for i in range(intentos):
        try:
            num_user = int(input(f"Intento {i+1}/{intentos}: "))
            pista = dar_pista(numero_secreto, num_user)
            print(pista)
            if pista == "🎉 Correcto":
                break
            if ultimo_intento is not None:
                if abs(numero_secreto - num_user) < abs(numero_secreto - ultimo_intento):
                    print("🔥 Más cerca")
                elif abs(numero_secreto - num_user) > abs(numero_secreto - ultimo_intento):
                    print("❄️ Más lejos")
            ultimo_intento = num_user
        except ValueError:
            print("⚠️ Número inválido.")
    else:
        print(f"😢 Número secreto era: {numero_secreto}.")

# ---------- Forma 4: con while ----------
def adivinar_4():
    numero_secreto = random.randint(1, 10)
    intentos = 3
    count = 0
    ultimo_intento = None

    while count < intentos:
        try:
            num_user = int(input(f"Intento {count+1}/{intentos}: "))
            if num_user == numero_secreto:
                print(f"🎉 Correcto! Número secreto {numero_secreto}")
                break
            elif num_user > numero_secreto:
                print("❌ Mayor")
            else:
                print("❌ Menor")

            if ultimo_intento is not None:
                if abs(numero_secreto - num_user) < abs(numero_secreto - ultimo_intento):
                    print("🔥 Más cerca")
                elif abs(numero_secreto - num_user) > abs(numero_secreto - ultimo_intento):
                    print("❄️ Más lejos")
            ultimo_intento = num_user
            count += 1
        except ValueError:
            print("⚠️ Número inválido")
    else:
        print(f"😢 Se acabaron los intentos. Número secreto: {numero_secreto}")

# ---------- Forma 5: versión con mensaje final detallado ----------
def adivinar_5():
    numero_secreto = random.randint(1, 10)
    intentos = 3
    ultimo_intento = None
    exito = False

    for i in range(intentos):
        try:
            num_user = int(input(f"Intento {i+1}/{intentos}: "))
            if num_user == numero_secreto:
                exito = True
                print(f"🎉 ¡Acertaste! Número secreto: {numero_secreto}")
                break
            elif num_user > numero_secreto:
                print("❌ Número mayor")
            else:
                print("❌ Número menor")

            if ultimo_intento is not None:
                diff_actual = abs(numero_secreto - num_user)
                diff_anterior = abs(numero_secreto - ultimo_intento)
                if diff_actual < diff_anterior:
                    print("🔥 Más cerca que antes")
                elif diff_actual > diff_anterior:
                    print("❄️ Más lejos que antes")
                else:
                    print("- Igual de lejos que antes")
            ultimo_intento = num_user
        except ValueError:
            print("⚠️ Número inválido")
    if not exito:
        print(f"😢 Fin de intentos. Número secreto: {numero_secreto}")

# =====================================================================
# Ejecución del programa
# =====================================================================
if __name__ == "__main__":
    # Descomentar la forma que quieras probar
    # adivinar_1()
    # adivinar_2()
    # adivinar_3()
    # adivinar_4()
    adivinar_5()
