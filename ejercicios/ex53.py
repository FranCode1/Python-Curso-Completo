# ================================================================
# EJERCICIO 53: Normalización de títulos
# ---------------------------------------------------------------
# Pedir al usuario el título de un libro y mostrarlo:
# - Todo en mayúsculas
# - Con cada palabra en mayúscula (formato título)
# ================================================================


# 🔹 MÉTODO 1: Usando .upper() y .title()
titulo = input("Método 1 - Ingresá el título del libro: ")

print("🔠 MAYÚSCULAS:", titulo.upper())
print("🔤 FORMATO TÍTULO:", titulo.title())


# 🔹 MÉTODO 2: Función que imprime ambos formatos
def mostrar_titulo(t):
    print("🔠 MAYÚSCULAS:", t.upper())
    print("🔤 FORMATO TÍTULO:", t.title())

titulo2 = input("\nMétodo 2 - Ingresá el título del libro: ")
mostrar_titulo(titulo2)


# 🔹 MÉTODO 3: Guardar ambos formatos en variables
titulo3 = input("\nMétodo 3 - Ingresá el título del libro: ")
mayus = titulo3.upper()
titulo_formato = titulo3.title()
print("🔠:", mayus)
print("🔤:", titulo_formato)


# 🔹 MÉTODO 4: Convertir palabra por palabra manualmente
titulo4 = input("\nMétodo 4 - Ingresá el título del libro: ")
palabras = titulo4.split()
formateado = " ".join([p.capitalize() for p in palabras])
print("🔠:", titulo4.upper())
print("🔤:", formateado)


# 🔹 MÉTODO 5: Bucle hasta que el título no esté vacío
while True:
    titulo5 = input("\nMétodo 5 - Ingresá el título del libro: ").strip()
    if titulo5:
        print("🔠:", titulo5.upper())
        print("🔤:", titulo5.title())
        break
    else:
        print("⚠️ Ingresá al menos una palabra.")
