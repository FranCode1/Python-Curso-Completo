# =====================================================================
# EJERCICIO 42: Control de Stock
# ---------------------------------------------------------------------
# Una fábrica de tornillos produce por día una cantidad variable de piezas.
# Durante 7 días se registra la cantidad producida por día.
# El programa debe:
# 1. Permitir ingresar los datos con validación (>0)
# 2. Calcular: producción total, día de mayor producción y promedio semanal
# 3. Indicar si algún día no se alcanzó el mínimo diario (500 piezas)
# =====================================================================

# ---------- Forma 1: básica con while ----------
def stock_1():
    produccion_total = 0
    mayor_produccion = 0
    dia_mayor = 0
    dias_baja = []

    for dia in range(1, 8):
        while True:
            try:
                cantidad = int(input(f"Ingrese cantidad día {dia}: "))
                if cantidad > 0:
                    break
                else:
                    print("❌ Debe ser mayor a 0.")
            except ValueError:
                print("⚠️ Número inválido.")
        produccion_total += cantidad
        if cantidad > mayor_produccion:
            mayor_produccion = cantidad
            dia_mayor = dia
        if cantidad < 500:
            dias_baja.append(dia)

    promedio = produccion_total / 7
    print(f"Total: {produccion_total}, Mayor: {mayor_produccion} (día {dia_mayor}), Promedio: {promedio:.2f}")
    if dias_baja:
        print("Días con baja producción:", dias_baja)
    else:
        print("✅ Todos los días alcanzaron el mínimo.")

# ---------- Forma 2: usando lista para almacenar producción ----------
def stock_2():
    produccion = []
    for i in range(1, 8):
        while True:
            try:
                cantidad = int(input(f"Ingrese producción día {i}: "))
                if cantidad > 0:
                    produccion.append(cantidad)
                    break
                else:
                    print("❌ Debe ser mayor a 0.")
            except ValueError:
                print("⚠️ Número inválido.")

    total = sum(produccion)
    mayor = max(produccion)
    dia_mayor = produccion.index(mayor) + 1
    promedio = total / len(produccion)
    dias_baja = [i+1 for i, v in enumerate(produccion) if v < 500]

    print(f"Total: {total}, Mayor: {mayor} (día {dia_mayor}), Promedio: {promedio:.2f}")
    if dias_baja:
        print("Días con baja producción:", dias_baja)
    else:
        print("✅ Todos los días alcanzaron el mínimo.")

# ---------- Forma 3: usando funciones ----------
def pedir_cantidad(dia):
    while True:
        try:
            c = int(input(f"Día {dia} cantidad: "))
            if c > 0:
                return c
            else:
                print("❌ Debe ser mayor a 0.")
        except ValueError:
            print("⚠️ Número inválido.")

def stock_3():
    produccion = [pedir_cantidad(dia) for dia in range(1, 8)]
    total = sum(produccion)
    mayor = max(produccion)
    dia_mayor = produccion.index(mayor) + 1
    promedio = total / 7
    dias_baja = [i+1 for i, v in enumerate(produccion) if v < 500]
    print(f"Total: {total}, Mayor: {mayor} (día {dia_mayor}), Promedio: {promedio:.2f}")
    if dias_baja:
        print("Días con baja producción:", dias_baja)
    else:
        print("✅ Todos los días alcanzaron el mínimo.")

# ---------- Forma 4: usando while True ----------
def stock_4():
    produccion_total = 0
    mayor = 0
    dia_mayor = 0
    dias_baja = []
    dia = 1
    while dia <= 7:
        try:
            cantidad = int(input(f"Día {dia} cantidad: "))
            if cantidad <= 0:
                print("❌ Debe ser mayor a 0.")
                continue
        except ValueError:
            print("⚠️ Número inválido.")
            continue

        produccion_total += cantidad
        if cantidad > mayor:
            mayor = cantidad
            dia_mayor = dia
        if cantidad < 500:
            dias_baja.append(dia)
        dia += 1

    promedio = produccion_total / 7
    print(f"Total: {produccion_total}, Mayor: {mayor} (día {dia_mayor}), Promedio: {promedio:.2f}")
    if dias_baja:
        print("Días con baja producción:", dias_baja)
    else:
        print("✅ Todos los días alcanzaron el mínimo.")

# ---------- Forma 5: con iteradores y map ----------
def stock_5():
    cantidades = []
    for dia in range(1, 8):
        while True:
            try:
                cantidad = int(input(f"Día {dia} cantidad: "))
                if cantidad > 0:
                    cantidades.append(cantidad)
                    break
                else:
                    print("❌ Debe ser mayor a 0.")
            except ValueError:
                print("⚠️ Número inválido.")

    total = sum(cantidades)
    mayor = max(cantidades)
    dia_mayor = cantidades.index(mayor) + 1
    promedio = total / 7
    dias_baja = list(map(lambda x: x+1, filter(lambda i: cantidades[i] < 500, range(7))))

    print(f"Total: {total}, Mayor: {mayor} (día {dia_mayor}), Promedio: {promedio:.2f}")
    if dias_baja:
        print("Días con baja producción:", dias_baja)
    else:
        print("✅ Todos los días alcanzaron el mínimo.")

# =====================================================================
# Ejecución del programa
# =====================================================================
if __name__ == "__main__":
    # Descomentar la forma que quieras probar
    # stock_1()
    # stock_2()
    # stock_3()
    # stock_4()
    stock_5()
