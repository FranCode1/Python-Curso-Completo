# ----------------------------------------
# PRÁCTICA - CLASE 6: BUCLES EN PYTHON
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Contador con while
# Consigna: Mostrar los números del 1 al 5 usando while.
contador = 1
while contador <= 5:
    print("Número:", contador)
    contador += 1

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Suma acumulada con while
# Consigna: Sumar los números del 1 al 10 y mostrar el total.
i = 1
suma = 0
while i <= 10:
    suma += i
    i += 1
print("Suma total:", suma)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Iterar con for y range
# Consigna: Mostrar los números pares del 0 al 10 usando for.
for i in range(0, 11, 2):
    print("Par:", i)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Recorrer una lista
# Consigna: Imprimir todos los elementos de una lista de animales.
animales = ["perro", "gato", "loro"]
for animal in animales:
    print("Animal:", animal)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Recorrer un string
# Consigna: Mostrar cada letra de la palabra "Python"
for letra in "Python":
    print("Letra:", letra)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Usar enumerate
# Consigna: Mostrar el índice y nombre de cada fruta en una lista.
frutas = ["manzana", "banana", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"{indice} - {fruta}")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: break en for
# Consigna: Mostrar números del 0 al 9, pero detenerse cuando el número sea 4.
for i in range(10):
    if i == 4:
        break
    print("i:", i)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: continue en for
# Consigna: Mostrar números del 0 al 4, pero saltar el número 2.
for i in range(5):
    if i == 2:
        continue
    print("Valor:", i)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Contraseña hasta acertar
# Consigna: Simular que el usuario debe ingresar "python123" hasta acertar.
# (Simulación sin input real para que sea ejecutable sin interacción)
intentos = ["abc", "123", "python123"]
indice = 0
while True:
    intento = intentos[indice]
    print("Ingresado:", intento)
    if intento == "python123":
        print("¡Acceso concedido!")
        break
    else:
        print("Incorrecta. Intentá de nuevo.")
    indice += 1

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Tabla de multiplicar
# Consigna: Mostrar la tabla del 7 del 1 al 10 usando for.
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
