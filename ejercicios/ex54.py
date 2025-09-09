# ================================================================
# EJERCICIO 54: Validación de DNI
# ---------------------------------------------------------------
# Requisitos:
# - Solo debe contener números
# - Debe tener entre 7 y 8 dígitos
# - No debe comenzar con 0
# ================================================================


# 🔹 MÉTODO 1: Validación paso a paso
dni = input("Método 1 - Ingresá tu DNI: ")

if not dni.isdigit():
    print("❌ El DNI debe ser numérico.")
elif len(dni) < 7 or len(dni) > 8:
    print("❌ El DNI debe tener entre 7 y 8 dígitos.")
elif dni[0] == "0":
    print("❌ El DNI no puede comenzar con 0.")
else:
    print("✅ DNI válido.")


# 🔹 MÉTODO 2: Función que devuelve True/False
def validar_dni(dni):
    return dni.isdigit() and 7 <= len(dni) <= 8 and dni[0] != "0"

dni2 = input("\nMétodo 2 - Ingresá tu DNI: ")
print("✅ DNI válido." if validar_dni(dni2) else "❌ DNI inválido.")


# 🔹 MÉTODO 3: Función que devuelve mensaje personalizado
def verificar_dni(dni):
    if not dni.isdigit():
        return "❌ Solo se permiten números"
    if len(dni) < 7 or len(dni) > 8:
        return "❌ El DNI debe tener 7 u 8 cifras"
    if dni[0] == "0":
        return "❌ No puede empezar con 0"
    return "✅ DNI correcto"

dni3 = input("\nMétodo 3 - Ingresá tu DNI: ")
print(verificar_dni(dni3))


# 🔹 MÉTODO 4: Ternario anidado
dni4 = input("\nMétodo 4 - Ingresá tu DNI: ")
print("✅ Válido" if dni4.isdigit() and 7 <= len(dni4) <= 8 and dni4[0] != "0" else "❌ Inválido")


# 🔹 MÉTODO 5: Bucle hasta que sea correcto
while True:
    dni5 = input("\nMétodo 5 - Ingresá tu DNI: ")
    if dni5.isdigit() and 7 <= len(dni5) <= 8 and dni5[0] != "0":
        print("✅ DNI aceptado.")
        break
    else:
        print("❌ DNI inválido. Recordá: debe ser numérico, con 7 u 8 cifras y sin empezar en 0.")
