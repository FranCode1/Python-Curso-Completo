# ================================================================
# EJERCICIO 17 - Clasificar edad del socio
# ---------------------------------------------------------------
# - Menor a 18 → Juvenil
# - Entre 18 y 65 (inclusive) → Adulto
# - Mayor a 65 → Senior
# ================================================================


# 🔹 MÉTODO 1: if - elif - else clásico
edad = int(input("Método 1 - Ingrese su edad: "))

if edad < 18:
    print("El socio es juvenil")
elif 18 <= edad <= 65:
    print("El socio es adulto")
else:
    print("El socio es senior")


# 🔹 MÉTODO 2: función con return
def clasificar_edad(edad):
    if edad < 18:
        return "Juvenil"
    elif edad > 65:
        return "Senior"
    else:
        return "Adulto"

edad2 = int(input("\nMétodo 2 - Ingrese su edad: "))
print("El socio es", clasificar_edad(edad2))


# 🔹 MÉTODO 3: ternario anidado
edad3 = int(input("\nMétodo 3 - Ingrese su edad: "))

clasificacion = (
    "Juvenil" if edad3 < 18
    else "Senior" if edad3 > 65
    else "Adulto"
)

print("El socio es", clasificacion)


# 🔹 MÉTODO 4: uso de rangos con match-case (desde Python 3.10+)
edad4 = int(input("\nMétodo 4 - Ingrese su edad: "))

match edad4:
    case edad if edad < 18:
        print("El socio es juvenil")
    case edad if edad > 65:
        print("El socio es senior")
    case _:
        print("El socio es adulto")


# 🔹 MÉTODO 5: bucle hasta ingresar una edad válida (> 0)
while True:
    edad5 = int(input("\nMétodo 5 - Ingrese su edad (positiva): "))
    if edad5 <= 0:
        print("Edad inválida, intentá de nuevo.")
    else:
        if edad5 < 18:
            print("El socio es juvenil")
        elif edad5 > 65:
            print("El socio es senior")
        else:
            print("El socio es adulto")
        break
