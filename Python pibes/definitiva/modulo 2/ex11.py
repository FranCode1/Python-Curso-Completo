# ----------------------------------------
# PRÁCTICA - CLASE 11: SCOPE EN PYTHON
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Scope global
# Consigna: Crear una variable global y mostrar su valor dentro y fuera de una función.

nombre = "Franco"

def mostrar_nombre():
    print("Desde la función:", nombre)

mostrar_nombre()
print("Desde fuera:", nombre)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Scope local
# Consigna: Crear una variable local dentro de una función y tratar de acceder fuera (mostrar error).

def definir_local():
    edad = 25
    print("Dentro de la función:", edad)

definir_local()
# print(edad)  # Esto daría error: 'edad' no está definida fuera

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Global con modificación
# Consigna: Modificar una variable global desde una función usando `global`.

contador = 0

def aumentar():
    global contador
    contador += 1

aumentar()
print("Contador global:", contador)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Scope anidado (enclosing)
# Consigna: Crear una función dentro de otra que use variables de la función exterior.

def saludar_persona(nombre):
    saludo = "Hola"

    def mensaje():
        print(f"{saludo}, {nombre}!")

    mensaje()

saludar_persona("Lucía")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Scope enclosing con `nonlocal`
# Consigna: Crear un contador interno que no use `global` sino `nonlocal`.

def crear_contador():
    cuenta = 0

    def aumentar():
        nonlocal cuenta
        cuenta += 1
        return cuenta

    return aumentar

contador1 = crear_contador()
print(contador1())  # 1
print(contador1())  # 2
print(contador1())  # 3

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Mismo nombre en scopes distintos
# Consigna: Mostrar cómo una variable local puede ocultar una global.

x = "global"

def test():
    x = "local"
    print("Dentro:", x)

test()
print("Fuera:", x)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Uso de `global` con string
# Consigna: Convertir una variable global en mayúsculas desde una función.

mensaje = "hola"

def convertir():
    global mensaje
    mensaje = mensaje.upper()

convertir()
print("Mensaje convertido:", mensaje)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Evitar modificar global por error
# Consigna: Crear una función que reciba parámetros y no toque variables globales.

usuario = "Franco"

def cambiar_usuario(nombre):
    nombre = nombre.upper()
    print("Dentro de la función:", nombre)

cambiar_usuario(usuario)
print("Fuera de la función:", usuario)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Built-in vs. variables
# Consigna: Evitar sobrescribir funciones built-in como `sum`.

# sum = 100  # ❌ Nunca hagas esto: rompe la función sum()

# print(sum([1, 2, 3]))  # Esto fallaría si sum está sobrescrito

numeros = [1, 2, 3]
print("Suma:", sum(numeros))  # ✅ correcto

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Función generadora de saludos
# Consigna: Crear una función que devuelva otra función personalizada con scope enclosing.

def generar_saludo(nombre):
    def saludar():
        print(f"¡Hola {nombre}, buen día!")
    return saludar

saludo_franco = generar_saludo("Franco")
saludo_franco()

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
