# ----------------------------------------
# PRÁCTICA - CLASE 7: LISTAS EN PYTHON
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Crear y mostrar una lista
# Consigna: Crear una lista con 5 colores y mostrarla.
colores = ["rojo", "verde", "azul", "amarillo", "violeta"]
print("Lista de colores:", colores)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Acceder a elementos
# Consigna: Mostrar el primer, tercer y último color de la lista.
print("Primer color:", colores[0])
print("Tercer color:", colores[2])
print("Último color:", colores[-1])

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Modificar elementos
# Consigna: Cambiar el segundo color por "naranja" y mostrar la lista.
colores[1] = "naranja"
print("Lista modificada:", colores)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Agregar elementos
# Consigna: Agregar "celeste" al final y "negro" en la posición 2.
colores.append("celeste")
colores.insert(2, "negro")
print("Lista con nuevos colores:", colores)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Eliminar elementos
# Consigna: Eliminar "amarillo" y el último color con pop.
colores.remove("amarillo")
ultimo = colores.pop()
print("Se eliminó:", ultimo)
print("Lista actual:", colores)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Recorrer lista con for
# Consigna: Mostrar cada color de la lista con su índice.
for i in range(len(colores)):
    print(f"colores[{i}] = {colores[i]}")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Ordenar y revertir lista
# Consigna: Ordenar la lista de números y luego invertirla.
numeros = [8, 3, 6, 1, 9]
print("Original:", numeros)
numeros.sort()
print("Ordenado:", numeros)
numeros.reverse()
print("Reverso:", numeros)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Verificar existencia
# Consigna: Verificar si el número 3 está en la lista.
existe = 3 in numeros
print("¿El número 3 está en la lista?", existe)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Slicing de una lista
# Consigna: Mostrar los primeros 3 colores, del segundo al cuarto, y de 2 en 2.
print("Primeros 3:", colores[:3])
print("Del segundo al cuarto:", colores[1:4])
print("De 2 en 2:", colores[::2])

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Lista dinámica de tareas (versión simulada)
# Consigna: Simular agregar tareas a una lista.
tareas = []
entradas = ["estudiar", "hacer ejercicio", "leer", "salir"]

for entrada in entradas:
    tareas.append(entrada)
    print("Tareas actuales:", tareas)

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
