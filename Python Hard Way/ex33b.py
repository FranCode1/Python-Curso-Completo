# ex33b.py

import ex33a

# Usando la función del módulo
ex33a.apple()  # Salida: I AM APPLES!

# Usando la variable del módulo
print(ex33a.tangerine)  # Salida: Living reflection of a dream

# Usando un diccionario (alternativa no relacionada al módulo)
mystuff_dict = {'apple': "I AM APPLES!"}
print(mystuff_dict['apple'])  # Salida: I AM APPLES!

# Usando la clase del módulo
thing = ex33a.MyStuff()
thing.apple()  # Salida: I AM CLASSY APPLES!
print(thing.tangerine)  # Salida: And now a thousand years between
