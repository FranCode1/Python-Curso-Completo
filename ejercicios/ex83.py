# =====================================================================
# EJERCICIO 83: Clase Libro
# ---------------------------------------------------------------------
# Crear una clase "libro" con atributos (encapsulados)
# • titulo
# • autor
# • año
# • prestado
# • cantidad_veces_prestado
# En el programa inicial crear una lista vacía
# Permitir cargar tres biblioteca en la lista
# Recorrer la lista mostrando los datos
# Métodos:
# • Constructor: recibe los datos de los atributos [LISTO]
# • Mostrar_Datos: Muestra todos los atributos [LISTO]
# • mostrar_disponibles: Muestra todos los de biblioteca disponibles [LISTO]
# • libro_prestado: Marca un libro como prestado segun su nombre [LISTO]
# • mostrar_prestados: Muestra todos los biblioteca prestados y el
# usuario marca uno como disponible [LISTO]
# • cantidad_veces_prestado: Muestra la cantidad de veces que se presto el libro [LISTO]
# • mostrar-estadistica: Muestra cantidad de veces prestado, porcentaje de veces prestados, cantidad de libros disponibles y mostrar los datos del libro mas prestado
# =====================================================================

class Libro:
    def __init__(self, titulo, autor, año):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año
        self.__prestado = False
        self.__cantidad_veces_prestado = 0

    # -----------------------------
    # Métodos
    # -----------------------------
    def prestar(self):
        if self.__prestado:
            print(f"❌ El libro '{self.__titulo}' ya está prestado.")
        else:
            self.__prestado = True
            self.__cantidad_veces_prestado += 1
            print(f"✅ Ahora el libro '{self.__titulo}' está prestado.")

    def devolver(self):
        if not self.__prestado:
            print(f"📗 El libro '{self.__titulo}' ya estaba disponible.")
        else:
            self.__prestado = False
            print(f"📘 El libro '{self.__titulo}' fue devuelto y ahora está disponible.")

    def mostrar_datos(self):
        estado = "Prestado" if self.__prestado else "Disponible"
        print(f"📖 '{self.__titulo}' - {self.__autor} ({self.__año}) | Estado: {estado} | Veces prestado: {self.__cantidad_veces_prestado}")

    def esta_disponible(self):
        return not self.__prestado

    def get_titulo(self):
        return self.__titulo

    def get_cantidad_prestamos(self):
        return self.__cantidad_veces_prestado


# -----------------------------
# Funciones auxiliares
# -----------------------------
def mostrar_disponibles(biblioteca):
    print("\n📚 Libros disponibles:")
    disponibles = [libro for libro in biblioteca if libro.esta_disponible()]
    if not disponibles:
        print("No hay libros disponibles.")
    else:
        for libro in disponibles:
            libro.mostrar_datos()


def mostrar_prestados(biblioteca):
    print("\n📕 Libros prestados:")
    prestados = [libro for libro in biblioteca if not libro.esta_disponible()]
    if not prestados:
        print("No hay libros prestados.")
    else:
        for i, libro in enumerate(prestados, 1):
            print(f"{i}. {libro.get_titulo()}")
        opcion = int(input("Ingrese el número del libro a devolver (0 para cancelar): "))
        if 1 <= opcion <= len(prestados):
            prestados[opcion - 1].devolver()


def mostrar_estadistica(biblioteca):
    print("\n📊 Estadísticas:")

    total_prestamos = sum(libro.get_cantidad_prestamos() for libro in biblioteca)
    total_libros = len(biblioteca)
    disponibles = sum(1 for libro in biblioteca if libro.esta_disponible())

    print(f"Total de préstamos realizados: {total_prestamos}")
    print(f"Cantidad de libros disponibles: {disponibles}/{total_libros}")

    if total_prestamos > 0:
        mas_prestado = max(biblioteca, key=lambda l: l.get_cantidad_prestamos())
        porcentaje = (mas_prestado.get_cantidad_prestamos() / total_prestamos) * 100
        print(f"📌 Libro más prestado: '{mas_prestado.get_titulo()}' con {mas_prestado.get_cantidad_prestamos()} préstamos ({porcentaje:.2f}% del total)")
    else:
        print("Aún no se prestaron libros.")


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================
biblioteca = []

# Cargar libros
for i in range(3):
    titulo = input(f"Ingrese el nombre del libro {i+1}: ")
    autor = input("Ingrese el nombre del autor: ")
    año = int(input("Ingrese el año de publicación: "))
    biblioteca.append(Libro(titulo, autor, año))

# Mostrar todos los libros
print("\n📚 Biblioteca cargada:")
for libro in biblioteca:
    libro.mostrar_datos()

# Ejemplo de uso
mostrar_disponibles(biblioteca)
biblioteca[0].prestar()
mostrar_prestados(biblioteca)
mostrar_estadistica(biblioteca)
