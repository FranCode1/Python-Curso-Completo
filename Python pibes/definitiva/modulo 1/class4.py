# ----------------------------------------
# CLASE 4: OPERADORES EN PYTHON
# ----------------------------------------

# Los operadores son símbolos que realizan operaciones sobre valores o variables.
# Python tiene varios tipos de operadores:
# - Aritméticos
# - Comparación
# - Asignación
# - Lógicos
# - Identidad
# - Pertenencia


# ----------------------------------------
# ➕ OPERADORES ARITMÉTICOS
# ----------------------------------------

a = 10
b = 3

print("Suma:", a + b)             # 13
print("Resta:", a - b)            # 7
print("Multiplicación:", a * b)   # 30
print("División:", a / b)         # 3.333...
print("División entera:", a // b) # 3
print("Módulo:", a % b)           # 1 (resto)
print("Potencia:", a ** b)        # 1000 (10^3)


# ----------------------------------------
# ➗ OPERADORES DE ASIGNACIÓN
# ----------------------------------------

# Sirven para modificar el valor de una variable

x = 5
x += 3   # x = x + 3
print("x += 3:", x)

x -= 2   # x = x - 2
print("x -= 2:", x)

x *= 4
print("x *= 4:", x)

x /= 3
print("x /= 3:", x)


# ----------------------------------------
# 🔍 OPERADORES DE COMPARACIÓN
# ----------------------------------------

# Devuelven True o False

a = 10
b = 5

print("a == b:", a == b)  # ¿son iguales?
print("a != b:", a != b)  # ¿son distintos?
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# ----------------------------------------
# ⚙️ OPERADORES LÓGICOS
# ----------------------------------------

# Se usan para combinar condiciones

x = 7

print(x > 5 and x < 10)   # True si ambas son verdaderas
print(x > 10 or x == 7)   # True si al menos una es verdadera
print(not(x == 7))        # Invierte el resultado (False)


# ----------------------------------------
# 🧠 OPERADORES DE IDENTIDAD
# ----------------------------------------

# Comparan si dos variables apuntan al mismo objeto en memoria

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True → misma referencia
print(a is c)      # False → diferentes objetos aunque tengan el mismo contenido
print(a == c)      # True → mismo contenido


# ----------------------------------------
# 📦 OPERADORES DE PERTENENCIA
# ----------------------------------------

lista = [1, 2, 3, 4]

print(2 in lista)       # True
print(10 not in lista)  # True


# ----------------------------------------
# 🧪 Mini ejercicio práctico

# Descomentalo y completalo:

# num = int(input("Ingresá un número: "))
# if num % 2 == 0:
#     print("El número es par.")
# else:
#     print("El número es impar.")


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Operadores aritméticos: +, -, *, /, %, **
# - Operadores de asignación: +=, -=, etc.
# - Operadores de comparación: ==, !=, >, <, >=, <=
# - Operadores lógicos: and, or, not
# - Operadores de identidad: is, is not
# - Operadores de pertenencia: in, not in

# Próxima clase: estructuras condicionales con if, elif y else.
