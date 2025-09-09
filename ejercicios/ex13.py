# ----------------------------------------------------------
# EJERCICIO 13 - Determinar si un número es par o impar
# ----------------------------------------------------------

num = int(input("Ingrese un número: "))

# Método 1: if-else clásico
if num % 2 == 0:
    print("Método 1: El número es par")
else:
    print("Método 1: El número es impar")


# Método 2: Usando operador ternario (one-liner)
print("Método 2: El número es", "par" if num % 2 == 0 else "impar")


# Método 3: Usando lista de mensajes e índice
mensajes = ["El número es par", "El número es impar"]
print("Método 3:", mensajes[num % 2])


# Método 4: Usando función con retorno
def es_par(n):
    return n % 2 == 0

print("Método 4:", "El número es par" if es_par(num) else "El número es impar")


# Método 5: Usando diccionario para mapear resultado
resultado = {0: "El número es par", 1: "El número es impar"}
print("Método 5:", resultado[num % 2])
