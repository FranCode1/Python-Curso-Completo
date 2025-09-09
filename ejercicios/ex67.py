# =====================================================================
# EJERCICIO 67: Control de Notas Archivo (5 formas)
# ---------------------------------------------------------------------
# Pedir al usuario una lista de artículos para comprar, y que al
# finalizar la carga:
# • Muestre toda la lista.
# • Pedir al usuario un artículo para borrar.
# • Pedir al usuario un artículo y agregarlo al final.
# =====================================================================


# ---------- Forma 1: Clásica con listas ----------
def forma1():
    lista = []
    cantidad = int(input("Ingrese la cantidad de artículos a comprar: "))
    for i in range(cantidad):
        lista.append(input(f"Ingrese el artículo {i+1}: "))
    print("\nLista inicial:", lista)

    borrar = input("Ingrese el artículo a borrar: ")
    if borrar in lista:
        lista.remove(borrar)
    print("Lista luego de borrar:", lista)

    agregar = input("Ingrese un artículo para agregar: ")
    lista.append(agregar)
    print("Lista final:", lista)


# ---------- Forma 2: Con set (para evitar repetidos) ----------
def forma2():
    lista = set()
    cantidad = int(input("Ingrese la cantidad de artículos a comprar: "))
    for i in range(cantidad):
        lista.add(input(f"Ingrese el artículo {i+1}: "))
    print("\nLista inicial:", lista)

    borrar = input("Ingrese el artículo a borrar: ")
    lista.discard(borrar)  # no da error si no existe
    print("Lista luego de borrar:", lista)

    agregar = input("Ingrese un artículo para agregar: ")
    lista.add(agregar)
    print("Lista final:", lista)


# ---------- Forma 3: Con comprensión de listas ----------
def forma3():
    cantidad = int(input("Ingrese la cantidad de artículos a comprar: "))
    lista = [input(f"Ingrese el artículo {i+1}: ") for i in range(cantidad)]
    print("\nLista inicial:", lista)

    borrar = input("Ingrese el artículo a borrar: ")
    lista = [x for x in lista if x != borrar]
    print("Lista luego de borrar:", lista)

    agregar = input("Ingrese un artículo para agregar: ")
    lista = lista + [agregar]
    print("Lista final:", lista)


# ---------- Forma 4: Con diccionario para indexar ----------
def forma4():
    cantidad = int(input("Ingrese la cantidad de artículos a comprar: "))
    lista = {i+1: input(f"Ingrese el artículo {i+1}: ") for i in range(cantidad)}
    print("\nLista inicial:", lista)

    borrar = input("Ingrese el artículo a borrar: ")
    lista = {k: v for k, v in lista.items() if v != borrar}
    print("Lista luego de borrar:", lista)

    agregar = input("Ingrese un artículo para agregar: ")
    lista[len(lista)+1] = agregar
    print("Lista final:", lista)


# ---------- Forma 5: Con manejo tipo pila/cola ----------
def forma5():
    from collections import deque
    cantidad = int(input("Ingrese la cantidad de artículos a comprar: "))
    lista = deque([input(f"Ingrese el artículo {i+1}: ") for i in range(cantidad)])
    print("\nLista inicial:", lista)

    borrar = input("Ingrese el artículo a borrar: ")
    try:
        lista.remove(borrar)
    except ValueError:
        pass
    print("Lista luego de borrar:", lista)

    agregar = input("Ingrese un artículo para agregar: ")
    lista.append(agregar)  # agrega al final
    print("Lista final:", lista)


# ---------- Menú principal ----------
def main():
    print("=== EJERCICIO 67 - 5 Formas ===")
    print("1. Clásica con listas")
    print("2. Con set (sin repetidos)")
    print("3. Con comprensión de listas")
    print("4. Con diccionario indexado")
    print("5. Con deque (pila/cola)")
    opcion = input("Elija la forma (1-5): ")

    if opcion == "1":
        forma1()
    elif opcion == "2":
        forma2()
    elif opcion == "3":
        forma3()
    elif opcion == "4":
        forma4()
    elif opcion == "5":
        forma5()
    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()
