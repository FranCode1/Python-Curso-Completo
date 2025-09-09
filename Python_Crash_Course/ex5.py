# -------------------------------
# 1. Crear diccionarios y acceder a valores
# -------------------------------


# Crear un diccionario con color y puntos
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# Agregar nuevas claves al diccionario
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Acceder a un valor usando su clave
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Mostrar valores individuales
print(alien_0['color'])
print(alien_0['points'])


# -------------------------------
# 2. Crear un diccionario vacío y agregarle datos
# -------------------------------


# Crear diccionario vacío
alien_1 = {}
# Agregar claves y valores
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)


# -------------------------------
# 3. Modificar valores en un diccionario
# -------------------------------


# Cambiar el color del alien
alien_2 = {'color': 'green'}
print(f"The alien is {alien_2['color']}.")
alien_2['color'] = 'yellow'
print(f"The alien is now {alien_2['color']}.")


# -------------------------------
# 4. Actualizar valores condicionalmente
# -------------------------------


# Mover un alien según su velocidad
alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_3['x_position']}")

# Determinar incremento según velocidad
if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3  # 'fast'

# Actualizar posición
alien_3['x_position'] += x_increment
print(f"New position: {alien_3['x_position']}")


# -------------------------------
# 5. Eliminar claves
# -------------------------------


# Eliminar una clave con del
alien_4 = {'color': 'green', 'points': 5}
print(alien_4)
del alien_4['points']
print(alien_4)  # Solo queda 'color'


# -------------------------------
# 6. Recorrer un diccionario
# -------------------------------


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# Recorrer claves y valores
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

# Mostrar todas las claves
for name in favorite_languages.keys():
    print(name.title())

# Mostrar todos los valores (puede haber repetidos)
print("Languages mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Mostrar solo valores únicos con set()
print("Unique languages mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Claves ordenadas
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Verificar si una clave no está presente
if 'erin' not in favorite_languages:
    print("Erin, please take our poll!")

# Acceder directamente al valor de una clave
language = favorite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")


for name, language in favorite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")


friends = ['phil', 'sarah']


# esto es lo mismo, porque es el codigo por default
# for name in favourite_languages: 
for name in favorite_languages.keys():
    print(name.title())
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


# -------------------------------
# 7. Manejo seguro con .get()
# -------------------------------


# alien_5 = {'color': 'green', 'speed': 'slow'}
# print(alien_5['points'])
# La razon del porque esto esta mal es porque pides algo que no existe o no esta en el diccionario


# Usar get() para evitar errores si no existe la clave
alien_6 = {'color': 'green', 'speed': 'slow'}
point_value = alien_6.get('points', 'No point value assigned.')
print(point_value)


# -------------------------------
# 8. Recorrer un diccionario con items()
# -------------------------------


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# forma abreviada: 
# for k, v in user_0.items():
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")


# -------------------------------
# 9. Diccionarios con listas como valores
# -------------------------------


# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")



# -------------------------------
# 10. Diccionario dentro de diccionario
# -------------------------------


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


# -------------------------------
# 11. Listas de diccionarios
# -------------------------------


# Varios aliens como diccionarios
alien_7 = {'color': 'green', 'points': 5}
alien_8 = {'color': 'yellow', 'points': 10}
alien_9 = {'color': 'red', 'points': 15}

aliens0 = [alien_7, alien_8, alien_9]

for alien in aliens0:
    print(alien)


# -------------------------------
# 12. Crear y modificar en masa diccionarios dentro de listas
# -------------------------------


# Make an empty list for storing aliens.
aliens1 = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens1.append(new_alien)

for alien in aliens1[:3]:
    if alien['color'] == ['green']:
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens
for alien in aliens1[:5]:
    print(alien)
    print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens1)}")