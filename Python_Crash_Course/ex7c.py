from ex7a import make_pizza as mp
# Asi importas funciones o lo que sea de otro archivo a este, pero con 'as' podes decirle con que nombre queres llamar a esa funcion o lo que sea en este archivo, aqui importe make_pizza pero le digo que este archivo voy a llamar a esa funcion como 'mp'

from ex7a import pizza as p
from ex7a import *
# con el * importamos todo lo del archivo o modulo

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


