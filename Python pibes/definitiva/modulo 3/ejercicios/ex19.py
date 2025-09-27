# ----------------------------------------
# CLASE 19: DISTRIBUCIÓN DE CÓDIGO EN PYTHON (EJERCICIOS)
# ----------------------------------------

# ==========================
# EJERCICIO 1
# ==========================
# Consigna: Crear una función en un archivo y probar que solo se ejecute el bloque main si se ejecuta directamente.
def hola():
    print("¡Hola, mundo!")

if __name__ == "__main__":
    print("Ej1: Ejecutado directamente")
    hola()


# ==========================
# EJERCICIO 2
# ==========================
# Consigna: Simular un archivo "operaciones.py" que defina sumar y restar con un bloque de pruebas.
def sumar(a, b): return a + b
def restar(a, b): return a - b

if __name__ == "__main__":
    print("Ej2: Prueba de operaciones")
    print("5 + 3 =", sumar(5, 3))
    print("5 - 2 =", restar(5, 2))


# ==========================
# EJERCICIO 3
# ==========================
# Consigna: Simular un "main.py" que importa la función sumar del módulo operaciones.
resultado = sumar(10, 20)
print("Ej3: Resultado desde main =", resultado)


# ==========================
# EJERCICIO 4
# ==========================
# Consigna: Crear una función utilitaria (helpers) en un submódulo ficticio.
def mostrar_mensaje(msg):
    return f"[INFO] {msg}"

print("Ej4:", mostrar_mensaje("Sistema iniciado"))


# ==========================
# EJERCICIO 5
# ==========================
# Consigna: Simular estructura de proyecto con utils/helpers.py y probar función saludo.
def saludo(nombre):
    return f"Hola, {nombre}"

print("Ej5:", saludo("Franco"))


# ==========================
# EJERCICIO 6
# ==========================
# Consigna: Crear una función "multiplicar" con bloque main para pruebas unitarias.
def multiplicar(a, b): return a * b

if __name__ == "__main__":
    print("Ej6: Probando multiplicación")
    print("4 * 5 =", multiplicar(4, 5))


# ==========================
# EJERCICIO 7
# ==========================
# Consigna: Simular un archivo de tests que verifica el resultado de sumar().
def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    return "Pruebas sumar() pasaron"

print("Ej7:", test_sumar())


# ==========================
# EJERCICIO 8
# ==========================
# Consigna: Simular un archivo de tests que verifica el resultado de restar().
def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5
    return "Pruebas restar() pasaron"

print("Ej8:", test_restar())


# ==========================
# EJERCICIO 9
# ==========================
# Consigna: Crear un módulo "calculadora" con funciones de suma, resta, mult y div, y probarlas desde un main.
def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

print("Ej9:", sumar(3, 2), restar(5, 1), multiplicar(4, 2), dividir(10, 2))


# ==========================
# EJERCICIO 10
# ==========================
# Consigna: Simular un proyecto "calculadora" con main.py que muestra resultados usando utils.
def mostrar_resultado(op, res):
    return f"Resultado de {op}: {res}"

if __name__ == "__main__":
    print("Ej10: Proyecto calculadora")
    print(mostrar_resultado("suma", sumar(7, 3)))
    print(mostrar_resultado("resta", restar(7, 3)))
    print(mostrar_resultado("multiplicación", multiplicar(7, 3)))
    print(mostrar_resultado("división", dividir(7, 3)))
