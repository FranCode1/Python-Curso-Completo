# FUNCTIONS


def greet_user(username):
    """Display a simple greeting."""
    print(f'Hello, {username.title()}!')

greet_user('jeese')


def describe_pet(animal_type, pet_name='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

#A hamster named Harry.
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

describe_pet()


def get_formatted_name_1(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician_1 = get_formatted_name_1('jimi', 'hendrix')
musician_2 = get_formatted_name_1('john', 'lee', 'hooker')
print(musician_1)


def get_formatted_name_2(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician_3 = get_formatted_name_2('jimi', 'hendrix')
print(musician_3)

musician_4 = get_formatted_name_2('john', 'hooker', 'lee')
print(musician_4)


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician_5 = build_person('jimi', 'hendrix', age=27)
print(musician_5)


def get_formatted_name_3(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")


    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name_3(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing mode: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# ESTO '[:]' SIRVE PARA CREAR UNA COPIA DE LA LISTA LLAMADA Y NO MODIFICAR LA ORIGINAL
# function_name(list_name[:])
# print_models(unprinted_designs[:], completed_models)



# EL ASTERISCO EN EL PARAMETRO SIRVE PARA CREAR UNA TUPLA TEMPORAL PARA USARLA EN LA FUNCION, Y ASI FUNCIONA SIN TENER QUE TENER UNA LISTA O TUPLA DE ANTEMANO
def make_pizza(size, *toppings):

    """Sumarize the pizza we are about to make."""
    print("\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# Los dos asteriscos ** sirven para poder creer las partes extra del objeto a crear con la funcion, siempre y cuando proporciones la key, value que faltan, como en la funcion de abajo
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


