# ----------------------------------------
# PRÁCTICA - CLASE 9: DICCIONARIOS EN PYTHON
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Crear un diccionario
# Consigna: Crear un diccionario llamado "alumno" con nombre, edad y curso.
alumno = {
    "nombre": "Lucía",
    "edad": 20,
    "curso": "Python"
}
print("Diccionario alumno:", alumno)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Acceder a un valor
# Consigna: Mostrar el curso del alumno.
print("Curso:", alumno["curso"])

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Usar get() para evitar errores
# Consigna: Obtener el valor de la clave "email" sin generar error.
print("Email:", alumno.get("email", "No registrado"))

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Modificar y agregar claves
# Consigna: Cambiar la edad a 21 y agregar la clave "email".
alumno["edad"] = 21
alumno["email"] = "lucia@email.com"
print("Alumno actualizado:", alumno)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Eliminar claves
# Consigna: Eliminar la clave "curso" del diccionario.
del alumno["curso"]
print("Sin curso:", alumno)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Usar pop() para eliminar y guardar el valor
# Consigna: Eliminar "email" con pop y mostrar su valor.
email = alumno.pop("email")
print("Email eliminado:", email)
print("Alumno final:", alumno)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Recorrer claves
# Consigna: Imprimir solo las claves del diccionario.
persona = {"nombre": "Franco", "edad": 22, "ciudad": "Buenos Aires"}
for clave in persona:
    print("Clave:", clave)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Recorrer claves y valores
# Consigna: Imprimir cada clave y su valor con items().
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Diccionario anidado
# Consigna: Crear un diccionario de productos con info anidada.
productos = {
    "001": {"nombre": "Mouse", "precio": 1500},
    "002": {"nombre": "Teclado", "precio": 3000}
}
print("Producto 002:", productos["002"]["nombre"], "-", productos["002"]["precio"])

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Mini agenda de contactos
# Consigna: Crear una agenda con 3 contactos y permitir buscar uno.
agenda = {
    "franco": "1234",
    "lucia": "5678",
    "maxi": "9012"
}

nombre = "lucia"
print(f"Teléfono de {nombre}:", agenda.get(nombre, "No encontrado"))

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
