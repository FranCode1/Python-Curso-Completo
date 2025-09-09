# ============================================
# EJERCICIO 50: Validación de dirección postal
# Requisitos:
# - Calle solo letras y espacios
# - Altura solo números
# - Ningún campo vacío o con solo espacios
# ============================================


# 🔹 MÉTODO 1: Validación paso a paso (como el que ya hiciste)
def validar_direccion_1():
    print("\n🔹 MÉTODO 1:")
    while True:
        calle = input("Calle: ").strip()
        altura = input("Altura: ").strip()
        if not calle or not altura:
            print("❌ Ningún campo puede estar vacío.")
            continue
        if not all(c.isalpha() or c.isspace() for c in calle):
            print("❌ La calle sólo debe tener letras y espacios.")
            continue
        if not altura.isdigit():
            print("❌ La altura debe ser numérica.")
            continue
        print(f"✅ Dirección válida: {calle.title()} {altura}")
        break


# 🔹 MÉTODO 2: Función booleana para cada validación
def es_calle_valida(texto):
    return texto and all(c.isalpha() or c.isspace() for c in texto)

def es_altura_valida(texto):
    return texto.isdigit()

def validar_direccion_2():
    print("\n🔹 MÉTODO 2:")
    while True:
        calle = input("Calle: ").strip()
        altura = input("Altura: ").strip()
        if not es_calle_valida(calle):
            print("❌ Calle inválida.")
            continue
        if not es_altura_valida(altura):
            print("❌ Altura inválida.")
            continue
        print(f"✅ Dirección válida: {calle.title()} {altura}")
        break


# 🔹 MÉTODO 3: Función única que devuelve mensaje de error
def check_direccion(calle, altura):
    if not calle.strip() or not altura.strip():
        return "❌ No se puede dejar campos vacíos."
    if not all(c.isalpha() or c.isspace() for c in calle):
        return "❌ Calle solo debe tener letras y espacios."
    if not altura.isdigit():
        return "❌ Altura debe tener solo números."
    return "ok"

def validar_direccion_3():
    print("\n🔹 MÉTODO 3:")
    while True:
        calle = input("Calle: ")
        altura = input("Altura: ")
        resultado = check_direccion(calle, altura)
        if resultado == "ok":
            print(f"✅ Dirección válida: {calle.title()} {altura}")
            break
        else:
            print(resultado)


# 🔹 MÉTODO 4: Validación sin funciones, usando expresiones en una línea
def validar_direccion_4():
    print("\n🔹 MÉTODO 4:")
    while True:
        calle = input("Calle: ").strip()
        altura = input("Altura: ").strip()
        if calle and altura and all(c.isalpha() or c.isspace() for c in calle) and altura.isdigit():
            print(f"✅ Dirección válida: {calle.title()} {altura}")
            break
        print("❌ Dirección inválida. Revisá los campos.")


# 🔹 MÉTODO 5: Validación en función pura que devuelve True o False
def direccion_valida(calle, altura):
    return calle.strip() != "" and altura.strip().isdigit() and all(c.isalpha() or c.isspace() for c in calle)

def validar_direccion_5():
    print("\n🔹 MÉTODO 5:")
    while True:
        calle = input("Calle: ")
        altura = input("Altura: ")
        if direccion_valida(calle, altura):
            print(f"✅ Dirección válida: {calle.title()} {altura}")
            break
        else:
            print("❌ Dirección inválida.")


# --------------------------------------------
# Ejecutar todos los métodos
# --------------------------------------------
validar_direccion_1()
validar_direccion_2()
validar_direccion_3()
validar_direccion_4()
validar_direccion_5()
