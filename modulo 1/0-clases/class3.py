# ----------------------------------------
# CLASE 3: print(), input() y escape sequences
# ----------------------------------------

# 🖨️ print() → sirve para mostrar información en pantalla

print("Hola, mundo")
print("Esto es Python")

# También podés imprimir números, variables o resultados:
edad = 22
print("Edad:", edad)
print("La suma de 2 + 3 es", 2 + 3)

# Podés imprimir varias cosas separadas por coma:
print("Mi nombre es", "Franco", "y tengo", edad, "años")

# El argumento sep= define el separador entre los valores:
print("Python", "es", "genial", sep=" - ")

# El argumento end= cambia lo que se imprime al final (por defecto es \n)
print("Línea 1", end="... ")
print("Línea 2")


# ----------------------------------------
# 🎯 Escape Sequences → Caracteres especiales en texto
# ----------------------------------------

# Algunas secuencias útiles:
# \n → salto de línea
# \t → tabulación (espacio grande)
# \\ → barra invertida
# \" → comillas dobles dentro de un string

print("Primera línea\nSegunda línea")
print("Nombre:\tFranco")
print("C:\\Users\\Franco\\Documentos")  # Ruta en Windows
print("Dijo: \"Hola\" y se fue.")

# ¿Para qué sirven?
# - Para formatear texto
# - Para rutas de archivos
# - Para agregar detalles visuales


# ----------------------------------------
# ⌨️ input() → permite pedir datos al usuario

# nombre = input("¿Cómo te llamás? ")
# print("Hola,", nombre)

# ⚠️ Lo que devuelve input siempre es un string

# edad = input("¿Cuántos años tenés? ")
# print("Tenés", edad, "años")

# Si querés hacer operaciones numéricas, convertí el input:
# edad = int(input("¿Cuántos años tenés? "))
# print("En 5 años tendrás", edad + 5)

# Otra forma con f-strings:
# print(f"Hola {nombre}, en 5 años vas a tener {edad + 5}")


# ----------------------------------------
# 🧪 Ejercicio de práctica

# 1. Pedir el nombre del usuario
# 2. Pedir su edad
# 3. Mostrar un mensaje que diga: "Hola [nombre], tenés [edad] años."

# Descomentalo para probar:
# nombre = input("Tu nombre: ")
# edad = int(input("Tu edad: "))
# print(f"Hola {nombre}, tenés {edad} años.")


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - A usar print() para mostrar datos
# - Cómo usar sep= y end= para controlar la salida
# - Qué son las escape sequences (\n, \t, etc.)
# - A usar input() para pedir datos al usuario
# - A convertir tipos cuando necesitás operar con números

# En la próxima clase: operaciones con variables, operadores matemáticos y más tipos de printing.
