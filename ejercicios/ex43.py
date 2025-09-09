# =====================================================================
# EJERCICIO 43: Simulación de Cajero Automático
# ---------------------------------------------------------------------
# Simular el funcionamiento de un cajero automático que:
# 1. Pide un PIN (1234) con hasta 3 intentos.
# 2. Si el PIN es correcto, muestra un menú:
#    - Consultar saldo
#    - Depositar
#    - Extraer (solo si hay fondos suficientes)
#    - Salir
# 3. Usar variables para el saldo, funciones para cada operación,
#    y while para controlar el menú.
# =====================================================================

# ---------- Forma 1: básico, con while ----------
def cajero_1():
    saldo = 0
    intentos = 0
    while intentos < 3:
        pin = input("Ingrese el PIN: ")
        if pin == "1234":
            print("PIN correcto.")
            break
        else:
            print("PIN incorrecto.")
            intentos += 1
    else:
        print("Se agotaron los intentos.")
        return

    while True:
        print("\n--- MENÚ ---")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Extraer")
        print("4 - Salir")
        opcion = input("Seleccione una acción: ")

        if opcion == "1":
            print(f"Saldo: ${saldo}")
        elif opcion == "2":
            monto = float(input("Ingrese monto a depositar: "))
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
        elif opcion == "3":
            monto = float(input("Ingrese monto a extraer: "))
            if monto <= saldo:
                saldo -= monto
                print(f"Extracción exitosa. Saldo restante: ${saldo}")
            else:
                print("Fondos insuficientes.")
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break
        else:
            print("Opción inválida.")

# ---------- Forma 2: usando funciones por operación ----------
def consultar_saldo(saldo):
    print(f"Saldo: ${saldo}")
    return saldo

def depositar(saldo):
    monto = float(input("Ingrese monto a depositar: "))
    saldo += monto
    print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
    return saldo

def extraer(saldo):
    monto = float(input("Ingrese monto a extraer: "))
    if monto <= saldo:
        saldo -= monto
        print(f"Extracción exitosa. Saldo restante: ${saldo}")
    else:
        print("Fondos insuficientes.")
    return saldo

def cajero_2():
    saldo = 0
    intentos = 0
    while intentos < 3:
        pin = input("Ingrese el PIN: ")
        if pin == "1234":
            print("PIN correcto.")
            break
        else:
            print("PIN incorrecto.")
            intentos += 1
    else:
        print("Se agotaron los intentos.")
        return

    while True:
        print("\n--- MENÚ ---")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Extraer")
        print("4 - Salir")
        opcion = input("Seleccione una acción: ")

        if opcion == "1":
            saldo = consultar_saldo(saldo)
        elif opcion == "2":
            saldo = depositar(saldo)
        elif opcion == "3":
            saldo = extraer(saldo)
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break
        else:
            print("Opción inválida.")

# ---------- Forma 3: menú con diccionario ----------
def cajero_3():
    saldo = 0
    pin = input("Ingrese PIN: ")
    if pin != "1234":
        print("PIN incorrecto. Fin del programa.")
        return

    def menu():
        print("\n--- MENÚ ---")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Extraer")
        print("4 - Salir")
        return input("Seleccione una acción: ")

    opciones = {
        "1": lambda s: print(f"Saldo: ${s}") or s,
        "2": lambda s: (s + float(input("Monto a depositar: "))),
        "3": lambda s: s - float(input("Monto a extraer: ")) if float(input("Monto a extraer: ")) <= s else print("Fondos insuficientes.") or s,
    }

    while True:
        eleccion = menu()
        if eleccion == "4":
            print("Gracias por usar el cajero.")
            break
        saldo = opciones.get(eleccion, lambda s: print("Opción inválida.") or s)(saldo)

# ---------- Forma 4: usando for para intentos ----------
def cajero_4():
    saldo = 0
    for intento in range(3):
        pin = input("Ingrese PIN: ")
        if pin == "1234":
            print("PIN correcto.")
            break
        else:
            print("PIN incorrecto.")
    else:
        print("Se agotaron los intentos.")
        return

    opciones = ["1", "2", "3", "4"]
    while True:
        print("\n--- MENÚ ---")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Extraer")
        print("4 - Salir")
        opcion = input("Seleccione acción: ")
        if opcion not in opciones:
            print("Opción inválida.")
            continue
        if opcion == "1":
            print(f"Saldo: ${saldo}")
        elif opcion == "2":
            saldo += float(input("Monto a depositar: "))
        elif opcion == "3":
            monto = float(input("Monto a extraer: "))
            if monto <= saldo:
                saldo -= monto
            else:
                print("Fondos insuficientes.")
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break

# ---------- Forma 5: con while True y break para todo ----------
def cajero_5():
    saldo = 0
    intentos = 0
    while True:
        pin = input("Ingrese PIN: ")
        if pin == "1234":
            print("PIN correcto.")
            break
        else:
            print("PIN incorrecto.")
            intentos += 1
            if intentos >= 3:
                print("Se agotaron los intentos.")
                return

    while True:
        opcion = input("\n1-Consultar saldo\n2-Depositar\n3-Extraer\n4-Salir\nSeleccione acción: ")
        if opcion == "1":
            print(f"Saldo: ${saldo}")
        elif opcion == "2":
            saldo += float(input("Monto a depositar: "))
            print(f"Nuevo saldo: ${saldo}")
        elif opcion == "3":
            monto = float(input("Monto a extraer: "))
            if monto <= saldo:
                saldo -= monto
                print(f"Extracción exitosa. Saldo restante: ${saldo}")
            else:
                print("Fondos insuficientes.")
        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break
        else:
            print("Opción inválida.")

# =====================================================
# Ejecución del programa
# =====================================================
if __name__ == "__main__":
    # Descomentar la forma que quieras probar
    # cajero_1()
    # cajero_2()
    # cajero_3()
    # cajero_4()
    cajero_5()
