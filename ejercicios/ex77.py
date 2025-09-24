# =====================================================================
# EJERCICIO 77: Clase Alumno
# ---------------------------------------------------------------------
# Crear la clase Alumno co los atributos:
# • __nombre
# • __nota
# El constructor inicializa ambos valores por parametro.
# Metodos:
# • aprobado: Devuelve True si la nota es mayor o igual a 7
# • cargar_nota: Recibe nota y la guarda en su atributo.
# • mostrar_datos: Imprime nombre y nota
# 
# Pedir al usuario cuantos alumnos desea cargar.
# Crear los objetos con los datos ingresados por teclado y mostrar si el alumno esta aprobado. =====================================================================

class Alumno:
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    def aprobado(self):
        return self.__nota >= 7
        
    def cargar_nota(self, nueva_nota):
        self.__nota = nueva_nota

    def mostrar_datos(self):
        print(f"{self.__nombre} tiene una nota de {self.__nota}")

# Pedir al usuario la cantidad de alumnos
cantidad = int(input("¿Cuántos alumnos desea cargar? "))

# Lista para guardar los objetos Alumno
alumnos = []

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    alumno = Alumno(nombre, nota)
    alumnos.append(alumno)

# Mostrar los datos y si están aprobados
for alumno in alumnos:
    alumno.mostrar_datos()
    if alumno.aprobado():
        print("Está aprobado")
    else:
        print("No está aprobado")
    print("-" * 30)
