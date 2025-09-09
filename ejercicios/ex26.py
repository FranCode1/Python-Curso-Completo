# =====================================================================
# EJERCICIO 26: Un saludo personalizado
# ---------------------------------------------------------------------
# Hacer una función que reciba un nombre como parámetro y salude a la persona
# Entrada: saludar_persona("Ana")
# Salida: Hola, Ana
# =====================================================================

# ---------- Forma 1: función simple ----------
def saludo1(nombre):
    return f"Hola, {nombre}"

# ---------- Forma 2: función con print dentro ----------
def saludo2(nombre):
    print(f"Hola, {nombre}")

# ---------- Forma 3: usando concatenación ----------
def saludo3(nombre):
    return "Hola, " + nombre

# ---------- Forma 4: usando formato tradicional %
def saludo4(nombre):
    return "Hola, %s" % nombre

# ---------- Forma 5: usando f-string y saludo extendido ----------
def saludo5(nombre):
    return f"Hola, {nombre}! Qué gusto saludarte."

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    nombre = input("Ingrese un nombre: ")

    # Descomentar la forma que quieras probar
    print(saludo1(nombre))
    # saludo2(nombre)
    # print(saludo3(nombre))
    # print(saludo4(nombre))
    # print(saludo5(nombre))
