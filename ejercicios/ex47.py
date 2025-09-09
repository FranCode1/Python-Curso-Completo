# =====================================================================
# EJERCICIO 47: Calculadora de impuestos
# ---------------------------------------------------------------------
# Recibe un precio y un porcentaje de impuestos (por defecto 21%)
# Devuelve el precio final con impuestos incluidos.
# =====================================================================

# ---------- Forma 1: Función con return ----------
def calc_impuesto_1(precio, impuesto=21):
    impuesto_final = (impuesto / 100) * precio
    precio_final = precio + impuesto_final
    return precio_final

# ---------- Forma 2: Calcula directamente sin variable ----------
def calc_impuesto_2(precio, impuesto=21):
    return precio * (1 + impuesto / 100)

# ---------- Forma 3: Solicita precio e impuesto al usuario ----------
def calc_impuesto_3():
    precio = float(input("Ingrese el precio: "))
    impuesto = input("Ingrese el porcentaje de impuesto (dejar vacío = 21%): ")
    impuesto = float(impuesto) if impuesto else 21
    precio_final = precio * (1 + impuesto / 100)
    print(f"Precio final con impuestos: ${precio_final}")

# ---------- Forma 4: Usando función lambda ----------
calc_impuesto_4 = lambda precio, impuesto=21: precio * (1 + impuesto / 100)

# ---------- Forma 5: Usando diccionario para varios productos ----------
def calc_impuesto_5(productos, impuesto=21):
    precios_finales = {}
    for nombre, precio in productos.items():
        precios_finales[nombre] = precio * (1 + impuesto / 100)
    return precios_finales

# =====================================================
# Ejecución de ejemplos
# =====================================================
if __name__ == "__main__":
    # Forma 1
    print(f"[Forma 1] Precio final: ${calc_impuesto_1(1000)}")
    print(f"[Forma 1] Precio final 10%: ${calc_impuesto_1(1000, 10)}")

    # Forma 2
    print(f"[Forma 2] Precio final: ${calc_impuesto_2(1000)}")
    print(f"[Forma 2] Precio final 10%: ${calc_impuesto_2(1000, 10)}")

    # Forma 3
    # calc_impuesto_3()  # Descomentar para ingresar valores por teclado

    # Forma 4
    print(f"[Forma 4] Precio final: ${calc_impuesto_4(1000)}")
    print(f"[Forma 4] Precio final 10%: ${calc_impuesto_4(1000, 10)}")

    # Forma 5
    productos = {"Leche": 150, "Pan": 50, "Queso": 300}
    finales = calc_impuesto_5(productos)
    print("[Forma 5] Precios finales con 21% de impuestos:")
    for prod, precio_final in finales.items():
        print(f"{prod}: ${precio_final}")
