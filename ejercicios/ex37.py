# =====================================================================
# EJERCICIO 37: Función que recibe nombre, apellido y edad
# ---------------------------------------------------------------------
# Crear una función que reciba nombre, apellido y edad e imprima
# todos los datos en orden.
# =====================================================================

# ---------- Forma 1: usando print directo ----------
def dni1(nombre, apellido, edad):
    print(nombre, apellido, edad)

# ---------- Forma 2: usando f-string ----------
def dni2(nombre, apellido, edad):
    print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")

# ---------- Forma 3: usando join y lista ----------
def dni3(nombre, apellido, edad):
    print(" ".join([str(nombre), str(apellido), str(edad)]))

# ---------- Forma 4: retornando string y luego imprimir ----------
def dni4(nombre, apellido, edad):
    return f"{nombre} {apellido} {edad}"

# ---------- Forma 5: usando diccionario ----------
def dni5(nombre, apellido, edad):
    persona = {"Nombre": nombre, "Apellido": apellido, "Edad": edad}
    for key, value in persona.items():
        print(f"{key}: {value}")

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    nombre_input = input("Ingrese el nombre: ")
    apellido_input = input("Ingrese el apellido: ")
    edad_input = input("Ingrese la edad: ")

    print("\nForma 1:")
    dni1(nombre_input, apellido_input, edad_input)

    print("\nForma 2:")
    dni2(nombre_input, apellido_input, edad_input)

    print("\nForma 3:")
    dni3(nombre_input, apellido_input, edad_input)

    print("\nForma 4:")
    print(dni4(nombre_input, apellido_input, edad_input))

    print("\nForma 5:")
    dni5(nombre_input, apellido_input, edad_input)
