# ============================================================
# MÓDULO 3 - print(), input() y escape sequences
# PARTE 1: ERRORES COMUNES
# ============================================================

# En esta sección repasamos los errores más frecuentes
# al usar print(), input() y las secuencias de escape.

# ------------------------------------------------------------
# ❌ ERROR 1: Olvidar paréntesis en print()
# ------------------------------------------------------------
# print "Hola"    # ❌ SyntaxError en Python 3
# ✅ En Python 3 siempre se usan paréntesis
print("✅ Hola")


# ------------------------------------------------------------
# ❌ ERROR 2: Confundir coma con +
# ------------------------------------------------------------
nombre = "Franco"
edad = 22
# print("Me llamo " + nombre, "y tengo " + edad + " años")
# ❌ TypeError: solo se puede concatenar str con str
# ✅ Usar coma o convertir edad a str
print("✅ Forma con coma:", "Me llamo", nombre, "y tengo", edad, "años")
print("✅ Forma con str():", "Me llamo " + nombre + " y tengo " + str(edad) + " años")
print(f"✅ Forma moderna: Me llamo {nombre} y tengo {edad} años")


# ------------------------------------------------------------
# ❌ ERROR 3: Usar mal el argumento sep=
# ------------------------------------------------------------
# print("A", "B", sep = - )   # ❌ SyntaxError
# ✅ El separador debe ser un string
print("✅ Con sep=' - ':", "A", "B", sep=" - ")


# ------------------------------------------------------------
# ❌ ERROR 4: Usar mal el argumento end=
# ------------------------------------------------------------
# print("Hola", end=5)   # ❌ TypeError: end debe ser un string
# ✅ end debe recibir texto
print("✅ end con puntos:", "Hola", end="...")
print(" Mundo\n")


# ------------------------------------------------------------
# ❌ ERROR 5: Olvidar las barras invertidas en rutas de Windows
# ------------------------------------------------------------
# print("C:\nueva\carpeta")   # ❌ "\n" se interpreta como salto de línea
# ✅ Usar doble barra o prefijo r
print("✅ Ruta correcta:", "C:\\nueva\\carpeta")
print(r"✅ Otra forma (raw string): C:\nueva\carpeta")


# ------------------------------------------------------------
# ❌ ERROR 6: Mal uso de comillas en escape sequences
# ------------------------------------------------------------
# print("Dijo: "Hola" y se fue")   # ❌ SyntaxError
# ✅ Escapar comillas o usar comillas simples
print("✅ Dijo: \"Hola\" y se fue")
print('✅ Dijo: "Hola" y se fue')


# ------------------------------------------------------------
# ❌ ERROR 7: Olvidar que input devuelve string
# ------------------------------------------------------------
# edad = input("¿Cuántos años tenés? ")
# print(edad + 5)   # ❌ TypeError: str + int
# ✅ Convertir a número
edad = 22
print("✅ Edad + 5 =", edad + 5)


# ------------------------------------------------------------
# ❌ ERROR 8: Dejar inputs comentados al probar
# ------------------------------------------------------------
# nombre = input("¿Cómo te llamás? ")
# print("Hola,", nombre)
# ⚠️ Si está comentado, nunca se ejecuta y parece "que no funciona"
# ✅ Descomentar para que funcione
print("✅ Recordá descomentar los inputs cuando quieras probarlos")


# ------------------------------------------------------------
# ❌ ERROR 9: Paréntesis mal cerrados en print()
# ------------------------------------------------------------
# print("Hola"   # ❌ SyntaxError: falta cerrar paréntesis
# ✅ Revisar siempre que se cierren
print("✅ Paréntesis cerrados correctamente")


# ------------------------------------------------------------
# ❌ ERROR 10: Usar variables sin definir en input
# ------------------------------------------------------------
# print("Hola", usuario)   # ❌ NameError: usuario no definido
# ✅ Primero pedimos el dato
usuario = "Ejemplo"
print("✅ Hola", usuario)
