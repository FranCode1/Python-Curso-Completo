# ----------------------------------------
# CLASE 6: BUCLES EN PYTHON
# ----------------------------------------

# Los bucles nos permiten ejecutar una sección de código varias veces.

# En Python tenemos dos tipos principales:
# - while → se repite mientras una condición sea verdadera
# - for → se repite sobre una secuencia (lista, string, rango, etc.)


# ----------------------------------------
# 🔁 BUCLE WHILE
# ----------------------------------------

# while condición:
#     hacer algo mientras la condición sea True

contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1  # importante: modificar la variable para evitar bucle infinito

print("Fin del bucle while")


# ----------------------------------------
# ⚠️ CUIDADO CON BUCLES INFINITOS

# Este ejemplo se ejecutaría para siempre (¡NO LO HAGAS!)
# while True:
#     print("Nunca termina")

# Siempre asegurate de que la condición cambie en algún momento


# ----------------------------------------
# 🔁 BUCLE FOR
# ----------------------------------------

# for variable in secuencia:
#     hacer algo

# Ejemplo con rango de números:
for i in range(5):  # range(5) genera los números 0,1,2,3,4
    print("Número:", i)

# Ejemplo con lista:
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print("Me gusta la", fruta)

# Ejemplo con string (cada letra es un carácter):
for letra in "Python":
    print(letra)


# ----------------------------------------
# 📌 FUNCIONES ÚTILES EN BUCLES FOR

# range(inicio, fin, paso)
for i in range(1, 10, 2):  # de 1 a 9, de 2 en 2
    print(i)

# enumerate() → devuelve el índice y el valor
for indice, fruta in enumerate(frutas):
    print(indice, "-", fruta)


# ----------------------------------------
# 🧱 CONTROL DE BUCLES: break y continue

# break → sale del bucle antes de tiempo
for i in range(10):
    if i == 5:
        break
    print("i:", i)

# continue → salta al siguiente ciclo
for i in range(5):
    if i == 2:
        continue
    print("Valor:", i)


# ----------------------------------------
# 🧪 MINI PROYECTO DE PRÁCTICA

# Pedir al usuario que ingrese contraseñas hasta que escriba la correcta

# contraseña_correcta = "python123"
# intento = ""

# while intento != contraseña_correcta:
#     intento = input("Ingresá la contraseña: ")
#     if intento != contraseña_correcta:
#         print("Incorrecta. Intentá de nuevo.")

# print("¡Acceso concedido!")


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - A usar el bucle while y su lógica condicional
# - A recorrer listas, strings y rangos con for
# - Cómo usar range(), enumerate(), break y continue
# - A repetir acciones según condiciones del usuario

# Próxima clase: colecciones avanzadas — más sobre listas, y cómo usar diccionarios, tuplas y sets.
