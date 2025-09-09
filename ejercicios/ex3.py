# ----------------------------------------
# EJERCICIO 3 - Precio con descuento
# ----------------------------------------
# Pedir el precio unitario y la cantidad vendida.
# Si el total supera $10.000, aplicar 10% de descuento.

# ========== MÉTODO 1: if-else clásico ==========
print("\n🔹 MÉTODO 1: Clásico con if-else")
precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad vendida: "))
total = precio_unitario * cantidad

if total > 10000:
    total *= 0.9  # aplica 10% de descuento
print(f"Precio final: ${total:.2f}")


# ========== MÉTODO 2: con operador ternario ==========
print("\n🔹 MÉTODO 2: Operador ternario")
pu = float(input("Precio unitario: "))
cant = int(input("Cantidad: "))
total2 = pu * cant
descuento_aplicado = True if total2 > 10000 else False
precio_final2 = total2 * 0.9 if descuento_aplicado else total2
print(f"Precio final: ${precio_final2:.2f}")


# ========== MÉTODO 3: función separada ==========
print("\n🔹 MÉTODO 3: Función que aplica descuento")

def calcular_total(pu, cantidad):
    subtotal = pu * cantidad
    if subtotal > 10000:
        return subtotal * 0.9
    return subtotal

pu3 = float(input("Precio unitario: "))
cant3 = int(input("Cantidad vendida: "))
print(f"Precio final: ${calcular_total(pu3, cant3):.2f}")


# ========== MÉTODO 4: usando diccionario booleano ==========
print("\n🔹 MÉTODO 4: Diccionario con condición booleana")

pu4 = float(input("Precio unitario: "))
cant4 = int(input("Cantidad vendida: "))
total4 = pu4 * cant4
descuentos = {
    True: total4 * 0.9,
    False: total4
}
print(f"Precio final: ${descuentos[total4 > 10000]:.2f}")


# ========== MÉTODO 5: match-case (Python 3.10+) ==========
print("\n🔹 MÉTODO 5: match-case")

pu5 = float(input("Precio unitario: "))
cant5 = int(input("Cantidad vendida: "))
total5 = pu5 * cant5

match total5:
    case total if total > 10000:
        total5 *= 0.9
    case _:
        pass

print(f"Precio final: ${total5:.2f}")
