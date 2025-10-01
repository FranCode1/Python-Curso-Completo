# ----------------------------------------
# CLASE 2: VARIABLES Y TIPOS DE DATOS
# ----------------------------------------

# 📌 ¿Qué es una variable?
# Es un "nombre" que guarda un valor para poder reutilizarlo más adelante.

# Podemos pensar en una variable como una caja con etiqueta.
# Ejemplo: caja = "manzana" → la caja se llama "caja" y guarda el valor "manzana"

# 🔤 Crear variables en Python es muy simple:
nombre = "Franco"
edad = 22
altura = 1.78
activo = True

# Mostramos los valores en pantalla
print(nombre)
print(edad)
print(altura)
print(activo)


# ----------------------------------------
# TIPO DE DATOS EN PYTHON
# ----------------------------------------

# Python detecta automáticamente el tipo de dato (tipado dinámico)

print(type(nombre))   # str (cadena de texto)
print(type(edad))     # int (entero)
print(type(altura))   # float (decimal)
print(type(activo))   # bool (booleano)

# Python tiene muchos tipos de datos, pero los más básicos son:
# - int: números enteros (1, 100, -5)
# - float: números decimales (3.14, -0.5)
# - str: cadenas de texto ("Hola")
# - bool: verdadero o falso (True / False)


# ----------------------------------------
# CAMBIAR EL VALOR DE UNA VARIABLE
# ----------------------------------------

# Podemos reasignar un valor a una variable en cualquier momento:
edad = 23
print("Edad actualizada:", edad)

# Incluso cambiar el tipo de valor:
edad = "veintitrés"
print("Ahora edad es:", edad, "y su tipo es:", type(edad))


# ----------------------------------------
# NOMBRAR BIEN LAS VARIABLES
# ----------------------------------------

# ✅ Reglas para nombres válidos:
# - Deben comenzar con letra o guion bajo
# - No pueden tener espacios
# - No pueden usar caracteres especiales
# - No pueden llamarse como palabras clave de Python (como `print`, `if`, etc.)

# Ejemplos válidos:
_nombre = "ok"
miEdad = 30
altura_en_metros = 1.75

# Ejemplos inválidos (NO USAR):
# 2cosas = "no"     ← no puede empezar con número
# mi-edad = 22      ← no puede tener guiones
# class = "error"   ← `class` es palabra reservada


# ----------------------------------------
# CONVERTIR ENTRE TIPOS DE DATOS
# ----------------------------------------

# A veces queremos convertir datos (casting)

numero = "45"
print(numero, type(numero))  # str

numero = int(numero)         # convertimos a int
print(numero, type(numero))  # int

decimal = float("3.14")
texto = str(100)
booleano = bool(1)           # True (0 es False, todo lo demás es True)


# ----------------------------------------
# CONCATENAR STRINGS Y MEZCLAR TIPOS
# ----------------------------------------

# Esto funciona:
saludo = "Hola, " + nombre
print(saludo)

# Esto NO funciona: (error)
# print("Tengo " + edad + " años") ← edad es int

# Para arreglarlo, convertimos a str:
print("Tengo " + str(edad) + " años")

# Otra forma moderna:
print(f"{nombre} tiene {edad} años y mide {altura}m")

# Las f-strings (f"...") permiten insertar variables fácilmente.


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es una variable y cómo se usa
# - Tipos de datos básicos en Python: int, float, str, bool
# - Reglas para nombrar variables correctamente
# - Cómo convertir entre tipos
# - Cómo concatenar textos y usar f-strings

# Próxima clase: Listas – estructuras para guardar múltiples valores
