from ex7a import pizza
from ex7a import make_pizza

# De esta manera podes importar mas de una funcion a la vez con la misma linea de codigo
# from ex7a import pizza, make_pizza, print_models

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')