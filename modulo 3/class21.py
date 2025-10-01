# ----------------------------------------
# CLASE 21: MANEJO DE EXCEPCIONES EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es una excepción?
# Un error que ocurre durante la ejecución del programa y detiene el flujo normal del código.

# Ejemplos comunes:
# - ZeroDivisionError
# - FileNotFoundError
# - TypeError
# - ValueError

# Se pueden manejar con bloques try-except


# ==========================
# 🔹 SINTAXIS BÁSICA
# ==========================

try:
    numero = int(input("Ingresá un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("❌ No se puede dividir por cero.")
except ValueError:
    print("❌ Tenés que ingresar un número válido.")
    

# ==========================
# 🔹 else y finally
# ==========================

try:
    archivo = open("archivo.txt")
except FileNotFoundError:
    print("❌ El archivo no existe.")
else:
    print("✅ Archivo abierto correctamente.")
    archivo.close()
finally:
    print("🔁 Bloque finally siempre se ejecuta (para cerrar conexiones, liberar recursos, etc).")


# ==========================
# 🔹 CAPTURAR EL ERROR COMO OBJETO
# ==========================

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("Detalles del error:", e)


# ==========================
# 🔹 EXCEPCIONES PERSONALIZADAS
# ==========================

# Podés definir tus propios errores heredando de Exception

class EdadInvalidaError(Exception):
    """Excepción para edades menores a 0."""
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa.")

try:
    validar_edad(-5)
except EdadInvalidaError as e:
    print("❌ Error personalizado:", e)


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Crear una calculadora segura que no se rompa con entradas inválidas

# def calculadora_segura():
#     try:
#         a = float(input("Número 1: "))
#         b = float(input("Número 2: "))
#         operacion = input("Operación (+, -, *, /): ")
        
#         if operacion == "+":
#             print("Resultado:", a + b)
#         elif operacion == "-":
#             print("Resultado:", a - b)
#         elif operacion == "*":
#             print("Resultado:", a * b)
#         elif operacion == "/":
#             print("Resultado:", a / b)
#         else:
#             print("❌ Operación no válida.")
#     except ValueError:
#         print("❌ Entrada inválida: ingresá números.")
#     except ZeroDivisionError:
#         print("❌ No se puede dividir por cero.")

# calculadora_segura()


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es una excepción y por qué ocurren
# - Cómo usar try-except-else-finally para controlarlas
# - Cómo capturar errores específicos y obtener sus mensajes
# - Cómo crear tus propias excepciones
# - Cómo proteger tu programa contra fallos inesperados

# Próxima clase: Pruebas con pytest – cómo testear tu código de forma profesional.
