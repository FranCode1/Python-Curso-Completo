# =====================================================================
# EJERCICIO 69: Ordenar una Lista (5 formas)
# ---------------------------------------------------------------------
# Alturas = [180, 195, 172, 200, 176, 190]
# • Ordenar de mayor a menor (sin sort() ni sorted()).
# • Mostrar el más alto y el más bajo.
# =====================================================================

alturas_original = [180, 195, 172, 200, 176, 190]


# ---------- Forma 1: Burbuja ----------
def forma1():
    alturas = alturas_original[:]
    n = len(alturas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if alturas[j] < alturas[j + 1]:  # Descendente
                alturas[j], alturas[j + 1] = alturas[j + 1], alturas[j]
    print("Burbuja:", alturas)
    print("Más alto:", alturas[0], "Más bajo:", alturas[-1])


# ---------- Forma 2: Selección ----------
def forma2():
    alturas = alturas_original[:]
    n = len(alturas)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if alturas[j] > alturas[max_idx]:
                max_idx = j
        alturas[i], alturas[max_idx] = alturas[max_idx], alturas[i]
    print("Selección:", alturas)
    print("Más alto:", alturas[0], "Más bajo:", alturas[-1])


# ---------- Forma 3: Inserción ----------
def forma3():
    alturas = alturas_original[:]
    for i in range(1, len(alturas)):
        key = alturas[i]
        j = i - 1
        while j >= 0 and key > alturas[j]:
            alturas[j + 1] = alturas[j]
            j -= 1
        alturas[j + 1] = key
    print("Inserción:", alturas)
    print("Más alto:", alturas[0], "Más bajo:", alturas[-1])


# ---------- Forma 4: QuickSort ----------
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    mayores = [x for x in lista[1:] if x >= pivote]
    menores = [x for x in lista[1:] if x < pivote]
    return quicksort(mayores) + [pivote] + quicksort(menores)


def forma4():
    alturas = alturas_original[:]
    alturas = quicksort(alturas)
    print("QuickSort:", alturas)
    print("Más alto:", alturas[0], "Más bajo:", alturas[-1])


# ---------- Forma 5: Usando max y remove ----------
def forma5():
    alturas = alturas_original[:]
    ordenadas = []
    while alturas:
        max_val = max(alturas)
        ordenadas.append(max_val)
        alturas.remove(max_val)
    print("Max+Remove:", ordenadas)
    print("Más alto:", ordenadas[0], "Más bajo:", ordenadas[-1])


# ---------- Menú principal ----------
def main():
    print("=== EJERCICIO 69 - 5 Formas ===")
    print("1. Burbuja")
    print("2. Selección")
    print("3. Inserción")
    print("4. QuickSort")
    print("5. Max + Remove")
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
