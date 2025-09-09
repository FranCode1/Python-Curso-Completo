# ----------------------------------------
# EJERCICIO 2 - Verificar si puede votar
# ----------------------------------------
# Solicitar la edad de una persona.
# Si tiene 16 años o más → "Puede votar"
# Si tiene menos de 16 años → "No puede votar"

# ========== MÉTODO 1: if-else clásico ==========
print("\n🔹 MÉTODO 1: Clásico con if-else")
edad = int(input("Ingrese su edad: "))
if edad >= 16:
    print("✅ Puede votar")
else:
    print("❌ No puede votar")


# ========== MÉTODO 2: operador ternario ==========
print("\n🔹 MÉTODO 2: Operador ternario")
edad2 = int(input("Edad: "))
mensaje2 = "✅ Puede votar" if edad2 >= 16 else "❌ No puede votar"
print(mensaje2)


# ========== MÉTODO 3: función con retorno ==========
print("\n🔹 MÉTODO 3: Usando una función")

def puede_votar(edad):
    if edad >= 16:
        return "✅ Puede votar"
    else:
        return "❌ No puede votar"

edad3 = int(input("Edad: "))
print(puede_votar(edad3))


# ========== MÉTODO 4: con match-case (Python 3.10+) ==========
print("\n🔹 MÉTODO 4: match-case (requiere Python 3.10+)")

def evaluar_voto(edad):
    match edad:
        case edad if edad >= 16:
            return "✅ Puede votar"
        case _:
            return "❌ No puede votar"

edad4 = int(input("Edad: "))
print(evaluar_voto(edad4))


# ========== MÉTODO 5: con diccionario booleano ==========
print("\n🔹 MÉTODO 5: Diccionario con expresión booleana")

edad5 = int(input("Edad: "))
resultado5 = {
    True: "✅ Puede votar",
    False: "❌ No puede votar"
}
print(resultado5[edad5 >= 16])
