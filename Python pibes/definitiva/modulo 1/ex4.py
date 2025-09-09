# ----------------------------------------
# PRÁCTICA - CLASE 4: OPERADORES EN PYTHON
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Operaciones aritméticas básicas
# Consigna: Declarar dos variables `a = 12`, `b = 4` y mostrar su suma, resta, multiplicación y división.
a = 12
b = 4
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: División entera, módulo y potencia
# Consigna: Usá `a = 15`, `b = 6` y mostrálos usando //, %, **
a = 15
b = 6
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Operadores de asignación
# Consigna: Usá una variable x = 10 y aplicá +=, -=, *= y /= mostrando el resultado cada vez.
x = 10
x += 5
print("x += 5:", x)
x -= 2
print("x -= 2:", x)
x *= 3
print("x *= 3:", x)
x /= 4
print("x /= 4:", x)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Comparaciones simples
# Consigna: Compará a = 7 y b = 10 usando ==, !=, >, <, >=, <=
a = 7
b = 10
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Operadores lógicos
# Consigna: Usá x = 8 y evaluá: x > 5 and x < 10, x < 5 or x == 8, not(x == 8)
x = 8
print(x > 5 and x < 10)
print(x < 5 or x == 8)
print(not(x == 8))

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Comparación de listas
# Consigna: Usá a = [1, 2], b = a, c = [1, 2] y comparalos con `is` y `==`
a = [1, 2]
b = a
c = [1, 2]
print("a is b:", a is b)   # True
print("a is c:", a is c)   # False
print("a == c:", a == c)   # True

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Pertenencia en listas
# Consigna: Mostrá si 5 está en la lista `[3, 4, 5, 6]` y si 2 no está.
lista = [3, 4, 5, 6]
print(5 in lista)
print(2 not in lista)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Par o impar
# Consigna: Usá un número `n = 13` y mostrale al usuario si es par o impar usando `%`.
n = 13
if n % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Condición compuesta con operadores lógicos
# Consigna: Dado `edad = 20`, comprobar si la persona es mayor de edad y menor de 30.
edad = 20
es_joven_adulto = edad >= 18 and edad < 30
print("¿Es joven adulto (18-29)?", es_joven_adulto)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Verificar coincidencia de objetos
# Consigna: Crear dos listas iguales y comparar si apuntan al mismo objeto.
lista1 = [10, 20, 30]
lista2 = [10, 20, 30]
print("lista1 is lista2:", lista1 is lista2)   # False
print("lista1 == lista2:", lista1 == lista2)   # True

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
