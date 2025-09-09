# esta linea de codigo importa la funcion randint del moduo random, sirve para devolver valores random entre los limites que le des
from random import randint
randint(1, 6)


# esta funcion elige un valor random de una lista on tupla
from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)