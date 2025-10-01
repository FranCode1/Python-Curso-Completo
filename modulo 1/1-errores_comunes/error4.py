# ============================================================
# MÓDULO 4 - OPERADORES EN PYTHON
# PARTE 1: ERRORES COMUNES
# ============================================================

# En esta sección repasamos los errores más frecuentes
# al usar operadores en Python.

# ------------------------------------------------------------
# ❌ ERROR 1: Confundir división normal con división entera
# ------------------------------------------------------------
a = 10
b = 3
print("✅ División normal:", a / b)   # 3.333...
print("✅ División entera:", a // b) # 3
# ⚠️ Error común: pensar que "/" ya devuelve un entero


# ------------------------------------------------------------
# ❌ ERROR 2: Usar operador de asignación en lugar de comparación
# ------------------------------------------------------------
x = 5
y = 5
# if x = y:    # ❌ SyntaxError (en Python no se puede usar "=" en condicionales)
# ✅ Usar "=="
if x == y:
    print("✅ x es igual a y")


# ------------------------------------------------------------
# ❌ ERROR 3: Confundir "==" con "is"
# ------------------------------------------------------------
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
# if lista1 is lista2:    # ❌ False → no son el mismo objeto
# ✅ Usar "=="
if lista1 == lista2:
    print("✅ lista1 y lista2 tienen el mismo contenido")


# ------------------------------------------------------------
# ❌ ERROR 4: Mezclar tipos incompatibles en comparación
# ------------------------------------------------------------
# print(5 < "10")    # ❌ TypeError: no se puede comparar int con str
# ✅ Convertir al mismo tipo
print("✅ Comparación correcta:", 5 < int("10"))


# ------------------------------------------------------------
# ❌ ERROR 5: Usar mal los operadores lógicos
# ------------------------------------------------------------
x = 7
# if x > 5 and 10:    # ❌ Esto siempre da True porque 10 es un valor "truthy"
# ✅ Comparar correctamente
if x > 5 and x < 10:
    print("✅ x está entre 5 y 10")


# ------------------------------------------------------------
# ❌ ERROR 6: Pensar que "not" se escribe como "!" (como en otros lenguajes)
# ------------------------------------------------------------
# if !(x == 7):    # ❌ SyntaxError
# ✅ En Python se usa "not"
if not (x == 7):
    print("Esto no se ejecuta porque x == 7")


# ------------------------------------------------------------
# ❌ ERROR 7: Usar "in" en tipos no iterables
# ------------------------------------------------------------
# if 3 in 100:    # ❌ TypeError: int no es iterable
# ✅ Usar "in" en listas, strings, tuplas, etc.
if 3 in [1, 2, 3, 4]:
    print("✅ 3 está en la lista")


# ------------------------------------------------------------
# ❌ ERROR 8: Confundir módulo con división
# ------------------------------------------------------------
num = 10
# if num / 2 == 0:    # ❌ Da 5.0, nunca es 0
# ✅ Usar el operador módulo %
if num % 2 == 0:
    print("✅ num es par")


# ------------------------------------------------------------
# ❌ ERROR 9: Olvidar paréntesis al combinar condiciones
# ------------------------------------------------------------
edad = 20
# if edad > 18 and < 30:    # ❌ SyntaxError
# ✅ Escribir la condición completa
if edad > 18 and edad < 30:
    print("✅ edad está entre 18 y 30")


# ------------------------------------------------------------
# ❌ ERROR 10: Confundir operadores bit a bit (&, |) con lógicos (and, or)
# ------------------------------------------------------------
a = True
b = False
# if a & b:    # ⚠️ Esto funciona pero no es lo que se espera (bitwise)
# ✅ Usar operadores lógicos
if a and b:
    print("Esto no se imprime porque b es False")
else:
    print("✅ Usar 'and' y 'or' en condiciones lógicas")
