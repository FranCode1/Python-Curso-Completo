# -------------------------------
# USER INPUT BASICS
# -------------------------------

# Solicita un mensaje y lo repite
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Solicita el nombre del usuario y lo saluda
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Solicita el nombre con un mensaje más elaborado
prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# -------------------------------
# USO DE INPUT CON CONVERSIÓN DE DATOS
# -------------------------------

# Solicita la edad y verifica si el usuario es mayor de edad
age = input("How old are you? ")
age = int(age)  # Conversión a entero
print(age >= 18)  # Devuelve True si tiene 18 o más

# Solicita la altura y determina si puede subir a una atracción
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# Solicita un número y dice si es par o impar
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# -------------------------------
# CICLOS WHILE BÁSICOS
# -------------------------------

# Imprime los números del 1 al 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Versión con condición de salida usando una variable
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# Versión usando una variable de control `active`
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Versión con ciclo infinito y break
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# -------------------------------
# USO DE CONTINUE EN WHILE
# -------------------------------

# Imprime los números impares del 1 al 9
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # Salta el resto del ciclo si es par
    print(current_number)

# Otro ejemplo básico de while
x = 1
while x <= 5:
    print(x)
    x += 1

# -------------------------------
# GESTIÓN DE LISTAS CON WHILE
# -------------------------------

# Verificar usuarios no confirmados y moverlos a la lista de confirmados
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verifica cada usuario hasta que la lista esté vacía
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Mostrar los usuarios confirmados
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# -------------------------------
# REMOVER ELEMENTOS REPETIDOS DE UNA LISTA
# -------------------------------

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("\nOriginal pet list:", pets)

# Elimina todas las ocurrencias de 'cat'
while 'cat' in pets:
    pets.remove('cat')

print("Updated pet list:", pets)

# -------------------------------
# ALMACENAMIENTO DE RESPUESTAS EN UN DICCIONARIO
# -------------------------------

responses = {}

# Bandera para controlar el ciclo de encuestas
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Guarda la respuesta en el diccionario
    responses[name] = response

    # Verifica si otra persona quiere participar
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Muestra los resultados de la encuesta
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
