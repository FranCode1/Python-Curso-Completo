# =====================================================================
# EJERCICIO 25: Sistema de Cálculo de Interés Compuesto
# ---------------------------------------------------------------------
# Solicitar monto inicial, tasa de interés mensual y cantidad de meses.
# Mostrar el total al finalizar los meses y evaluar si conviene invertir
# en interés compuesto o buscar otra opción.
# =====================================================================

# ---------- Forma 1: fórmula directa ----------
def interes1(monto, tasa, meses):
    total = monto * (1 + tasa/100) ** meses
    print(f"Total final: ${total:.2f}")
    return total

# ---------- Forma 2: iterativa sumando mes a mes ----------
def interes2(monto, tasa, meses):
    total = monto
    for i in range(meses):
        total += total * (tasa / 100)
    print(f"Total final: ${total:.2f}")
    return total

# ---------- Forma 3: recursiva ----------
def interes_rec(monto, tasa, meses):
    if meses == 0:
        return monto
    else:
        return interes_rec(monto*(1 + tasa/100), tasa, meses-1)

# ---------- Forma 4: usando while ----------
def interes4(monto, tasa, meses):
    total = monto
    i = 0
    while i < meses:
        total *= (1 + tasa/100)
        i += 1
    print(f"Total final: ${total:.2f}")
    return total

# ---------- Forma 5: con evaluación de conveniencia ----------
def interes5(monto, tasa, meses):
    total = monto * (1 + tasa/100) ** meses
    print(f"Total final: ${total:.2f}")
    if tasa < 1:  # arbitrario: tasa baja, conviene otra inversión
        print("💡 La tasa es baja, podrías considerar invertir en otra opción.")
    else:
        print("💡 El interés compuesto conviene para esta inversión.")
    return total

# =====================================================================
# Ejecución
# =====================================================================
if __name__ == "__main__":
    monto = float(input("Ingrese el monto inicial: "))
    tasa = float(input("Ingrese la tasa de interés mensual (%): "))
    meses = int(input("Ingrese la cantidad de meses: "))

    # Descomentar la función que quieras probar
    # interes1(monto, tasa, meses)
    # interes2(monto, tasa, meses)
    # print(f"Total final (recursivo): ${interes_rec(monto, tasa, meses):.2f}")
    # interes4(monto, tasa, meses)
    # interes5(monto, tasa, meses)
