# ----------------------------------------
# CLASE 5: CONDICIONALES EN PYTHON
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

edad = 18

if edad >= 18:
    print("Sos mayor de edad.")

# El bloque debajo del if se ejecuta solo si la condición es True


# ----------------------------------------
# ✅ if - else

numero = int(input("Ingresá un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")


# ----------------------------------------
# ✅ if - elif - else

nota = int(input("Ingresá tu nota (0 a 10): "))

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Muy bien")
elif nota >= 4:
    print("Aprobado")
else:
    print("Desaprobado")


# ----------------------------------------
# 🔁 COMBINANDO CON OPERADORES LÓGICOS

edad = int(input("¿Qué edad tenés? "))

if edad >= 18 and edad <= 65:
    print("Sos adulto.")
elif edad < 18:
    print("Sos menor de edad.")
else:
    print("Sos mayor de 65 años.")


# ----------------------------------------
# ⚠️ IMPORTANTE: identación

# Python usa espacios (indentación) para definir bloques.
# Todo el código dentro del if debe estar indentado (generalmente 4 espacios o 1 tab)


# ----------------------------------------
# 🧠 CONDICIONES SIMPLIFICADAS (one-liners)

# Solo si la acción es muy simple:
x = 5
if x > 0: print("Es positivo")

# Operador ternario (una forma corta de if-else):
es_par = "Sí" if x % 2 == 0 else "No"
print("¿Es par?", es_par)

# También puede usarse para asignar valores en una sola línea según condiciones.
# Ejemplo:
temperatura = 30
estado = "Calor" if temperatura > 25 else "Templado"
print("Clima:", estado)


# ----------------------------------------
# 🧩 ESTRUCTURA MATCH - CASE (Python 3.10+)

# match case permite comparar una variable con múltiples valores posibles, de forma más ordenada que varios elif.

# Ejemplo:
comando = input("Ingresá un comando: ").lower()

match comando:
    case "saludar":
        print("¡Hola!")
    case "despedir":
        print("¡Chau!")
    case "ayuda":
        print("Comandos disponibles: saludar, despedir, ayuda.")
    case _:
        print("Comando no reconocido.")

# El guion bajo (_) es el caso por defecto, como el 'else'.


# ----------------------------------------
# 🧪 MINI PROYECTO DE PRÁCTICA

# Pedir al usuario:
# - su edad
# - si tiene entrada (sí/no)
# Y decir si puede entrar a un evento (mayor de 18 y con entrada)

# Descomentalo para probarlo:

# edad = int(input("¿Qué edad tenés? "))
# tiene_entrada = input("¿Tenés entrada? (sí/no): ").lower()

# if edad >= 18 and tiene_entrada == "sí":
#     print("Podés entrar al evento.")
# else:
#     print("No podés entrar.")


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Estructura if, elif y else
# - Evaluación de condiciones
# - Uso de operadores lógicos con condicionales
# - El concepto de indentación
# - Cómo crear decisiones simples y múltiples
# - El operador ternario para expresiones en una línea
# - La estructura match-case para múltiples opciones (Python 3.10+)

# Próxima clase: bucles (while y for) para repetir acciones.
