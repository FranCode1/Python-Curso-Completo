# ----------------------------------------
# EJERCICIO 6 - Verificar si un número está en el rango de dos números dados
# ----------------------------------------
# Se ingresan dos números (num1, num2) y luego un tercer número (num3)
# Se determina si num3 está dentro del rango definido por num1 y num2 (sin importar el orden)

# ========== MÉTODO 1: if-else clásico con comparación doble ==========
print("\n🔹 MÉTODO 1: if-else clásico")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if (num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2):
    print("El tercer número se encuentra en el rango de los dos primeros números.")
elif num3 == num1 and num3 == num2:
    print("Todos los valores son iguales.")
else:
    print("El tercer número no se encuentra en el rango de los dos primeros números.")


# ========== MÉTODO 2: usando min() y max() ==========
print("\n🔹 MÉTODO 2: Usando min() y max()")

num1_2 = float(input("Primer número: "))
num2_2 = float(input("Segundo número: "))
num3_2 = float(input("Tercer número: "))

if min(num1_2, num2_2) < num3_2 < max(num1_2, num2_2):
    print("El tercer número está dentro del rango.")
elif num3_2 == num1_2 == num2_2:
    print("Todos los números son iguales.")
else:
    print("El tercer número NO está dentro del rango.")


# ========== MÉTODO 3: función con retorno booleano ==========
print("\n🔹 MÉTODO 3: Función que verifica rango")

def esta_en_rango(a, b, c):
    if a == b == c:
        return "Todos los números son iguales."
    elif min(a, b) < c < max(a, b):
        return "El tercer número está dentro del rango."
    else:
        return "El tercer número NO está dentro del rango."

num1_3 = float(input("Primer número: "))
num2_3 = float(input("Segundo número: "))
num3_3 = float(input("Tercer número: "))

print(esta_en_rango(num1_3, num2_3, num3_3))


# ========== MÉTODO 4: usando operador ternario ==========
print("\n🔹 MÉTODO 4: Operador ternario")

num1_4 = float(input("Primer número: "))
num2_4 = float(input("Segundo número: "))
num3_4 = float(input("Tercer número: "))

mensaje = (
    "Todos los números son iguales." if num3_4 == num1_4 == num2_4 else
    "El tercer número está dentro del rango." if min(num1_4, num2_4) < num3_4 < max(num1_4, num2_4) else
    "El tercer número NO está dentro del rango."
)
print(mensaje)


# ========== MÉTODO 5: usando match-case (Python 3.10+) ==========
print("\n🔹 MÉTODO 5: match-case")

num1_5 = float(input("Primer número: "))
num2_5 = float(input("Segundo número: "))
num3_5 = float(input("Tercer número: "))

match True:
    case _ if num3_5 == num1_5 == num2_5:
        print("Todos los números son iguales.")
    case _ if min(num1_5, num2_5) < num3_5 < max(num1_5, num2_5):
        print("El tercer número está dentro del rango.")
    case _:
        print("El tercer número NO está dentro del rango.")
