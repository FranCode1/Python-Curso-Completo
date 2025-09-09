# =====================================================================
# EJERCICIO 68: Control de Stock (5 formas)
# ---------------------------------------------------------------------
# Una librería almacena los títulos de los libros en una lista:
# libros = ["Python", "Java Fundamental", "SQL Practico", "HTML5"]
# • Permitir que el usuario busque un título.
# • Si lo encuentra, mostrar "Disponible".
# • Si no está, agregarlo a la lista de pedidos.
# • Mostrar todos los libros en stock alfabéticamente.
# =====================================================================


# ---------- Forma 1: Básica con listas ----------
def forma1():
    libros = ["Python", "Java Fundamental", "SQL Practico", "HTML5"]
    pedidos = []
    buscado = input("Ingrese el libro que desea buscar: ")

    if buscado in libros:
        print(f"El libro '{buscado}' está disponible.")
    else:
        print(f"El libro '{buscado}' no está disponible. Se agregará a pedidos.")
        pedidos.append(buscado)

    libros.sort()
    print("Stock ordenado:", libros)
    print("Pedidos:", pedidos)


# ---------- Forma 2: Usando set para evitar duplicados ----------
def forma2():
    libros = {"Python", "Java Fundamental", "SQL Practico", "HTML5"}
    pedidos = set()
    buscado = input("Ingrese el libro que desea buscar: ")

    if buscado in libros:
        print(f"El libro '{buscado}' está disponible.")
    else:
        print(f"El libro '{buscado}' no está disponible. Se agregará a pedidos.")
        pedidos.add(buscado)

    print("Stock ordenado:", sorted(libros))
    print("Pedidos:", pedidos)


# ---------- Forma 3: Con diccionario (stock con disponibilidad) ----------
def forma3():
    libros = {
        "Python": True,
        "Java Fundamental": True,
        "SQL Practico": True,
        "HTML5": True
    }
    pedidos = []
    buscado = input("Ingrese el libro que desea buscar: ")

    if libros.get(buscado, False):
        print(f"El libro '{buscado}' está disponible.")
    else:
        print(f"El libro '{buscado}' no está disponible. Se agregará a pedidos.")
        pedidos.append(buscado)

    print("Stock ordenado:", sorted(libros.keys()))
    print("Pedidos:", pedidos)


# ---------- Forma 4: Funciones auxiliares ----------
def forma4():
    def mostrar_stock(libros):
        print("Stock ordenado:", sorted(libros))

    def buscar(libros, pedidos, buscado):
        if buscado in libros:
            print(f"El libro '{buscado}' está disponible.")
        else:
            print(f"El libro '{buscado}' no está disponible. Se agregará a pedidos.")
            pedidos.append(buscado)

    libros = ["Python", "Java Fundamental", "SQL Practico", "HTML5"]
    pedidos = []
    buscado = input("Ingrese el libro que desea buscar: ")
    buscar(libros, pedidos, buscado)
    mostrar_stock(libros)
    print("Pedidos:", pedidos)


# ---------- Forma 5: Con clase Libreria ----------
class Libreria:
    def __init__(self):
        self.libros = ["Python", "Java Fundamental", "SQL Practico", "HTML5"]
        self.pedidos = []

    def buscar(self, titulo):
        if titulo in self.libros:
            print(f"El libro '{titulo}' está disponible.")
        else:
            print(f"El libro '{titulo}' no está disponible. Se agregará a pedidos.")
            self.pedidos.append(titulo)

    def mostrar_stock(self):
        print("Stock ordenado:", sorted(self.libros))

    def mostrar_pedidos(self):
        print("Pedidos:", self.pedidos)


def forma5():
    libreria = Libreria()
    buscado = input("Ingrese el libro que desea buscar: ")
    libreria.buscar(buscado)
    libreria.mostrar_stock()
    libreria.mostrar_pedidos()


# ---------- Menú principal ----------
def main():
    print("=== EJERCICIO 68 - 5 Formas ===")
    print("1. Básica con listas")
    print("2. Con set (sin repetidos)")
    print("3. Con diccionario")
    print("4. Con funciones auxiliares")
    print("5. Con clase Librería")
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
