# ----------------------------------------------------------
# EJERCICIO 9 - Cajero Automático
# ----------------------------------------------------------
# Dado un monto ingresado por el usuario, calcular la combinación
# mínima de billetes para llegar a esa cantidad.
# El cajero tiene billetes de 10000, 1000, 500 y 200.

# ============================================
# MÉTODO 1: clásico con diccionario y for
# ============================================
print("\n🔹 MÉTODO 1: for con diccionario")

bills = [10000, 1000, 500, 200]
amount = int(input("Ingrese la cantidad deseada: "))
remaining = amount
result = {}

for bill in bills:
    count = remaining // bill
    remaining %= bill
    result[bill] = count

print(f"\nCombinación mínima de billetes para {amount}:")
for bill in bills:
    if result[bill] > 0:
        print(f"{result[bill]} billete(s) de {bill}")


# ============================================
# MÉTODO 2: usando una función
# ============================================
print("\n🔹 MÉTODO 2: función con retorno")

def calcular_billetes(cantidad):
    disponibles = [10000, 1000, 500, 200]
    resultado = {}
    for billete in disponibles:
        resultado[billete] = cantidad // billete
        cantidad %= billete
    return resultado

monto = int(input("Cantidad a retirar: "))
salida = calcular_billetes(monto)
print(f"\nBilletes para {monto}:")
for b, c in salida.items():
    if c > 0:
        print(f"{c} billete(s) de {b}")


# ============================================
# MÉTODO 3: con while y contador
# ============================================
print("\n🔹 MÉTODO 3: bucles anidados con while")

cantidad = int(input("Monto a retirar: "))
billetes = [10000, 1000, 500, 200]
contador = 0

while cantidad > 0 and contador < len(billetes):
    billete = billetes[contador]
    num_billetes = cantidad // billete
    if num_billetes > 0:
        print(f"{num_billetes} billete(s) de {billete}")
        cantidad -= num_billetes * billete
    contador += 1


# ============================================
# MÉTODO 4: con listas paralelas (valores y cantidades)
# ============================================
print("\n🔹 MÉTODO 4: con listas paralelas")

denominaciones = [10000, 1000, 500, 200]
cantidades = []
restante = int(input("Cantidad solicitada: "))

for valor in denominaciones:
    cantidades.append(restante // valor)
    restante %= valor

for i in range(len(denominaciones)):
    if cantidades[i] > 0:
        print(f"{cantidades[i]} billete(s) de {denominaciones[i]}")


# ============================================
# MÉTODO 5: versión recursiva
# ============================================
print("\n🔹 MÉTODO 5: recursividad")

def devolver_billetes(monto, i=0):
    tipos = [10000, 1000, 500, 200]
    if i >= len(tipos):
        return
    cantidad = monto // tipos[i]
    if cantidad > 0:
        print(f"{cantidad} billete(s) de {tipos[i]}")
    devolver_billetes(monto % tipos[i], i + 1)

monto_final = int(input("Ingresá un monto: "))
devolver_billetes(monto_final)
