# =====================================================================
# EJERCICIO 38: Función con parámetros por defecto y desordenables
# ---------------------------------------------------------------------
# Modificar el ejercicio 37 para que la función pueda ser llamada
# con los argumentos en cualquier orden usando parámetros por defecto.
# =====================================================================

# ---------- Forma 1: print directo ----------
def dni1(nombre='', apellido='', edad=''):
    print(nombre, apellido, edad)

# ---------- Forma 2: usando f-string ----------
def dni2(nombre='', apellido='', edad=''):
    print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")

# ---------- Forma 3: usando join y lista ----------
def dni3(nombre='', apellido='', edad=''):
    print(" ".join([str(nombre), str(apellido), str(edad)]))

# ---------- Forma 4: retornando string ----------
def dni4(nombre='', apellido='', edad=''):
    return f"{nombre} {apellido} {edad}"

# ---------- Forma 5: usando diccionario ----------
def dni5(nombre='', apellido='', edad=''):
    persona = {"Nombre": nombre, "Apellido": apellido, "Edad": edad}
    for key, value in persona.items():
        print(f"{key}: {value}")

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    print("\nForma 1:")
    dni1(edad=25, nombre="Ana", apellido="González")

    print("\nForma 2:")
    dni2(apellido="Pérez", nombre="Luis", edad=30)

    print("\nForma 3:")
    dni3(edad=40, nombre="Carla", apellido="Suárez")

    print("\nForma 4:")
    print(dni4(nombre="Miguel", edad=35, apellido="Torres"))

    print("\nForma 5:")
    dni5(apellido="López", nombre="Laura", edad=28)
