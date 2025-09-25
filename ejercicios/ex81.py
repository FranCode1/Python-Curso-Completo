# =====================================================================
# EJERCICIO 81: Estudiantes
# ---------------------------------------------------------------------
# Crear una clase llamada Estudiantes, con los siguientes campos:
# • nombre
# • edad
# • nota
# Cargar 5 estudiantes
# Mostrar el nombre de los estudiantes que aprobaron
# =====================================================================

class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def aprobado(self):
        return self.nota >= 7

    def __str__(self):
        return f"{self.nombre} (Edad: {self.edad}, Nota: {self.nota})"


def main():
    estudiantes = []

    # Cargar 5 estudiantes
    for i in range(5):
        print(f"\n--- Estudiante {i+1} ---")
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        nota = float(input("Ingrese la nota: "))
        estudiantes.append(Estudiante(nombre, edad, nota))

    # Mostrar estudiantes que aprobaron
    print("\nEstudiantes que aprobaron:")
    for est in estudiantes:
        if est.aprobado():
            print(f"- {est.nombre} (Nota: {est.nota})")


if __name__ == "__main__":
    main()
