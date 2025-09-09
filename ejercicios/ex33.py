# =====================================================================
# EJERCICIO 33: Contar vocales en una palabra
# ---------------------------------------------------------------------
# Crear una función que reciba una palabra y devuelva la cantidad
# de vocales que contiene.
# Entrada: "Murciélago"
# Salida: 5
# =====================================================================

# ---------- Forma 1: usando match/case ----------
def contar_vocales1(palabra):
    contador = 0
    for letra in palabra.lower():
        match letra:
            case 'a'|'e'|'i'|'o'|'u':
                contador += 1
    return contador

# ---------- Forma 2: usando in ----------
def contar_vocales2(palabra):
    contador = 0
    for letra in palabra.lower():
        if letra in 'aeiou':
            contador += 1
    return contador

# ---------- Forma 3: usando list comprehension ----------
def contar_vocales3(palabra):
    return sum(1 for letra in palabra.lower() if letra in 'aeiou')

# ---------- Forma 4: usando filter ----------
def contar_vocales4(palabra):
    return len(list(filter(lambda x: x in 'aeiou', palabra.lower())))

# ---------- Forma 5: usando replace iterativo ----------
def contar_vocales5(palabra):
    palabra_lower = palabra.lower()
    total_vocales = 0
    for vocal in 'aeiou':
        total_vocales += palabra_lower.count(vocal)
    return total_vocales

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    palabra_input = input("Ingrese una palabra: ")

    print("\nForma 1:", contar_vocales1(palabra_input))
    print("Forma 2:", contar_vocales2(palabra_input))
    print("Forma 3:", contar_vocales3(palabra_input))
    print("Forma 4:", contar_vocales4(palabra_input))
    print("Forma 5:", contar_vocales5(palabra_input))
