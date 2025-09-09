#1. Juego del Numero Oculto:
# El programa elige un numero al azar entre 1 y 100. El usuario debe adivinarlo:
# - Le indicas si el numero ingresado es mayor o menor que el secreto.
# - Limita los intentos a 7.

# - el usuario debe adivinarlo
# - le das una pista de si el numero es mayor o menor al ingresado en cada intento
# - solo tiene 7 intentos

import random

def random_game():
    print("🎲 Bienvenido al juego de adivinar el número entre 1 y 100.")
    numero_secreto = random.randint(1, 100)
    intentos = 7
    ultimo_intento = None  

    for i in range(intentos):
        try:
            num_user = int(input(f"Intento {i+1}/{intentos} - Ingresá tu número: "))

            if num_user == numero_secreto:
                print(f"🎉 ¡Felicidades! El número era {numero_secreto}.")
                break

            elif num_user > numero_secreto:
                print("❌ Incorrecto. Tu número es más grande.")
            else:
                print("❌ Incorrecto. Tu número es más pequeño.")

            # Pista de acercamiento
            if ultimo_intento is not None:
                dif_actual = abs(numero_secreto - num_user)
                dif_anterior = abs(numero_secreto - ultimo_intento)
                if dif_actual < dif_anterior:
                    print("🔥 Estás más cerca que antes.")
                elif dif_actual > dif_anterior:
                    print("❄️ Estás más lejos que antes.")
                else:
                    print("➖ Estás igual de lejos que antes.")

            ultimo_intento = num_user

        except ValueError:
            print("⚠️ Por favor ingresá un número válido.")

    else:
        print(f"😢 Se acabaron los intentos. El número era {numero_secreto}.")

# Ejecución
random_game()
