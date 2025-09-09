# ----------------------------------------
# CLASE 24: EXPRESIONES REGULARES EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es una expresión regular (regex)?
# Una secuencia de caracteres que define un patrón de búsqueda sobre texto.

# Python incluye el módulo `re` para trabajar con regex.

import re


# ==========================
# 🔹 BÚSQUEDA SIMPLE CON re.search()
# ==========================

texto = "Mi número es 1123-456-789 y mi mail es franco@mail.com"

# Buscar si hay un número
resultado = re.search(r"\d{4}", texto)
print(resultado.group())  # 1123


# ==========================
# 🔹 COINCIDENCIAS CON re.findall()
# ==========================

# Encuentra todos los mails en el texto
mails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", texto)
print(mails)  # ['franco@mail.com']


# ==========================
# 🔹 COINCIDENCIAS AL INICIO CON re.match()
# ==========================

# Solo verifica si el inicio del texto coincide
print(re.match(r"Mi número", texto))  # Coincide
print(re.match(r"número", texto))     # No coincide


# ==========================
# 🔹 SUSTITUIR TEXTO CON re.sub()
# ==========================

nuevo_texto = re.sub(r"\d", "*", texto)
print(nuevo_texto)  # Reemplaza todos los números por "*"


# ==========================
# 🔹 GRUPOS Y CAPTURAS
# ==========================

texto_fecha = "La fecha es 24/06/2025"

# Extraer día, mes y año
match = re.search(r"(\d{2})/(\d{2})/(\d{4})", texto_fecha)
if match:
    dia, mes, anio = match.groups()
    print(f"Día: {dia}, Mes: {mes}, Año: {anio}")


# ==========================
# 🔹 PATRONES MÁS COMUNES
# ==========================

# \d → cualquier dígito (0-9)
# \w → carácter alfanumérico (letra, número o _)
# \s → espacio en blanco
# .  → cualquier carácter (excepto salto de línea)
# +  → una o más repeticiones
# *  → cero o más repeticiones
# ?  → cero o una repetición
# {n} → exactamente n veces
# ^  → inicio de línea
# $  → fin de línea
# [abc] → a, b o c
# [^abc] → cualquier cosa menos a, b o c


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Validar una contraseña segura:
# Debe tener al menos:
# - 8 caracteres
# - una mayúscula
# - una minúscula
# - un número

def validar_password(password):
    patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    return re.match(patron, password) is not None

# Pruebas
print(validar_password("Abc12345"))  # True
print(validar_password("abc123"))    # False


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es una expresión regular y cómo usar el módulo re
# - Cómo buscar, encontrar y reemplazar texto
# - Cómo capturar grupos específicos del texto
# - Cómo validar formatos como mails, fechas y contraseñas

# Próxima clase: Programación funcional en Python – map, filter, reduce y más.
