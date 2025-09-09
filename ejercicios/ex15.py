# ================================================================
# EJERCICIO 15 - Clasificación de nota
# ---------------------------------------------------------------
# - Mostrar "Desaprobado" si la nota es menor que 6
# - Mostrar "Aprobado" si la nota está entre 6 y 10 (inclusive)
# - Mostrar "Nota inválida" si está fuera de ese rango
# ================================================================


# 🔹 MÉTODO 1: if-elif-else clásico
nota = int(input("Método 1 - Ingrese una nota: "))

if nota < 6:
    print("Desaprobado")
elif 6 <= nota <= 10:
    print("Aprobado")
else:
    print("Nota inválida")


# 🔹 MÉTODO 2: Usando función para evaluar nota
def evaluar_nota(n):
    if n < 6:
        return "Desaprobado"
    elif 6 <= n <= 10:
        return "Aprobado"
    else:
        return "Nota inválida"

nota2 = int(input("\nMétodo 2 - Ingrese una nota: "))
print(evaluar_nota(nota2))


# 🔹 MÉTODO 3: Usando operador ternario anidado
nota3 = int(input("\nMétodo 3 - Ingrese una nota: "))

resultado = (
    "Desaprobado" if nota3 < 6
    else "Aprobado" if 6 <= nota3 <= 10
    else "Nota inválida"
)

print(resultado)


# 🔹 MÉTODO 4: Usando un diccionario para clasificar (con validación previa)
nota4 = int(input("\nMétodo 4 - Ingrese una nota: "))

if 0 <= nota4 <= 10:
    clasificacion = {
        True: "Aprobado",
        False: "Desaprobado"
    }
    print(clasificacion[nota4 >= 6])
else:
    print("Nota inválida")


# 🔹 MÉTODO 5: Validación dentro de un bucle hasta que ingrese una nota válida
while True:
    nota5 = int(input("\nMétodo 5 - Ingrese una nota: "))
    if nota5 < 0 or nota5 > 10:
        print("Nota inválida, intentá de nuevo.")
    else:
        if nota5 < 6:
            print("Desaprobado")
        else:
            print("Aprobado")
        break
