# ----------------------------------------
# PRÁCTICA - CLASE 10: FUNCIONES EN PYTHON
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Función sin parámetros
# Consigna: Crear una función que imprima un mensaje motivador.
def motivar():
    print("¡Sos capaz de lograr lo que te propongas!")

motivar()

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Función con un parámetro
# Consigna: Crear una función que salude a una persona por su nombre.
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Lucía")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Función que retorne un valor
# Consigna: Crear una función que calcule el doble de un número.
def doble(num):
    return num * 2

print("Doble de 4:", doble(4))

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Sumar dos números
# Consigna: Crear una función que reciba dos números y devuelva su suma.
def sumar(a, b):
    return a + b

resultado = sumar(3, 7)
print("Suma:", resultado)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Parámetro por defecto
# Consigna: Crear una función que presente a una persona. Si no se da edad, usar 18.
def presentar(nombre, edad=18):
    print(f"{nombre} tiene {edad} años.")

presentar("Franco")
presentar("Mara", 25)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Función con *args
# Consigna: Crear una función que reciba varios números y devuelva su promedio.
def promedio(*numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

print("Promedio:", promedio(5, 7, 9, 3))

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Función con **kwargs
# Consigna: Crear una función que reciba info de una persona y la muestre.
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Sofía", edad=30, país="Argentina")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Función que devuelva si un número es par
# Consigna: Crear una función que reciba un número y retorne True si es par.
def es_par(n):
    return n % 2 == 0

print("¿Es 6 par?", es_par(6))
print("¿Es 7 par?", es_par(7))

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Reutilizar funciones
# Consigna: Crear una función que use otra para calcular y mostrar el cuadrado de un número.
def cuadrado(n):
    return n * n

def mostrar_cuadrado(n):
    print(f"El cuadrado de {n} es {cuadrado(n)}")

mostrar_cuadrado(5)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Función que indique si puede votar
# Consigna: Crear una función que diga si una persona puede votar (mayor de 16).
def puede_votar(nombre, edad):
    if edad >= 16:
        print(f"{nombre} puede votar.")
    else:
        print(f"{nombre} NO puede votar.")

puede_votar("Martina", 15)
puede_votar("Julián", 18)

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
