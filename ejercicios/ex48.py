# isAlpha(), isAlNum(), isSpace(), 

# =====================================================================
# EJERCICIO 48: Validar nombre y apellido
# ---------------------------------------------------------------------
# Pedí al usuario su nombre y apellido. Verificá que:
# •	Solo contenga letras.
# •	El nombre comience con mayúscula.
# •	No contenga números ni símbolos.
# =====================================================================

""""
def nombre_y_apellido(nombre, apellido):
    
    # hacer un for para recorrer el nombre y apellido, y asi verificar que no tenga numeros y simbolos, solo letras

    palabra_verificada = len(nombre)
    cont = 0
    
    for letra in nombre or apellido:
        cont += 1
        letra_verificada = letra.isalpha()
        
        if letra_verificada == True:
            continue
        else:
            print("El nombre contiene numeros o simbolos")
            break
        
    if cont == palabra_verificada:
        print("El nombre no posee numeros o simbolos")

nombre_y_apellido("j0aquin", "valdez")
"""

def validar_nombre_y_apellido():
    while True:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")

        # Condiciones de validación
        # longitud_valida = len(contraseña) >= 8
        # tiene_letra = False
        tiene_numero = False
        tiene_simbolo = False

        # Recorremos la contraseña para validar caracteres
        for caracter in nombre:
            # if caracter.isupper():
            #    tiene_mayuscula = True
            if caracter.isdigit():
                tiene_numero = True
            if caracter.isalpha():
                tiene_simbolo = True
        
        for caracter in apellido:
            if caracter.isdigit():
                tiene_numero = True
            if caracter.isalpha():
                tiene_simbolo = True

        # Verificamos condiciones y mostramos mensajes
        if tiene_numero:
            print("❌ Tu nombre no debe contener numeros.")
        if tiene_simbolo:
            print("❌ Tu nombre no debe contener simbolos")

        # Si todas las condiciones se cumplen, salimos del bucle
        if not tiene_simbolo and not tiene_numero:
            print("✅ Nombre y Apellido correctos.")
            break
        else:
            print("🔁 Intentá de nuevo.\n")

# Ejecutamos la función
validar_nombre_y_apellido()
