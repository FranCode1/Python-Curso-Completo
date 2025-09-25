# =====================================================================
# EJERCICIO 79: Clase Libro
# ---------------------------------------------------------------------
# Crear una clase llamada Libro con atributos encapsulados:
# • __titulo
# • __autor
# • __año
# En el programa inicial crear una lista vacia
# Permitir cargar tres libros en la lista
# Recorrer la lista mostrando los datos
# La clase debe tener como metodos:
# • contstructor: Recibe los datos de los atributos
# • mostrar_datos: Muestra todos los atributos
# =====================================================================

class Libro:
    def __init__(self, titulo, autor, año):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año

    def mostrar_datos(self):
        print(f"El libro '{self.__titulo}' del autor {self.__autor} publicado en {self.__año}")

# Pedir al usuario la cantidad de libros
cantidad = 3

# Lista para guardar los objetos de Libro
libros = []

for i in range(cantidad):
    titulo = input(f"Ingrese el nombre del libro {i+1}: ")
    autor = input(f"Ingrese el nombre del autor: ")
    año = int(input("Ingrese el año de publicacion: "))

    libro = Libro(titulo, autor, año)
    libros.append(libro)

# Mostrar los datos y si estan aprobados
for libro in libros:
    libro.mostrar_datos()