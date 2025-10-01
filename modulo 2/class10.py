# ----------------------------------------
# CLASE 10: FUNCIONES EN PYTHON
# ----------------------------------------

# ¿Qué es una función?
# Una función es un bloque de código que se puede reutilizar.
# Se define una sola vez y se puede llamar las veces que quieras.

# 📌 Sintaxis básica:
# def nombre_de_funcion(parámetros):
#     bloque de código

# ✅ Ejemplo simple:

def saludar():
    print("¡Hola! Bienvenido al curso.")

saludar()  # llamada a la función


# ----------------------------------------
# 🔢 FUNCIONES CON PARÁMETROS

def saludar_persona(nombre):
    print(f"Hola, {nombre}.")

saludar_persona("Franco")
saludar_persona("Lucía")


# ----------------------------------------
# 🔁 FUNCIONES CON RETORNO

# Usamos return para devolver un valor

def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(5, 3)
print("Resultado:", total)


# ----------------------------------------
# ✅ PARÁMETROS OPCIONALES / POR DEFECTO

def presentar(nombre, edad=18):
    print(f"{nombre} tiene {edad} años.")

presentar("Tomás")          # usa valor por defecto
presentar("María", 22)      # sobrescribe


# ----------------------------------------
# 🎯 FUNCIONES CON VALORES VARIABLES

# *args → múltiples argumentos
def sumar_todo(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar_todo(1, 2, 3, 4))  # 10

# **kwargs → múltiples claves y valores
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Franco", edad=22, ciudad="Córdoba")


# ----------------------------------------
# 🔁 REUTILIZACIÓN DE FUNCIONES

def calcular_area_rectangulo(base, altura):
    return base * altura

area1 = calcular_area_rectangulo(5, 2)
area2 = calcular_area_rectangulo(3, 4)

print("Área 1:", area1)
print("Área 2:", area2)


# ----------------------------------------
# 🧪 MINI PROYECTO PRÁCTICO

# Crear una función que reciba un nombre y edad, y diga si puede votar

# def puede_votar(nombre, edad):
#     if edad >= 16:
#         print(f"{nombre} puede votar.")
#     else:
#         print(f"{nombre} NO puede votar.")

# nombre = input("Tu nombre: ")
# edad = int(input("Tu edad: "))

# puede_votar(nombre, edad)


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es una función y cómo se define
# - Cómo pasar y retornar valores
# - Parámetros opcionales y variables (*args, **kwargs)
# - Reutilizar funciones para mantener el código limpio
# - Crear lógica dentro de funciones

# Próxima clase: Programación orientada a objetos – clases, atributos y métodos.
