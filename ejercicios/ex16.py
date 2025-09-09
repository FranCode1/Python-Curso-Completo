# ================================================================
# EJERCICIO 16 - Aplicar 10% de descuento si el monto supera los $10.000
# ================================================================


# 🔹 MÉTODO 1: if clásico
monto = float(input("Método 1 - Ingrese monto: "))
if monto > 10000:
    monto -= monto * 0.10
print("Monto final:", monto)


# 🔹 MÉTODO 2: if-else con mensaje
monto2 = float(input("\nMétodo 2 - Ingrese monto: "))
if monto2 > 10000:
    monto2 *= 0.90  # Aplica el 90% directamente
    print("Se aplicó descuento. Monto final:", monto2)
else:
    print("Sin descuento. Monto final:", monto2)


# 🔹 MÉTODO 3: función con return
def calcular_descuento(monto):
    return monto * 0.90 if monto > 10000 else monto

monto3 = float(input("\nMétodo 3 - Ingrese monto: "))
print("Monto final:", calcular_descuento(monto3))


# 🔹 MÉTODO 4: operador ternario dentro del print
monto4 = float(input("\nMétodo 4 - Ingrese monto: "))
print("Monto final con descuento aplicado:" if monto4 > 10000 else "Monto sin descuento:", monto4 * 0.90 if monto4 > 10000 else monto4)


# 🔹 MÉTODO 5: función con mensaje personalizado
def aplicar_descuento(monto):
    if monto > 10000:
        descuento = monto * 0.10
        nuevo_monto = monto - descuento
        print(f"Descuento de ${descuento:.2f} aplicado. Monto final: ${nuevo_monto:.2f}")
    else:
        print(f"Sin descuento. Monto final: ${monto:.2f}")

monto5 = float(input("\nMétodo 5 - Ingrese monto: "))
aplicar_descuento(monto5)
