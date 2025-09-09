# ----------------------------------------
# CLASE 9: DICCIONARIOS EN PYTHON
# ----------------------------------------

# Un diccionario almacena pares de clave:valor (key:value)
# Cada elemento tiene un nombre (la clave) y un contenido (el valor)

# Sintaxis: {clave: valor}

persona = {
    "nombre": "Franco",
    "edad": 22,
    "activo": True,
    "altura": 1.75
}

print(persona)
print(type(persona))  # <class 'dict'>


# ----------------------------------------
# 📌 ACCEDER A LOS VALORES

print(persona["nombre"])  # Franco

# ❗ Si accedés a una clave que no existe → error
# print(persona["peso"])  ← Esto da error

# ✔️ Con get(), evitamos el error si no existe
print(persona.get("peso"))         # None
print(persona.get("peso", "No definido"))  # mensaje por defecto


# ----------------------------------------
# ✏️ MODIFICAR Y AGREGAR VALORES

persona["edad"] = 23               # modificar
persona["ciudad"] = "Buenos Aires"  # agregar

print(persona)


# ----------------------------------------
# ❌ ELIMINAR ELEMENTOS

del persona["activo"]
print(persona)

# o con pop():
altura = persona.pop("altura")
print("Altura eliminada:", altura)


# ----------------------------------------
# 🔁 RECORRER UN DICCIONARIO

# Claves:
for clave in persona:
    print("Clave:", clave)

# Valores:
for valor in persona.values():
    print("Valor:", valor)

# Claves y valores:
for clave, valor in persona.items():
    print(f"{clave}: {valor}")


# ----------------------------------------
# 📦 DICCIONARIOS ANIDADOS

usuarios = {
    "franco": {"edad": 22, "rol": "admin"},
    "lucia": {"edad": 19, "rol": "editor"},
    "maxi": {"edad": 25, "rol": "viewer"}
}

print(usuarios["lucia"]["rol"])  # editor


# ----------------------------------------
# 🧪 MINI PROYECTO PRÁCTICO

# Crear un diccionario de contactos
# Agregar y consultar contactos por nombre

# contactos = {}

# while True:
#     accion = input("¿Querés 'agregar', 'consultar' o 'salir'? ").lower()

#     if accion == "salir":
#         break

#     elif accion == "agregar":
#         nombre = input("Nombre del contacto: ")
#         numero = input("Número: ")
#         contactos[nombre] = numero
#         print("Contacto guardado.")

#     elif accion == "consultar":
#         nombre = input("Nombre a buscar: ")
#         print("Número:", contactos.get(nombre, "No encontrado"))

# print("Agenda final:", contactos)


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es un diccionario (dict) y cómo se define
# - Cómo acceder, modificar, agregar y eliminar elementos
# - Cómo recorrer claves, valores o ambos
# - Cómo usar diccionarios anidados
# - Proyecto real de agenda de contactos

# Próxima clase: Funciones – cómo organizar y reutilizar tu código.
