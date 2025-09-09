# ----------------------------------------
# TRABAJANDO CON LISTAS Y BUCLES FOR
# ----------------------------------------

# Lista básica de magos e impresión simple
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)  # Imprime cada nombre en la lista

print("\n")  # Separador visual

# Imprime un mensaje personalizado para cada mago
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Mensaje final (fuera del bucle)
print('Thank you, everyone. That was a great magic show!')

print("\n")

# ----------------------------------------
# ERRORES COMUNES (COMENTADOS)
# ----------------------------------------

# Error común: falta de indentación
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)  # ❌ Error: faltó indentación

# Error común: indentación innecesaria
# message = 'Hello Python World!'
#     print(message)  # ❌ Error: print() está mal indentado

# Error común: falta de dos puntos ":"
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians  # ❌ Error: falta ":"
#     print(magician)

print("\n")

# ----------------------------------------
# BUCLES Y VALORES FUERA DEL BUCLE
# ----------------------------------------

# El siguiente print se ejecuta una sola vez (fuera del bucle)
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
print("I can't wait to see your next trick, magician.\n")  # Usará el último valor de "magician"

print("\n")

# Bucle correctamente indentado con múltiples mensajes
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everyone, that was a great magic show!")

print("\n")

# ----------------------------------------
# USO DE RANGE Y LISTAS NUMÉRICAS
# ----------------------------------------

# Imprime números del 1 al 4
for value in range(1, 5):
    print(value)

# Imprime números del 1 al 5
for value in range(1, 6):
    print(value)

# Crear una lista de números del 1 al 5
numbers = list(range(1, 6))
print(numbers)

# Crear una lista de números pares del 2 al 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)

print("\n")

# ----------------------------------------
# LISTAS DE CUADRADOS (MÉTODOS DIFERENTES)
# ----------------------------------------

# Forma detallada (con variable intermedia)
squares1 = []
for value in range(1, 11):
    square = value ** 2
    squares1.append(square)
print(squares1)

# Versión resumida
squares2 = []
for value in range(1, 11):
    squares2.append(value ** 2)
print(squares2)

# List comprehension (más compacta)
squares3 = [value ** 2 for value in range(1, 11)]
print(squares3)

print("\n")

# ----------------------------------------
# FUNCIONES MIN, MAX, SUM
# ----------------------------------------

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # Valor mínimo
print(max(digits))  # Valor máximo
print(sum(digits))  # Suma total

print("\n")

# ----------------------------------------
# SLICE: SUBLISTAS
# ----------------------------------------

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])  # Primeros 3 elementos
print(players[1:4])  # Del segundo al cuarto
print(players[:4])   # Desde el inicio hasta el cuarto
print(players[2:])   # Desde el tercero hasta el final
print(players[-3:])  # Últimos 3 elementos

print("\n")

# Usando slicing en bucles
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\n")

# ----------------------------------------
# COPIAR LISTAS CORRECTAMENTE
# ----------------------------------------

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # Copia correcta (no enlazadas)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend\'s favorite foods are:")
print(friend_foods)

print("\n")

# ----------------------------------------
# TRABAJANDO CON TUPLAS (LISTAS INMUTABLES)
# ----------------------------------------

# Definición de tupla
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Intento de modificar tupla (error)
# dimensions[0] = 250  # ❌ Error: las tuplas no se pueden modificar

# Recorriendo una tupla
for dimension in dimensions:
    print(dimension)

print("\n")

# Redefiniendo tupla (sí se puede reasignar)
dimensions = (400, 100)
print("Modified Dimensions:")
for dimension in dimensions:
    print(dimension)
