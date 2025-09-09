# =====================================================================
# EJERCICIO 44: Validación de contraseña segura
# ---------------------------------------------------------------------
# Escribí un programa que pida una contraseña y verifique que:
# •	Tenga al menos 8 caracteres.
# •	Contenga al menos una letra mayúscula.
# •	Contenga al menos un número.
# •	No contenga espacios.
# El programa debe repetirse hasta que el usuario ingrese una contraseña válida.
# =====================================================================

# ---------- Forma 1: clásico for + flags ----------
def validar_contraseña_1():
    while True:
        contraseña = input("Ingrese la contraseña: ")
        longitud_valida = len(contraseña) >= 8
        tiene_mayuscula = any(c.isupper() for c in contraseña)
        tiene_numero = any(c.isdigit() for c in contraseña)
        sin_espacios = " " not in contraseña

        if longitud_valida and tiene_mayuscula and tiene_numero and sin_espacios:
            print("✅ Contraseña aceptada.")
            break
        else:
            print("❌ Contraseña inválida. Intentá de nuevo.")

# ---------- Forma 2: usando funciones auxiliares ----------
def es_segura(contraseña):
    return (len(contraseña) >= 8 and
            any(c.isupper() for c in contraseña) and
            any(c.isdigit() for c in contraseña) and
            " " not in contraseña)

def validar_contraseña_2():
    while True:
        contraseña = input("Ingrese la contraseña: ")
        if es_segura(contraseña):
            print("✅ Contraseña aceptada.")
            break
        else:
            print("❌ Contraseña inválida. Intentá de nuevo.")

# ---------- Forma 3: usando expresiones regulares ----------
import re
def validar_contraseña_3():
    patron = re.compile(r'^(?=.*[A-Z])(?=.*\d)[^\s]{8,}$')
    while True:
        contraseña = input("Ingrese la contraseña: ")
        if patron.match(contraseña):
            print("✅ Contraseña aceptada.")
            break
        else:
            print("❌ Contraseña inválida. Intentá de nuevo.")

# ---------- Forma 4: mensajes detallados ----------
def validar_contraseña_4():
    while True:
        contraseña = input("Ingrese la contraseña: ")
        errores = []
        if len(contraseña) < 8:
            errores.append("Debe tener al menos 8 caracteres.")
        if not any(c.isupper() for c in contraseña):
            errores.append("Debe contener al menos una mayúscula.")
        if not any(c.isdigit() for c in contraseña):
            errores.append("Debe contener al menos un número.")
        if " " in contraseña:
            errores.append("No debe contener espacios.")
        if not errores:
            print("✅ Contraseña aceptada.")
            break
        else:
            print("❌ Contraseña inválida:")
            for e in errores:
                print("-", e)
            print("🔁 Intentá de nuevo.\n")

# ---------- Forma 5: con todas las validaciones en una función ----------
def validar_contraseña_final(contraseña):
    return (len(contraseña) >= 8 and
            any(c.isupper() for c in contraseña) and
            any(c.isdigit() for c in contraseña) and
            " " not in contraseña)

def validar_contraseña_5():
    while True:
        contraseña = input("Ingrese la contraseña: ")
        if validar_contraseña_final(contraseña):
            print("✅ Contraseña aceptada.")
            break
        else:
            print("❌ Contraseña inválida. Intentá de nuevo.")

# =====================================================
# Ejecución del programa
# =====================================================
if __name__ == "__main__":
    # Descomentar la forma que quieras probar
    # validar_contraseña_1()
    # validar_contraseña_2()
    # validar_contraseña_3()
    # validar_contraseña_4()
    validar_contraseña_5()
