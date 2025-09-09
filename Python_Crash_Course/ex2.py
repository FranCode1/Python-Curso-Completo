# ---------- CREACIÓN DE LISTAS Y ACCESO A ELEMENTOS ----------

# Lista de bicicletas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f'My first bicycle was a {bicycles[0].title()}.'  # Accede al primer elemento y lo capitaliza

# Lista de motocicletas
motorcycles = ['honda', 'yamaha', 'suzuki']

# Impresiones básicas
print(bicycles)
print(bicycles[0])             # Primer elemento
print(bicycles[0].title())     # Primer elemento capitalizado
print(bicycles[1])             # Segundo elemento
print(bicycles[3])             # Cuarto elemento
print(bicycles[-1])            # Último elemento

print(message)                 # Muestra el mensaje creado

print(motorcycles)             # Imprime lista original

# ---------- MODIFICACIÓN DE ELEMENTOS EN LA LISTA ----------

motorcycles[0] = 'ducati'      # Cambia 'honda' por 'ducati'
print(motorcycles)

motorcycles.append('ducati')   # Agrega 'ducati' al final
print(motorcycles)

# ---------- CREACIÓN Y LLENADO DE LISTA VACÍA ----------

motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamada')  # Error tipográfico: debería ser 'yamaha'
motorcycles2.append('suzuki')
print(motorcycles2)

# ---------- INSERCIÓN DE ELEMENTOS ----------

motorcycles3 = ['honda', 'yamada', 'suzuki']
motorcycles3.insert(0, 'ducati')   # Inserta 'ducati' al inicio
print(motorcycles3)

# ---------- ELIMINACIÓN DE ELEMENTOS CON 'del' ----------

motorcycles4 = ['honda', 'yamada', 'suzuki']
del motorcycles4[0]                # Elimina 'honda'
print(motorcycles4)

del motorcycles4[1]                # Elimina 'suzuki'
print(motorcycles4)

# ---------- USO DE 'pop()' PARA ELIMINAR Y USAR ELEMENTOS ----------

motorcycles5 = ['honda', 'yamada', 'suzuki']

popped_motorcycle = motorcycles5.pop()  # Elimina el último
print(motorcycles5)
print(popped_motorcycle)

# ---------- USO DE 'pop()' EN POSICIONES ESPECÍFICAS ----------

motorcycles6 = ['honda', 'yamada', 'suzuki']

last_owned = motorcycles6.pop()       # Elimina y guarda el último
print(f'The last motorcycle I owned was a {last_owned.title()}.')

first_owned = motorcycles6.pop(0)     # Elimina y guarda el primero
print(f'The first motorcycle I owned was a {first_owned.title()}.')

# ---------- ELIMINACIÓN POR VALOR CON 'remove()' ----------

motorcycles7 = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles7.remove('ducati')         # Elimina 'ducati' por valor
print(motorcycles7)

motorcycles8 = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles8.remove(too_expensive)
print(motorcycles8)
print(f'\nA {too_expensive.title()} is too expensive for me.')

# ---------- ORDENAMIENTO PERMANENTE CON 'sort()' ----------

cars1 = ['bmw', 'audi', 'toyota', 'subaru']
cars1.sort()                          # Orden alfabético permanente
print(cars1)

cars2 = ['bmw', 'audi', 'toyota', 'subaru']
cars2.sort(reverse=True)             # Orden inverso permanente
print(cars2)

# ---------- ORDENAMIENTO TEMPORAL CON 'sorted()' ----------

cars3 = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars3)

print('\nHere is the sorted list:')
print(sorted(cars3))                 # No modifica la original

print('\nHere is the original list again:')
print(cars3)

# ---------- INVERSIÓN DE LISTA CON 'reverse()' ----------

cars4 = ['bmw', 'audi', 'toyota', 'subaru']
cars4.reverse()                      # Invierte el orden de la lista
print(cars4)

# ---------- OBTENER LONGITUD DE LA LISTA ----------

cars5 = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars5))                    # Devuelve 4

# ---------- ERRORES COMUNES: ÍNDICES FUERA DE RANGO ----------

motorcycles9 = ['honda', 'yamaha', 'suzuki']
# print(motorcycles9[3])             # ❌ Error: índice 3 no existe

# ---------- ACCESO AL ÚLTIMO ELEMENTO DE UNA LISTA ----------

motorcycles10 = ['honda', 'yamaha', 'suzuki']
print(motorcycles10[-1])             # Devuelve 'suzuki'

# ---------- ERRORES AL ACCEDER A ELEMENTOS DE LISTAS VACÍAS ----------

motorcycles11 = []
# print(motorcycles11[-1])          # ❌ Error: la lista está vacía
