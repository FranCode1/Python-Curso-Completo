# =====================================================================
# EJERCICIO 74: Sistema de Notas
# ---------------------------------------------------------------------
# Inizializar un diccionario con las materias del primer año.
# Crear un menú con las siguientes opciones:
# • 1 - Agregar nota de una materia
# • 2 - Cambiar nota de una materia
# • 3 - Mostrar promedio de notas
# • 4 - Salir
# =====================================================================

materias = {
    "Analisis": 0,
    "Practicas": 0,
    "Arquitectura": 0,
    "Algebra": 0,
    "Sistemas": 0,
    "Algoritmos": 0,
    "Ingles": 0,
    "Ciencia": 0,
}

while True:
    print("Que desea hacer?: ")
    print("1 - Agregar nota")
    print("2 - Cambiar nota de una materia")
    print("3 - Mostrar promedio de antes")
    print("4 - Salir")

    decision = input("Elija una opcion de 1-4 \n")

    if decision == "1":
        nombre_materia = input("Ingrese el nombre de la materia: ")
        numero_nota = int(input("Ingrese la nota de la materia: "))
        materias[nombre_materia] = numero_nota
        print(f"Materia Agregado: {nombre_materia}: {numero_nota}")

    elif decision == "2":
        nombre = input("Ingrese el nombre de la materia a modificar: ")
        if nombre in materias:
            nuevo_nota = int(input("Ingrese la nueva nota: "))
            materias[nombre] = nuevo_nota
            print(f"Nota actualizada: {nombre}: {nuevo_nota}")
        else:
            print("Materia no encontrada.")

    elif decision == "3":
        if not materias:
            print("No hay materias registradas.")
        else:
            print("Listado de materias:")
            suma=0
            for nota in materias.values():
                #print(f"• {nombre}: {nota}")
                suma += nota
            promedio = suma/len(materias)
            print(f"El promedio de las notas es: {promedio}")

    elif decision == "4":
        print("Hasta luego")
        break

    else:
        print("Decision Erronea")