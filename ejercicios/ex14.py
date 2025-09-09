# ----------------------------------------------------------
# EJERCICIO 14 - Comparar dos números
# ----------------------------------------------------------
# Ingresar dos números y mostrar cuál es mayor o si son iguales

# ========================
# MÉTODO 1: if-elif-else clásico
# ========================
print("\n🔹 MÉTODO 1: Estructura clásica")

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

if a > b:
    print("El primer número es mayor")
elif b > a:
    print("El segundo número es mayor")
else:
    print("Ambos valores son iguales")


# ========================
# MÉTODO 2: Función comparadora
# ========================
print("\n🔹 MÉTODO 2: Usando una función")

def comparar(x, y):
    if x > y:
        return "El primero es mayor"
    elif y > x:
        return "El segundo es mayor"
    else:
        return "Son iguales"

print(comparar(a, b))


# ========================
# MÉTODO 3: Ternario anidado
# ========================
print("\n🔹 MÉTODO 3: Operador ternario anidado")

resultado = "El primero es mayor" if a > b else ("El segundo es mayor" if b > a else "Son iguales")
print(resultado)


# ========================
# MÉTODO 4: Diccionario con comparación
# ========================
print("\n🔹 MÉTODO 4: Diccionario como decisión")

comparaciones = {
    True: "El primero es mayor",
    False: {
        True: "El segundo es mayor",
        False: "Son iguales"
    }
}

print(comparaciones[a > b] if a > b else comparaciones[False][b > a])


# ========================
# MÉTODO 5: Mostrar diferencia
# ========================
print("\n🔹 MÉTODO 5: Mostrar también diferencia")

if a == b:
    print("Son iguales")
else:
    diferencia = abs(a - b)
    mayor = "primero" if a > b else "segundo"
    print(f"El {mayor} número es mayor por {diferencia}")
