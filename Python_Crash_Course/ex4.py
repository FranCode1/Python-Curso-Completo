# -------------------------------
# Trabajando con listas e ifs
# -------------------------------

cars = ['audi', 'bmw', 'subaru', 'toyota']

# Recorremos cada auto en la lista
for car in cars:
    if car == 'bmw':
        print(car.upper())  # Para BMW lo escribimos en mayúsculas
    else:
        print(car.title())  # Para los demás, con la primera letra en mayúscula

# -------------------------------
# Comparaciones (True / False)
# -------------------------------

car = 'bmw'
print("car == 'bmw' ->", car == 'bmw')  # True

car = 'Audi'
print("car == 'audi' ->", car == 'audi')  # False (porque 'Audi' != 'audi')

print("car.lower() == 'audi' ->", car.lower() == 'audi')  # True (normaliza a minúsculas)

# -------------------------------
# Operador de desigualdad
# -------------------------------

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")  # Solo imprime si el topping NO es 'anchovies'

# -------------------------------
# Comparaciones numéricas
# -------------------------------

age = 18
print("age > 21:", age > 21)
print("age >= 21:", age >= 21)
print("age < 21:", age < 21)
print("age <= 21:", age <= 21)
print("age == 18:", age == 18)

# -------------------------------
# Operadores lógicos: and / or
# -------------------------------

age_0 = 22
age_1 = 18

print("Ambos >= 21:", age_0 >= 21 and age_1 >= 21)  # False
age_1 = 22
print("Ambos >= 21:", age_0 >= 21 and age_1 >= 21)  # True

age_0 = 22
age_1 = 18
print("Al menos uno >= 21:", age_0 >= 21 or age_1 >= 21)  # True

age_0 = 18
print("Al menos uno >= 21:", age_0 >= 21 or age_1 >= 21)  # False

# -------------------------------
# Comparación con valores esperados
# -------------------------------

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# -------------------------------
# Verificando si un elemento está en una lista
# -------------------------------

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("'mushrooms' in list:", 'mushrooms' in requested_toppings)  # True
print("'pepperoni' in list:", 'pepperoni' in requested_toppings)  # False

# -------------------------------
# Comprobando si un usuario no está baneado
# -------------------------------

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')

# -------------------------------
# Variables booleanas
# -------------------------------

game_active = True
can_edit = False

# -------------------------------
# Comparaciones con predicciones
# -------------------------------

car0 = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car0 == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car0 == 'audi')

# -------------------------------
# Ejemplo simple de estructura if-else
# -------------------------------

age_3 = 19

if age_3 >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# -------------------------------
# if-elif-else: precios por edad
# -------------------------------

age_4 = 12

if age_4 < 4:
    print("Your admission cost is $0.")
elif age_4 < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# Otra forma: guardar el precio en una variable
age_5 = 12

if age_5 < 4:
    price = 0
elif age_5 < 18:
    price = 25
elif age_5 < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

# -------------------------------
# elif se detiene cuando encuentra una coincidencia
# -------------------------------

requested_toppings_1 = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings_1:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings_1:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings_1:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")  # Ojo que el elif evita que se agreguen varios toppings

# -------------------------------
# Recorriendo lista de toppings y usando if dentro del for
# -------------------------------

requested_toppings_2 = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings_2:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# -------------------------------
# Lista vacía: preguntar si el usuario quiere una pizza sin toppings
# -------------------------------

requested_toppings_3 = []

if requested_toppings_3:
    for requested_topping in requested_toppings_3:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# -------------------------------
# Validando si los toppings solicitados están disponibles
# -------------------------------

available_toppings = [
    'mushrooms', 'olives', 'green peppers',
    'pepperoni', 'pineapple', 'extra cheese'
]

requested_toppings_4 = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings_4:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
