# =====================================================================
# EJERCICIO 39: Función descuento con porcentaje por defecto
# ---------------------------------------------------------------------
# Crear una función que calcule el precio final con un porcentaje de
# descuento opcional (por defecto 10%).
# =====================================================================

# ---------- Forma 1: print directo ----------
def descuento1(precio, porcentaje=10):
    precio_final = precio * (1 - porcentaje / 100)
    print(f"El precio final es: ${precio_final}")

# ---------- Forma 2: usando f-string con 2 decimales ----------
def descuento2(precio, porcentaje=10):
    precio_final = precio * (1 - porcentaje / 100)
    print(f"Precio original: ${precio}, Descuento: {porcentaje}%, Total: ${precio_final:.2f}")

# ---------- Forma 3: retornando el valor ----------
def descuento3(precio, porcentaje=10):
    return precio * (1 - porcentaje / 100)

# ---------- Forma 4: mostrando cantidad descontada ----------
def descuento4(precio, porcentaje=10):
    monto_descuento = precio * (porcentaje / 100)
    precio_final = precio - monto_descuento
    print(f"Se aplicó un descuento de ${monto_descuento}, precio final: ${precio_final}")

# ---------- Forma 5: usando diccionario para detalle ----------
def descuento5(precio, porcentaje=10):
    resultado = {
        "Precio Original": precio,
        "Porcentaje Descuento": porcentaje,
        "Monto Descuento": precio * (porcentaje / 100),
        "Precio Final": precio * (1 - porcentaje / 100)
    }
    for k, v in resultado.items():
        print(f"{k}: ${v:.2f}")

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    print("\nForma 1:")
    descuento1(1000)

    print("\nForma 2:")
    descuento2(1000, 15)

    print("\nForma 3:")
    print(f"Precio final: ${descuento3(2000, 20)}")

    print("\nForma 4:")
    descuento4(1500)

    print("\nForma 5:")
    descuento5(2500, 25)
