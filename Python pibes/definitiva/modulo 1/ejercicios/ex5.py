# ----------------------------------------
# PRÁCTICA - CLASE 5: CONDICIONALES EN PYTHON
# Autor: Franco Lugo
# ----------------------------------------

# ✅ Ejercicio 1: Mayor o menor de edad
# Consigna: Dado una edad, mostrar si la persona es mayor o menor de edad.
edad = 17
if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 2: Verificar número par o impar
# Consigna: Usar un número y mostrar si es par o impar.
numero = 12
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 3: Calificar una nota
# Consigna: Dada una nota (0 a 10), mostrar: Excelente (9-10), Muy bien (7-8), Aprobado (4-6), Desaprobado (0-3)
nota = 6
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Muy bien")
elif nota >= 4:
    print("Aprobado")
else:
    print("Desaprobado")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 4: Clasificación de edad
# Consigna: Mostrar si alguien es menor, adulto (18-65), o mayor de 65.
edad = 70
if edad < 18:
    print("Sos menor de edad.")
elif edad <= 65:
    print("Sos adulto.")
else:
    print("Sos mayor de 65 años.")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 5: Condición simplificada
# Consigna: Mostrar si un número es positivo usando una línea de código.
x = 3
if x > 0: print("Es positivo")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 6: Operador ternario
# Consigna: Usar operador ternario para verificar si un número es par.
n = 9
es_par = "Sí" if n % 2 == 0 else "No"
print("¿Es par?", es_par)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 7: Acceso a evento
# Consigna: Verificar si una persona puede entrar a un evento (edad ≥ 18 y tiene entrada).
edad = 20
tiene_entrada = "sí"
if edad >= 18 and tiene_entrada.lower() == "sí":
    print("Podés entrar al evento.")
else:
    print("No podés entrar.")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 8: Contraseña correcta
# Consigna: Verificar si la contraseña ingresada es correcta.
contraseña = "secreto123"
if contraseña == "secreto123":
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 9: Mayor de tres números
# Consigna: Comparar tres números y mostrar cuál es el mayor.
a = 8
b = 15
c = 12
if a >= b and a >= c:
    print("El mayor es:", a)
elif b >= c:
    print("El mayor es:", b)
else:
    print("El mayor es:", c)

print("\n" + "-"*50 + "\n")

# ✅ Ejercicio 10: Evaluar temperatura
# Consigna: Dada una temperatura, decir si está fría (≤10), templada (11-25) o caliente (>25).
temperatura = 27
if temperatura <= 10:
    print("Está frío.")
elif temperatura <= 25:
    print("Está templado.")
else:
    print("Hace calor.")

# ----------------------------------------
# Fin del archivo
# ----------------------------------------
