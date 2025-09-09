# =====================================================================
# EJERCICIO 30: Área de un triángulo
# ---------------------------------------------------------------------
# Crear una función que reciba base y altura y devuelva el área del triángulo
# Fórmula: área = (base * altura) / 2
# Entrada: base=2, altura=6
# Salida: 6
# =====================================================================

# ---------- Forma 1: función simple ----------
def area_triangulo1(base, altura):
    return (base * altura) / 2

# ---------- Forma 2: usando operador *
def area_triangulo2(base, altura):
    area = base * altura / 2
    return area

# ---------- Forma 3: con función lambda ----------
area_triangulo3 = lambda b, h: (b * h) / 2

# ---------- Forma 4: usando función interna ----------
def area_triangulo4(base, altura):
    def calcular(b, h):
        return (b * h) / 2
    return calcular(base, altura)

# ---------- Forma 5: imprimir dentro de la función ----------
def area_triangulo5(base, altura):
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")
    return area

# =====================================================================
# Ejecución de ejemplo
# =====================================================================
if __name__ == "__main__":
    b = float(input("Ingrese la base del triángulo: "))
    h = float(input("Ingrese la altura del triángulo: "))

    print("Forma 1:", area_triangulo1(b, h))
    print("Forma 2:", area_triangulo2(b, h))
    print("Forma 3:", area_triangulo3(b, h))
    print("Forma 4:", area_triangulo4(b, h))
    area_triangulo5(b, h)
