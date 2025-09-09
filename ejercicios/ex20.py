# =====================================================================
# EJERCICIO 20: Vocal o Consonante
# ---------------------------------------------------------------------
# Pedir al usuario una letra (solo minúscula) y mostrar si es:
# - Vocal
# - Consonante
# =====================================================================

# ---------- Forma 1: usando match/case ----------
def letra1():
    letra = input("Ingresar una letra (minúscula): ")
    match letra:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print("Es una vocal")
        case 'b' | 'c' | 'd' | 'f' | 'g' | 'h' | 'j' | 'k' | 'l' | 'm' | 'n' | 'ñ' | 'p' | 'q' | 'r' | 's' | 't' | 'v' | 'w' | 'x' | 'y' | 'z':
            print("Es una consonante")
        case _:
            print("Entrada inválida")

# ---------- Forma 2: usando if/elif ----------
def letra2():
    letra = input("Ingresar una letra (minúscula): ")
    if letra in "aeiou":
        print("Es una vocal")
    elif letra in "bcdfghjklmnñpqrstvwxyz":
        print("Es una consonante")
    else:
        print("Entrada inválida")

# ---------- Forma 3: usando listas ----------
def letra3():
    vocales = ['a', 'e', 'i', 'o', 'u']
    consonantes = [c for c in "bcdfghjklmnñpqrstvwxyz"]
    letra = input("Ingresar una letra (minúscula): ")

    if letra in vocales:
        print("Es una vocal")
    elif letra in consonantes:
        print("Es una consonante")
    else:
        print("Entrada inválida")

# ---------- Forma 4: usando sets ----------
def letra4():
    vocales = {'a','e','i','o','u'}
    consonantes = set("bcdfghjklmnñpqrstvwxyz")
    letra = input("Ingresar una letra (minúscula): ")

    if letra in vocales:
        print("Es una vocal")
    elif letra in consonantes:
        print("Es una consonante")
    else:
        print("Entrada inválida")

# ---------- Forma 5: usando operador ternario ----------
def letra5():
    letra = input("Ingresar una letra (minúscula): ")
    print("Es una vocal" if letra in "aeiou" else "Es una consonante" if letra in "bcdfghjklmnñpqrstvwxyz" else "Entrada inválida")

# =====================================================================
# Ejecución
# =====================================================================
if __name__ == "__main__":
    # Descomentar la función que quieras probar
    # letra1()
    # letra2()
    # letra3()
    # letra4()
    letra5()
