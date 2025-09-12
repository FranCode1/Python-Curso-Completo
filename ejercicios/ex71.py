# =====================================================================
# EJERCICIO 71: Agenda Telefonica
# ---------------------------------------------------------------------
# Crear un diccionario donde las claves sean nombres de personas
# y los valores sus telefonos.
# El sistema debe tener el siguiente menú:
# • Agregar Contacto
# • Cambiar Numero de Telefono de un Contacto
# • Eliminar un Contacto
# • Mostar la agenda recorriendola
# • Salir
# =====================================================================


personas = {
    "Patricio": 1156453454,
    "Bob": 1445455676,
    "Cangrejo": 2298980909,
}

while True:
    print("Que desea hacer?: ")
    print("1 - Agregar Contacto")
    print("2 - Cambiar Numero de Contacto")
    print("3 - Eliminar un Contacto")
    print("4 - Mostrar Agenda")
    print("5 - Salir")

    decision = input("Elija una opcion de 1-5 \n")

    if decision == "1":
        nombre_contacto = input("Ingrese el nombre de contacto: ")
        numero_contacto = int(input("Ingrese el numero del contacto: "))
        personas[nombre_contacto] = numero_contacto
        print(f"Contacto Agregado: {nombre_contacto}: {numero_contacto}")

    elif decision == "2":
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre in personas:
            nuevo_contacto = int(input("Ingrese nuevo numero de contacto: "))
            personas[nombre] = nuevo_contacto
            print(f"Contacto actualizado: {nombre}: {nuevo_contacto}")
        else:
            print("Contacto no encontrado.")

    elif decision == "3":
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre in personas:
            # nuevo_contacto = int(input("Ingrese nuevo numero de contacto: "))
            del personas[nombre]
            print(f"Contacto eliminado")
        else:
            print("Contacto no encontrado.")

    elif decision == "4":
        if not personas:
            print("No hay contactos registrados.")
        else:
            print("Agenda Actual:")
            suma=0
            for nombre, numero in personas.items():
                print(f"• {nombre}: {numero}")

    elif decision == "5":
        print("Hasta luego")
        break

    else:
        print("Decision Erronea")