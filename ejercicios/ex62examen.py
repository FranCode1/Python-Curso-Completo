# -------------------------------------------------
# Ejercicio: Clasificación de cajas por peso (5 formas distintas)

#1. Clasificacion de Productos:
# Un sistema de envio recibe cajas con distintos pesos. Pedi al usuario que ingrese 10 pesos y clasificar cada uno en:
# - Liviano: Hasta 2kg
# - Mediano: entre 2kg y 5kg
# - Pesado: mas de 5kg
# Mostar cuantas cajas hay de cada tipo

# Autor: Franco Lugo
# -------------------------------------------------

# ✅ Forma 1: Con if simples y contadores
def clasificacion_1():
    liviano = mediano = pesado = 0
    for i in range(10):
        peso = float(input(f"Ingrese el peso de la caja {i+1}: "))
        if peso <= 2:
            liviano += 1
        elif peso <= 5:
            mediano += 1
        else:
            pesado += 1
    print(f"Livianos: {liviano}, Medianos: {mediano}, Pesados: {pesado}")


# ✅ Forma 2: Usando lista
def clasificacion_2():
    categorias = [0, 0, 0]  # [liviano, mediano, pesado]
    for i in range(10):
        peso = float(input(f"Ingrese el peso de la caja {i+1}: "))
        if peso <= 2:
            categorias[0] += 1
        elif peso <= 5:
            categorias[1] += 1
        else:
            categorias[2] += 1
    print(f"Livianos: {categorias[0]}, Medianos: {categorias[1]}, Pesados: {categorias[2]}")


# ✅ Forma 3: Usando diccionario
def clasificacion_3():
    categorias = {"Liviano": 0, "Mediano": 0, "Pesado": 0}
    for i in range(10):
        peso = float(input(f"Ingrese el peso de la caja {i+1}: "))
        if peso <= 2:
            categorias["Liviano"] += 1
        elif peso <= 5:
            categorias["Mediano"] += 1
        else:
            categorias["Pesado"] += 1
    print("Resultados:")
    for tipo, cantidad in categorias.items():
        print(f"{tipo}: {cantidad}")


# ✅ Forma 4: Usando función auxiliar
def obtener_categoria(peso):
    if peso <= 2:
        return "Liviano"
    elif peso <= 5:
        return "Mediano"
    return "Pesado"

def clasificacion_4():
    categorias = {"Liviano": 0, "Mediano": 0, "Pesado": 0}
    for i in range(10):
        peso = float(input(f"Ingrese el peso de la caja {i+1}: "))
        categoria = obtener_categoria(peso)
        categorias[categoria] += 1
    print("Resultados:")
    for tipo, cantidad in categorias.items():
        print(f"{tipo}: {cantidad}")


# ✅ Forma 5: Usando comprensión de listas
def clasificacion_5():
    pesos = [float(input(f"Ingrese el peso de la caja {i+1}: ")) for i in range(10)]
    livianos = sum(1 for p in pesos if p <= 2)
    medianos = sum(1 for p in pesos if 2 < p <= 5)
    pesados = sum(1 for p in pesos if p > 5)
    print(f"Livianos: {livianos}, Medianos: {medianos}, Pesados: {pesados}")


# -------------------------------------------------
# Menú principal
# -------------------------------------------------
if __name__ == "__main__":
    print("Clasificación de Cajas - 5 Métodos")
    print("1. If simples")
    print("2. Lista")
    print("3. Diccionario")
    print("4. Función auxiliar")
    print("5. Comprensión de listas")

    opcion = input("Elija una opción (1-5): ")

    if opcion == "1":
        clasificacion_1()
    elif opcion == "2":
        clasificacion_2()
    elif opcion == "3":
        clasificacion_3()
    elif opcion == "4":
        clasificacion_4()
    elif opcion == "5":
        clasificacion_5()
    else:
        print("❌ Opción inválida")
