# ============================================================
# MÓDULO 2 - VARIABLES Y TIPOS DE DATOS
# PARTE 1: ERRORES COMUNES
# ============================================================

# En esta sección vamos a repasar los errores más comunes
# que cometen los principiantes al trabajar con variables
# y tipos de datos en Python, junto con sus soluciones.

# ------------------------------------------------------------
# ❌ ERROR 1: Usar una variable sin definirla
# ------------------------------------------------------------
# print(nombre)   # Da error: NameError: name 'nombre' is not defined
# ✅ Solución: siempre asegurate de definir primero la variable

nombre = "Franco"
print("✅ Nombre definido:", nombre)


# ------------------------------------------------------------
# ❌ ERROR 2: Confundir el tipo de dato al concatenar
# ------------------------------------------------------------
edad = 22
# print("Tengo " + edad + " años")   # TypeError: can only concatenate str (not "int") to str
# ✅ Solución: convertir a string o usar f-strings
print("✅ Forma correcta:", "Tengo " + str(edad) + " años")
print(f"✅ Forma moderna: Tengo {edad} años")


# ------------------------------------------------------------
# ❌ ERROR 3: Usar nombres inválidos para variables
# ------------------------------------------------------------
# 2cosas = "manzanas"    # ❌ SyntaxError
# mi-edad = 22           # ❌ SyntaxError
# class = "dato"         # ❌ SyntaxError (palabra reservada)

# ✅ Solución: usar nombres válidos y descriptivos
cosas2 = "manzanas"
mi_edad = 22
mi_clase = "dato"
print("✅ Nombres válidos:", cosas2, mi_edad, mi_clase)


# ------------------------------------------------------------
# ❌ ERROR 4: Olvidar comillas en strings
# ------------------------------------------------------------
# saludo = Hola
# print(saludo)          # ❌ NameError

# ✅ Solución: poner comillas
saludo = "Hola"
print("✅ String correcto:", saludo)


# ------------------------------------------------------------
# ❌ ERROR 5: Convertir tipos incorrectamente
# ------------------------------------------------------------
# numero = int("hola")   # ❌ ValueError: invalid literal for int()
# ✅ Solución: asegurate de que el contenido sea numérico

numero = int("45")
print("✅ Conversión correcta:", numero)


# ------------------------------------------------------------
# ❌ ERROR 6: Confundir True/False con strings
# ------------------------------------------------------------
activo = True
# if activo == "True":   # ❌ Comparando booleano con string
#     print("Activo!") 

# ✅ Solución: comparar con el booleano real
if activo:
    print("✅ Activo correctamente detectado")


# ------------------------------------------------------------
# ❌ ERROR 7: Reasignar variable sin darse cuenta
# ------------------------------------------------------------
pi = 3.14159
print("Valor inicial de pi:", pi)

pi = "numero mágico"
print("Valor reasignado de pi:", pi, "tipo:", type(pi))
# ⚠️ Esto no da error, pero puede confundir mucho

# ✅ Recomendación: usar nombres distintos para cosas diferentes
pi_real = 3.14159
pi_texto = "numero mágico"


# ------------------------------------------------------------
# ❌ ERROR 8: Confundir mayúsculas y minúsculas
# ------------------------------------------------------------
Nombre = "Ana"
# print(nombre)   # ❌ NameError: name 'nombre' is not defined
# ✅ Solución: respetar las mayúsculas

print("✅ Variable con mayúscula:", Nombre)


# ------------------------------------------------------------
# ❌ ERROR 9: Espacios indebidos en nombres
# ------------------------------------------------------------
# mi edad = 25   # ❌ SyntaxError
# ✅ Solución: usar guion bajo
mi_edad = 25
print("✅ Variable con guion bajo:", mi_edad)


# ------------------------------------------------------------
# ❌ ERROR 10: Uso incorrecto de f-strings
# ------------------------------------------------------------
# nombre = "Luis"
# print(f"Hola, {nombre")   # ❌ SyntaxError por llaves mal cerradas

# ✅ Solución:
nombre = "Luis"
print(f"✅ Hola, {nombre}")
