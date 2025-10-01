# ----------------------------------------
# CLASE X: ERRORES COMUNES EN PYTHON
# ----------------------------------------

# 🎯 Objetivo:
# Reconocer los errores más frecuentes al comenzar con Python,
# entender por qué ocurren y cómo corregirlos.
# ----------------------------------------

# ----------------------------------------------------
# 1. ERROR DE SINTAXIS (SyntaxError)
# ----------------------------------------------------
# Ocurre cuando escribimos mal las reglas del lenguaje.

# ❌ Ejemplo incorrecto:
# print("Hola"

# ✅ Corrección:
print("Hola")   # Cerramos bien el paréntesis


# ----------------------------------------------------
# 2. ERROR DE NOMBRE (NameError)
# ----------------------------------------------------
# Pasa cuando usamos una variable que no existe.

# ❌ Ejemplo incorrecto:
# print(mensage)   # Variable no definida (error de ortografía)

# ✅ Corrección:
mensaje = "Hola, mundo"
print(mensaje)


# ----------------------------------------------------
# 3. ERROR DE TIPOS (TypeError)
# ----------------------------------------------------
# Sucede cuando intentamos mezclar tipos de datos incompatibles.

# ❌ Ejemplo incorrecto:
# numero = 5
# texto = "años"
# print(numero + texto)   # No se puede sumar int + str

# ✅ Corrección:
numero = 5
texto = "años"
print(str(numero) + " " + texto)  # Convertimos a string


# ----------------------------------------------------
# 4. ERROR DE INDENTACIÓN (IndentationError)
# ----------------------------------------------------
# Python usa indentación (espacios/tabulaciones) para definir bloques de código.

# ❌ Ejemplo incorrecto:
# def saludar():
# print("Hola")   # Falta la indentación dentro de la función

# ✅ Corrección:
def saludar():
    print("Hola")   # Indentamos con 4 espacios

saludar()


# ----------------------------------------------------
# 5. ERROR DE ÍNDICE (IndexError)
# ----------------------------------------------------
# Ocurre al acceder a un índice fuera de rango en listas o strings.

# ❌ Ejemplo incorrecto:
# numeros = [1, 2, 3]
# print(numeros[5])   # No existe índice 5

# ✅ Corrección:
numeros = [1, 2, 3]
print(numeros[2])   # Último índice válido


# ----------------------------------------------------
# 6. ERROR DE VALOR (ValueError)
# ----------------------------------------------------
# Aparece cuando le damos un valor inválido a una función.

# ❌ Ejemplo incorrecto:
# edad = int("veinte")   # No se puede convertir texto a número

# ✅ Corrección:
edad = int("20")
print("Edad:", edad)


# ----------------------------------------------------
# 7. ERROR DE ATRIBUTO (AttributeError)
# ----------------------------------------------------
# Ocurre cuando intentamos usar un método que no existe en un objeto.

# ❌ Ejemplo incorrecto:
# texto = "python"
# texto.append("3")   # append() es de listas, no de strings

# ✅ Corrección:
texto = "python"
print(texto.upper())   # upper() sí existe en strings


# ----------------------------------------------------
# 8. ERROR DE IMPORTACIÓN (ImportError / ModuleNotFoundError)
# ----------------------------------------------------
# Pasa cuando intentamos importar un módulo que no está instalado.

# ❌ Ejemplo incorrecto:
# import pepito

# ✅ Corrección:
import math
print("Raíz cuadrada de 16:", math.sqrt(16))


# ----------------------------------------------------
# 9. ERROR DE DIVISIÓN POR CERO (ZeroDivisionError)
# ----------------------------------------------------
# Ocurre al dividir entre 0.

# ❌ Ejemplo incorrecto:
# resultado = 10 / 0

# ✅ Corrección:
resultado = 10 / 2
print("Resultado:", resultado)


# ----------------------------------------------------
# 10. ERROR DE ENTRADA (InputError → en realidad ValueError)
# ----------------------------------------------------
# Cuando pedimos input y no validamos el tipo.

# ❌ Ejemplo incorrecto:
# numero = int(input("Ingresá un número: "))  # Si escribo "hola" → ValueError

# ✅ Corrección:
# try:
#     numero = int(input("Ingresá un número: "))
#     print("Número ingresado:", numero)
# except ValueError:
#     print("⚠ Debés ingresar un número válido")


# ----------------------------------------
# CONCLUSIÓN
# ----------------------------------------
# Los errores son parte natural del aprendizaje en Python.
# Lo importante es:
# - Leer bien el mensaje de error
# - Identificar la causa
# - Corregir el código según el tipo de error
# 
# En esta clase vimos:
# - SyntaxError
# - NameError
# - TypeError
# - IndentationError
# - IndexError
# - ValueError
# - AttributeError
# - ImportError
# - ZeroDivisionError
# - Errores con input()
