# =====================================================================
# EJERCICIO 32: Conversión de Celsius a Fahrenheit
# ---------------------------------------------------------------------
# Crear una función que reciba una temperatura en Celsius y devuelva
# su equivalente en Fahrenheit.
# Entrada: 28
# Salida: 82.4
# =====================================================================

# ---------- Forma 1: función básica ----------
def celsius_a_fahrenheit1(temp):
    return (temp * 9/5) + 32

# ---------- Forma 2: con variable intermedia ----------
def celsius_a_fahrenheit2(temp):
    resultado = (temp * 9/5) + 32
    return resultado

# ---------- Forma 3: con lambda ----------
celsius_a_fahrenheit3 = lambda temp: (temp * 9/5) + 32

# ---------- Forma 4: con print dentro de la función ----------
def celsius_a_fahrenheit4(temp):
    far = (temp * 9/5) + 32
    print(f"{temp}°C equivalen a {far}°F")
    return far

# ---------- Forma 5: devolver string formateado ----------
def celsius_a_fahrenheit5(temp):
    far = (temp * 9/5) + 32
    return f"{temp}°C equivalen a {far}°F"

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    temp_c = float(input("Ingrese la temperatura en Celsius: "))

    print("\nForma 1:", celsius_a_fahrenheit1(temp_c))
    print("Forma 2:", celsius_a_fahrenheit2(temp_c))
    print("Forma 3:", celsius_a_fahrenheit3(temp_c))
    print("Forma 4:")
    celsius_a_fahrenheit4(temp_c)
    print("Forma 5:", celsius_a_fahrenheit5(temp_c))
