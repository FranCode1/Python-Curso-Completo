# ----------------------------------------
# CLASE 5: CONDICIONALES EN PYTHON (con errores comunes)
# ----------------------------------------

# Las estructuras condicionales permiten ejecutar código solo si se cumple cierta condición.

# Sintaxis básica:

# if condición:
#     código si es verdadero
# elif otra_condición:
#     código si esa condición es verdadera
# else:
#     código si ninguna se cumple


# ----------------------------------------
# ✅ EJEMPLO BÁSICO CON if
# ----------------------------------------

edad = 18

if edad >= 18:
    print("Sos mayor de edad.")

# ✅ Salida esperada: Sos mayor de edad.

# ❌ ERROR COMÚN:
# if edad = 18:   # Usa "=" en lugar de "=="
#     print("Error")

# 🔧 SOLUCIÓN:
# "=" es asignación, "==" es comparación. 
# Para condiciones siempre se usa "==", ">=", "<=", etc.


# ----------------------------------------
# ✅ if - else
# ----------------------------------------

numero = 7

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# ✅ Salida esperada: El número es impar.

# ❌ ERROR COMÚN:
# if numero % 2 = 0:   # Usar "=" en lugar de "=="
# if numero % 2:       # Creer que esto devuelve True solo si es par
# else print("...")    # Olvidar los ":" o indentación

# 🔧 SOLUCIÓN:
# - Usar "==" para comparar.
# - Siempre cerrar la condición con ":".
# - Respetar la indentación (4 espacios).


# ----------------------------------------
# ✅ if - elif - else
# ----------------------------------------

nota = 8

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Muy bien")
elif nota >= 4:
    print("Aprobado")
else:
    print("Desaprobado")

# ✅ Salida esperada: Muy bien.

# ❌ ERROR COMÚN:
# Usar varios "if" en lugar de "elif":
# if nota >= 9:
#     print("Excelente")
# if nota >= 7:
#     print("Muy bien")   # Esto se ejecutaría también aunque el anterior ya cumplió

# 🔧 SOLUCIÓN:
# Usar "elif" para que solo una condición se cumpla.


# ----------------------------------------
# 🔁 COMBINANDO CON OPERADORES LÓGICOS
# ----------------------------------------

edad = 70

if edad >= 18 and edad <= 65:
    print("Sos adulto.")
elif edad < 18:
    print("Sos menor de edad.")
else:
    print("Sos mayor de 65 años.")

# ✅ Salida esperada: Sos mayor de 65 años.

# ❌ ERROR COMÚN:
# if edad >= 18 and <= 65:   # Sintaxis inválida
# 🔧 SOLUCIÓN:
# Repetir la variable en ambas comparaciones:
# if edad >= 18 and edad <= 65:


# ----------------------------------------
# ⚠️ IMPORTANTE: identación
# ----------------------------------------
# Python usa espacios (indentación) para definir bloques.
# Todo el código dentro del if debe estar indentado (generalmente 4 espacios o 1 tab).

# ❌ ERROR COMÚN:
# if edad > 18:
# print("Mayor de edad")   # Falta indentación -> IndentationError


# ----------------------------------------
# 🧠 CONDICIONES SIMPLIFICADAS (one-liners)
# ----------------------------------------

x = 5
if x > 0: print("Es positivo")

es_par = "Sí" if x % 2 == 0 else "No"
print("¿Es par?", es_par)

temperatura = 30
estado = "Calor" if temperatura > 25 else "Templado"
print("Clima:", estado)

# ✅ Salida esperada:
# Es positivo
# ¿Es par? No
# Clima: Calor

# ❌ ERROR COMÚN:
# es_par = "Sí" if x % 2 == 0  # Falta el "else"
# 🔧 SOLUCIÓN:
# Siempre incluir "else" en un operador ternario.


# ----------------------------------------
# 🧩 ESTRUCTURA MATCH - CASE (Python 3.10+)
# ----------------------------------------

comando = "ayuda"

match comando:
    case "saludar":
        print("¡Hola!")
    case "despedir":
        print("¡Chau!")
    case "ayuda":
        print("Comandos disponibles: saludar, despedir, ayuda.")
    case _:
        print("Comando no reconocido.")

# ✅ Salida esperada:
# Comandos disponibles: saludar, despedir, ayuda.

# ❌ ERROR COMÚN:
# Usar match en versiones < 3.10 → SyntaxError
# 🔧 SOLUCIÓN:
# Asegurarse de usar Python 3.10 o superior.


# ----------------------------------------
# 🧪 MINI PROYECTO DE PRÁCTICA
# ----------------------------------------

edad = 20
tiene_entrada = "sí"

if edad >= 18 and tiene_entrada == "sí":
    print("Podés entrar al evento.")
else:
    print("No podés entrar.")

# ✅ Salida esperada: Podés entrar al evento.

# ❌ ERROR COMÚN:
# if edad >= 18 and tiene_entrada = "sí":   # "=" en lugar de "=="
# if edad >= 18 and tiene_entrada == sí:    # Falta comillas en "sí"

# 🔧 SOLUCIÓN:
# - Usar "==" para comparar.
# - Las cadenas siempre deben ir entre comillas.


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - if, elif, else
# - Condiciones múltiples con and/or
# - El concepto de indentación
# - Uso del operador ternario
# - match-case en Python 3.10+
# - ❗ Y los errores más comunes:
#   • Confundir "=" con "=="
#   • Olvidar los ":" en la condición
#   • Problemas de indentación
#   • Usar varios if en lugar de elif
#   • Usar match en versiones viejas de Python

# Próxima clase: bucles (while y for).
