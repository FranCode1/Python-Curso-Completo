# ----------------------------------------
# CLASE 11: SCOPE EN PYTHON
# ----------------------------------------

# El "scope" o ámbito de una variable define **dónde puede ser usada**.
# Hay 4 tipos de scope principales en Python:
# - Local
# - Enclosing (cierre)
# - Global
# - Built-in

# Se recuerdan con la regla **LEGB** (Local > Enclosing > Global > Built-in)


# ----------------------------------------
# 🌐 SCOPE GLOBAL

# Una variable definida FUERA de cualquier función tiene scope global

x = "global"

def mostrar_x():
    print("Desde la función:", x)

mostrar_x()
print("Desde fuera:", x)


# ----------------------------------------
# 🔒 SCOPE LOCAL

# Una variable creada DENTRO de una función tiene scope local

def funcion_local():
    y = "local"
    print("Dentro de la función:", y)

funcion_local()

# print(y)  # Error: y no está definida fuera de la función


# ----------------------------------------
# ⚠️ MODIFICAR UNA VARIABLE GLOBAL DESDE UNA FUNCIÓN

# Para modificar una variable global desde una función, se usa `global`

contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print("Contador:", contador)


# ----------------------------------------
# 🔁 SCOPE ENCLOSING (anidado)

# Una función dentro de otra puede acceder a variables de la función exterior

def exterior():
    mensaje = "enclosing"

    def interior():
        print("Mensaje interno:", mensaje)

    interior()

exterior()


# ----------------------------------------
# 🧪 MINI PROYECTO PRÁCTICO

# Crear un contador que recuerde su valor sin usar variables globales

# def crear_contador():
#     contador = 0

#     def incrementar():
#         nonlocal contador
#         contador += 1
#         return contador

#     return incrementar

# contador1 = crear_contador()

# print(contador1())  # 1
# print(contador1())  # 2
# print(contador1())  # 3


# ----------------------------------------
# BUILT-IN SCOPE (mencionado brevemente)

# Python tiene funciones integradas que siempre están disponibles:
print(len("Hola"))       # len() es parte del scope built-in
print(sum([1, 2, 3]))     # sum() también


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es el scope (ámbito) de una variable
# - La regla LEGB: Local > Enclosing > Global > Built-in
# - Cómo funcionan los scopes local, global y anidado
# - Cuándo usar global y nonlocal (con cuidado)
# - Cómo evitar errores comunes relacionados al ámbito

# Próxima clase: POO – Programación Orientada a Objetos.
