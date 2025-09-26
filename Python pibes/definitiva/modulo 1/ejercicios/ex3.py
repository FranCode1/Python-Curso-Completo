# ----------------------------------------
# PRÁCTICA - CLASE 3: print(), input() y escape sequences
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Mostrar mensaje simple
# Consigna: Mostrá el mensaje "Hola, bienvenido a Python".
print("Hola, bienvenido a Python")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Mostrar edad con print()
# Consigna: Creá una variable edad con valor 22 y mostrala así: "Edad: 22"
edad = 22
print("Edad:", edad)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Imprimir múltiples valores
# Consigna: Mostrá tu nombre y edad en una sola línea con varias comas.
print("Me llamo", "Franco", "y tengo", edad, "años")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Usar sep=
# Consigna: Mostrá las palabras "Python", "es", "fácil" separadas por guiones.
print("Python", "es", "fácil", sep="-")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Usar end=
# Consigna: Mostrá dos líneas, pero sin que haya salto entre ellas.
print("Primera parte", end="... ")
print("segunda parte")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Escape sequences
# Consigna: Mostrá lo siguiente exactamente como se ve:
# Nombre: Franco    Edad: 22
print("Nombre:\tFranco\tEdad:\t22")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Ruta de archivo
# Consigna: Mostrá esta ruta: C:\MisDocumentos\Proyectos\Python
print("C:\\MisDocumentos\\Proyectos\\Python")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Comillas dentro de un texto
# Consigna: Mostrá el texto: Él dijo: "Estoy aprendiendo Python".
print("Él dijo: \"Estoy aprendiendo Python\".")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Pedir datos con input()
# Consigna: Pedí el nombre del usuario y mostrá "Hola, [nombre]"
nombre = "Franco"  # Simulación de input
print("Hola,", nombre)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Edad futura
# Consigna: Pedí la edad del usuario y mostrá cuántos años tendrá en 5 años.
edad_usuario = 22  # Simulación de input con conversión
print(f"En 5 años tendrás {edad_usuario + 5} años.")

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
