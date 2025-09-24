# =====================================================================
# EJERCICIO 75: Introduccion a Clases
# ---------------------------------------------------------------------
# Crear una clase llamada alumno
# Que tenga los siguientes atributos:
# • nombre
# • edad
# • curso
# Crear dos objetos
# Asignar valores a cada atributo de cada objeto
# Mostrar por pantalla los datos de ambos alumnos
# =====================================================================

class Alumno:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

alumno1 = Alumno("Joaquin", 24, "3A")
alumno2 = Alumno("Alexander", 23, "4A")

def mostrar_objeto(objeto):
    # Se pueden recorrer los objetos de una clase, pero de estas
    # dos maneras unicamente
    # for clave, valor in objeto.__dict__.items():
    for clave, valor in vars(objeto).items():
        print(f"{clave}: {valor}")

mostrar_objeto(alumno1)
mostrar_objeto(alumno2)


# print(alumno1.nombre)
# print(alumno1.edad)
# print(alumno1.curso)

# print(alumno2.nombre)
# print(alumno2.edad)
# print(alumno2.curso)