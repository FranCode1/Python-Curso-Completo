# ================================================================
# EJERCICIO 52: Control de entradas
# ---------------------------------------------------------------
# Validar código de ticket que cumpla:
# - Empieza con 2 letras mayúsculas
# - Sigue con 4 dígitos
# Ejemplo válido: AB1234
# ================================================================


# 🔹 MÉTODO 1: Validación paso a paso
codigo = input("Método 1 - Ingresá el código de ticket: ")

if len(codigo) != 6:
    print("❌ El código debe tener exactamente 6 caracteres.")
elif not codigo[:2].isalpha() or not codigo[:2].isupper():
    print("❌ Los dos primeros caracteres deben ser letras mayúsculas.")
elif not codigo[2:].isdigit():
    print("❌ Los últimos 4 caracteres deben ser dígitos.")
else:
    print("✅ Código válido.")


# 🔹 MÉTODO 2: Función que valida y devuelve True/False
def validar_ticket(cod):
    return (
        len(cod) == 6 and
        cod[:2].isalpha() and cod[:2].isupper() and
        cod[2:].isdigit()
    )

codigo2 = input("\nMétodo 2 - Ingresá el código de ticket: ")
print("✅ Código válido." if validar_ticket(codigo2) else "❌ Código inválido.")


# 🔹 MÉTODO 3: Función con mensajes personalizados
def analizar_ticket(cod):
    if len(cod) != 6:
        return "❌ Debe tener 6 caracteres"
    if not cod[:2].isalpha() or not cod[:2].isupper():
        return "❌ Debe comenzar con 2 letras mayúsculas"
    if not cod[2:].isdigit():
        return "❌ Debe continuar con 4 números"
    return "✅ Código válido"

codigo3 = input("\nMétodo 3 - Ingresá el código de ticket: ")
print(analizar_ticket(codigo3))


# 🔹 MÉTODO 4: Validación con ternario
codigo4 = input("\nMétodo 4 - Ingresá el código de ticket: ")
print(
    "✅ Válido" if (
        len(codigo4) == 6 and
        codigo4[:2].isalpha() and codigo4[:2].isupper() and
        codigo4[2:].isdigit()
    ) else "❌ Inválido"
)


# 🔹 MÉTODO 5: Repetir hasta que sea válido
while True:
    codigo5 = input("\nMétodo 5 - Ingresá el código de ticket: ")
    if (
        len(codigo5) == 6 and
        codigo5[:2].isalpha() and codigo5[:2].isupper() and
        codigo5[2:].isdigit()
    ):
        print("✅ Código aceptado.")
        break
    else:
        print("❌ Formato incorrecto. Ejemplo válido: AB1234")
