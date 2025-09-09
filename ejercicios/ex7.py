# ----------------------------------------------------------
# EJERCICIO 7 - Contar positivos, negativos y promedio
# ----------------------------------------------------------
# Permitir ingresar números indefinidamente hasta que se ingrese el 0.
# Al finalizar mostrar:
# - Cantidad de números positivos y negativos.
# - Promedio de los positivos.


# ============================================
# MÉTODO 1: while clásico
# ============================================
print("\n🔹 MÉTODO 1: WHILE clásico")

pos = 0
neg = 0
suma_pos = 0

while True:
    nro = int(input("Ingrese un número (0 para terminar): "))
    if nro == 0:
        break
    if nro > 0:
        pos += 1
        suma_pos += nro
    else:
        neg += 1

promedio = suma_pos / pos if pos > 0 else 0
print(f"Positivos: {pos} | Negativos: {neg} | Promedio positivos: {promedio:.2f}")


# ============================================
# MÉTODO 2: usando función
# ============================================
print("\n🔹 MÉTODO 2: Función")

def analizar_numeros():
    positivos = negativos = suma = 0

    while True:
        n = int(input("Número (0 para salir): "))
        if n == 0:
            break
        if n > 0:
            positivos += 1
            suma += n
        else:
            negativos += 1

    promedio = suma / positivos if positivos else 0
    print(f"Positivos: {positivos} | Negativos: {negativos} | Promedio positivos: {promedio:.2f}")

analizar_numeros()


# ============================================
# MÉTODO 3: usando recursividad
# ============================================
print("\n🔹 MÉTODO 3: Recursividad")

def contar(pos=0, neg=0, suma=0):
    num = int(input("Número (0 para terminar): "))
    if num == 0:
        prom = suma / pos if pos else 0
        print(f"Positivos: {pos} | Negativos: {neg} | Promedio positivos: {prom:.2f}")
        return
    if num > 0:
        contar(pos + 1, neg, suma + num)
    else:
        contar(pos, neg + 1, suma)

contar()


# ============================================
# MÉTODO 4: usando lista para almacenar los positivos
# ============================================
print("\n🔹 MÉTODO 4: Almacenando positivos en lista")

positivos = []
negativos = 0

while True:
    num = int(input("Ingresá un número (0 para terminar): "))
    if num == 0:
        break
    if num > 0:
        positivos.append(num)
    else:
        negativos += 1

prom = sum(positivos) / len(positivos) if positivos else 0
print(f"Positivos: {len(positivos)} | Negativos: {negativos} | Promedio positivos: {prom:.2f}")


# ============================================
# MÉTODO 5: usando una lambda y map para calcular el promedio
# ============================================
print("\n🔹 MÉTODO 5: Lambda + estructura acumuladora")

numeros = []
while True:
    n = int(input("Número (0 para terminar): "))
    if n == 0:
        break
    numeros.append(n)

positivos = list(filter(lambda x: x > 0, numeros))
negativos = list(filter(lambda x: x < 0, numeros))

prom = (lambda lst: sum(lst)/len(lst) if lst else 0)(positivos)

print(f"Positivos: {len(positivos)} | Negativos: {len(negativos)} | Promedio positivos: {prom:.2f}")
