# ================================================================
# EJERCICIO 51: Verificar código alfanumérico
# ---------------------------------------------------------------
# Requisitos del código de acceso:
# - Debe tener exactamente 6 caracteres
# - Debe ser alfanumérico (solo letras y números)
# - Debe tener al menos una letra y al menos un número
# ================================================================


# 🔹 MÉTODO 1: Validaciones paso a paso
codigo = input("Método 1 - Ingrese el código: ")

if len(codigo) != 6:
    print("❌ El código debe tener exactamente 6 caracteres.")
elif not codigo.isalnum():
    print("❌ El código debe ser alfanumérico.")
elif not any(c.isalpha() for c in codigo):
    print("❌ El código debe contener al menos una letra.")
elif not any(c.isdigit() for c in codigo):
    print("❌ El código debe contener al menos un número.")
else:
    print("✅ Código válido.")


# 🔹 MÉTODO 2: Función que devuelve True/False
def validar_codigo(cod):
    if len(cod) != 6:
        return False
    if not cod.isalnum():
        return False
    if not any(c.isalpha() for c in cod):
        return False
    if not any(c.isdigit() for c in cod):
        return False
    return True

codigo2 = input("\nMétodo 2 - Ingrese el código: ")
print("✅ Código válido." if validar_codigo(codigo2) else "❌ Código inválido.")


# 🔹 MÉTODO 3: Función que devuelve mensaje personalizado
def verificar_codigo(cod):
    if len(cod) != 6:
        return "❌ Debe tener 6 caracteres"
    if not cod.isalnum():
        return "❌ Solo se permiten letras y números"
    if not any(c.isalpha() for c in cod):
        return "❌ Falta al menos una letra"
    if not any(c.isdigit() for c in cod):
        return "❌ Falta al menos un número"
    return "✅ Código válido"

codigo3 = input("\nMétodo 3 - Ingrese el código: ")
print(verificar_codigo(codigo3))


# 🔹 MÉTODO 4: Todo en una sola línea con ternario
codigo4 = input("\nMétodo 4 - Ingrese el código: ")
print("✅ Código válido" if len(codigo4) == 6 and codigo4.isalnum()
      and any(c.isalpha() for c in codigo4)
      and any(c.isdigit() for c in codigo4) else "❌ Código inválido")


# 🔹 MÉTODO 5: Repetir hasta que sea válido
while True:
    codigo5 = input("\nMétodo 5 - Ingrese el código: ")
    if (len(codigo5) == 6 and codigo5.isalnum()
            and any(c.isalpha() for c in codigo5)
            and any(c.isdigit() for c in codigo5)):
        print("✅ Código aceptado")
        break
    else:
        print("❌ Código inválido, intentá de nuevo.")
