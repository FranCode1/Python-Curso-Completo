# ----------------------------------------
# CLASE 7: LISTAS EN PYTHON
# ----------------------------------------

# Las listas son colecciones ordenadas y modificables de elementos.
# Se escriben entre corchetes [] y pueden contener cualquier tipo de dato.

# Crear una lista:
frutas = ["manzana", "banana", "naranja"]
numeros = [1, 2, 3, 4, 5]
mixta = [True, "Python", 3.14, 42]

print(frutas)
print(numeros)
print(mixta)


# ----------------------------------------
# 📦 ACCEDER A ELEMENTOS DE UNA LISTA

print(frutas[0])  # Primer elemento
print(frutas[1])  # Segundo elemento
print(frutas[-1]) # Último elemento (índices negativos funcionan)


# ----------------------------------------
# ✏️ MODIFICAR ELEMENTOS

frutas[0] = "pera"
print(frutas)  # ["pera", "banana", "naranja"]


# ----------------------------------------
# ➕ AGREGAR ELEMENTOS

# append() agrega al final
frutas.append("uva")
print(frutas)

# insert(posición, valor)
frutas.insert(1, "kiwi")
print(frutas)


# ----------------------------------------
# ➖ ELIMINAR ELEMENTOS

# remove(valor)
frutas.remove("banana")
print(frutas)

# pop() saca el último por defecto, o uno específico
ultimo = frutas.pop()
print("Se eliminó:", ultimo)
print(frutas)

# del elimina por índice
del frutas[0]
print(frutas)


# ----------------------------------------
# 🔁 RECORRER UNA LISTA

for fruta in frutas:
    print("Fruta:", fruta)

# También con índices
for i in range(len(frutas)):
    print(f"frutas[{i}] = {frutas[i]}")


# ----------------------------------------
# 🔄 MÉTODOS ÚTILES DE LISTAS

numeros = [5, 2, 9, 1, 7]

print("Original:", numeros)
numeros.sort()          # ordena de menor a mayor
print("Ordenado:", numeros)

numeros.reverse()       # invierte el orden
print("Reverso:", numeros)

print("Largo:", len(numeros))  # cantidad de elementos

print("¿Está el 2?", 2 in numeros)


# ----------------------------------------
# 🎯 SLICING (rebanar listas)

# lista[inicio:fin:paso]
letras = ["a", "b", "c", "d", "e", "f"]

print(letras[1:4])   # ['b', 'c', 'd']
print(letras[:3])    # ['a', 'b', 'c']
print(letras[::2])   # ['a', 'c', 'e']


# ----------------------------------------
# 🧪 MINI PROYECTO DE PRÁCTICA

# Crear una lista de tareas vacía
# Dejar que el usuario agregue tareas
# Mostrar la lista actualizada cada vez

# tareas = []

# while True:
#     tarea = input("Agregá una tarea (o escribí 'salir'): ")
#     if tarea.lower() == "salir":
#         break
#     tareas.append(tarea)
#     print("Tareas actuales:", tareas)

# print("Lista final de tareas:", tareas)


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es una lista y cómo se crea
# - Cómo acceder, modificar, agregar y eliminar elementos
# - Cómo recorrer listas y usar slicing
# - Métodos útiles: append, insert, pop, sort, reverse, len
# - A crear listas dinámicas con input

# Próxima clase: Trabajando más a fondo con listas y colecciones: listas anidadas, comprehensions y más.
