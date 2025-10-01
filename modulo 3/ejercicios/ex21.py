# ----------------------------------------
# CLASE 21: MANEJO DE EXCEPCIONES EN PYTHON
# ----------------------------------------

# 📌 Ejercicios prácticos resueltos


# ==========================================================
# EJERCICIO 1: Capturar ZeroDivisionError
# Consigna: Pedir dos números y dividirlos. Manejar el error si el divisor es 0.
# ==========================================================
try:
    a, b = 10, 0
    print("Resultado:", a / b)
except ZeroDivisionError:
    print("✅ Ejercicio 1: Error capturado -> No se puede dividir por cero.")


# ==========================================================
# EJERCICIO 2: Manejar ValueError
# Consigna: Convertir una cadena a número entero, pero manejar si no es válido.
# ==========================================================
try:
    numero = int("abc")
    print("Número:", numero)
except ValueError:
    print("✅ Ejercicio 2: Error capturado -> No se puede convertir texto a número.")


# ==========================================================
# EJERCICIO 3: Capturar múltiples excepciones
# Consigna: Manejar ValueError y ZeroDivisionError en el mismo bloque.
# ==========================================================
try:
    x = int("10")
    y = int("0")
    print(x / y)
except (ValueError, ZeroDivisionError) as e:
    print("✅ Ejercicio 3: Error capturado ->", e)


# ==========================================================
# EJERCICIO 4: Uso de else
# Consigna: Intentar abrir un archivo inexistente y usar else si se abre bien.
# ==========================================================
try:
    archivo = open("inexistente.txt", "r")
except FileNotFoundError:
    print("✅ Ejercicio 4: Error capturado -> Archivo no encontrado.")
else:
    print("Archivo abierto correctamente.")
    archivo.close()


# ==========================================================
# EJERCICIO 5: Uso de finally
# Consigna: Simular apertura de archivo con bloque finally que siempre se ejecute.
# ==========================================================
try:
    archivo = open("inexistente.txt", "r")
except FileNotFoundError:
    print("✅ Ejercicio 5: Error capturado -> Archivo no existe.")
finally:
    print("Bloque finally ejecutado.")


# ==========================================================
# EJERCICIO 6: Capturar el mensaje de error
# Consigna: Intentar dividir por cero y mostrar los detalles del error.
# ==========================================================
try:
    resultado = 5 / 0
except ZeroDivisionError as e:
    print("✅ Ejercicio 6: Detalles del error ->", e)


# ==========================================================
# EJERCICIO 7: Excepción personalizada
# Consigna: Crear una excepción para edades negativas.
# ==========================================================
class EdadInvalidaError(Exception):
    """Excepción para edades menores a 0."""
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa.")

try:
    validar_edad(-3)
except EdadInvalidaError as e:
    print("✅ Ejercicio 7: Error personalizado capturado ->", e)


# ==========================================================
# EJERCICIO 8: Manejo de TypeError
# Consigna: Intentar sumar número con cadena y capturar el error.
# ==========================================================
try:
    resultado = 5 + "cinco"
except TypeError as e:
    print("✅ Ejercicio 8: Error capturado ->", e)


# ==========================================================
# EJERCICIO 9: Diccionario seguro
# Consigna: Intentar acceder a una clave que no existe en un diccionario.
# ==========================================================
try:
    datos = {"nombre": "Franco"}
    print(datos["edad"])
except KeyError as e:
    print("✅ Ejercicio 9: Error capturado -> La clave no existe:", e)


# ==========================================================
# EJERCICIO 10: Mini calculadora segura
# Consigna: Crear una función que reciba 2 números y un operador,
# y maneje entradas inválidas con excepciones.
# ==========================================================
def calculadora_segura(a, b, operacion):
    try:
        if operacion == "+":
            return a + b
        elif operacion == "-":
            return a - b
        elif operacion == "*":
            return a * b
        elif operacion == "/":
            return a / b
        else:
            raise ValueError("Operación inválida")
    except ZeroDivisionError:
        return "❌ No se puede dividir por cero."
    except ValueError as e:
        return f"❌ {e}"

print("✅ Ejercicio 10: Resultado suma ->", calculadora_segura(5, 3, "+"))
print("✅ Ejercicio 10: Resultado división por cero ->", calculadora_segura(5, 0, "/"))
print("✅ Ejercicio 10: Operación inválida ->", calculadora_segura(5, 2, "%"))
