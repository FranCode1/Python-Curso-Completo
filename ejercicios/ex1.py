# ----------------------------------------
# EJERCICIO 1 - Cálculo del IMC
# ----------------------------------------
# Dado el peso y altura de una persona, calcular su IMC (Índice de Masa Corporal)
# Fórmula: IMC = peso / (altura ** 2)
# Clasificación:
#   - Menor a 18.5 → Bajo peso
#   - Entre 18.5 y 24.9 → Normal
#   - 25 o más → Sobrepeso

# ========== MÉTODO 1: if-elif-else clásico ==========
print("\n🔹 MÉTODO 1: Clásico con if-elif-else")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("IMC:", round(imc, 2), "- Bajo peso")
elif imc <= 24.9:
    print("IMC:", round(imc, 2), "- Normal")
else:
    print("IMC:", round(imc, 2), "- Sobrepeso")


# ========== MÉTODO 2: usando una función ==========
print("\n🔹 MÉTODO 2: Función con retorno de clasificación")

def clasificar_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return imc, "Bajo peso"
    elif imc <= 24.9:
        return imc, "Normal"
    else:
        return imc, "Sobrepeso"

peso2 = float(input("Peso: "))
altura2 = float(input("Altura: "))
imc2, clasificacion2 = clasificar_imc(peso2, altura2)
print(f"IMC: {round(imc2,2)} - {clasificacion2}")


# ========== MÉTODO 3: con diccionario y expresiones booleanas ==========
print("\n🔹 MÉTODO 3: Diccionario y lógica booleana")

peso3 = float(input("Peso: "))
altura3 = float(input("Altura: "))
imc3 = peso3 / (altura3 ** 2)

clasificaciones = {
    imc3 < 18.5: "Bajo peso",
    18.5 <= imc3 <= 24.9: "Normal",
    imc3 > 24.9: "Sobrepeso"
}

for condicion, mensaje in clasificaciones.items():
    if condicion:
        print(f"IMC: {round(imc3,2)} - {mensaje}")
        break


# ========== MÉTODO 4: con operador ternario anidado ==========
print("\n🔹 MÉTODO 4: Operador ternario")

peso4 = float(input("Peso: "))
altura4 = float(input("Altura: "))
imc4 = peso4 / (altura4 ** 2)

resultado4 = (
    "Bajo peso" if imc4 < 18.5 else
    "Normal" if imc4 <= 24.9 else
    "Sobrepeso"
)

print(f"IMC: {round(imc4, 2)} - {resultado4}")


# ========== MÉTODO 5: con función y match-case (Python 3.10+) ==========
print("\n🔹 MÉTODO 5: match-case (Python 3.10 o superior)")

def clasificacion_match(imc):
    match imc:
        case _ if imc < 18.5:
            return "Bajo peso"
        case _ if imc <= 24.9:
            return "Normal"
        case _:
            return "Sobrepeso"

peso5 = float(input("Peso: "))
altura5 = float(input("Altura: "))
imc5 = peso5 / (altura5 ** 2)
clasificacion5 = clasificacion_match(imc5)

print(f"IMC: {round(imc5,2)} - {clasificacion5}")
