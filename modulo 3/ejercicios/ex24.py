# ----------------------------------------
# CLASE 24: EXPRESIONES REGULARES EN PYTHON
# ----------------------------------------

import re

# =====================================================
# 1) Buscar todas las direcciones de correo en un texto
# =====================================================
texto1 = "Contactame en franco@mail.com o en info@empresa.org"
correos = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", texto1)
print("Ejercicio 1:", correos)  # ['franco@mail.com', 'info@empresa.org']


# =====================================================
# 2) Validar si un número de teléfono tiene formato XXX-XXX-XXXX
# =====================================================
def validar_telefono(numero):
    return re.match(r"^\d{3}-\d{3}-\d{4}$", numero) is not None

print("Ejercicio 2:", validar_telefono("123-456-7890"))  # True
print("Ejercicio 2:", validar_telefono("1234567890"))    # False


# =====================================================
# 3) Extraer solo los números de un texto
# =====================================================
texto2 = "El producto cuesta 1200 pesos y el envío 300"
numeros = re.findall(r"\d+", texto2)
print("Ejercicio 3:", numeros)  # ['1200', '300']


# =====================================================
# 4) Reemplazar múltiples espacios por uno solo
# =====================================================
texto3 = "Hola     mundo   con   espacios"
normalizado = re.sub(r"\s+", " ", texto3)
print("Ejercicio 4:", normalizado)  # "Hola mundo con espacios"


# =====================================================
# 5) Verificar si una cadena es un código postal argentino (4 dígitos)
# =====================================================
def validar_cp(cp):
    return re.match(r"^\d{4}$", cp) is not None

print("Ejercicio 5:", validar_cp("5000"))  # True
print("Ejercicio 5:", validar_cp("AB12"))  # False


# =====================================================
# 6) Capturar usuario y dominio de un correo
# =====================================================
correo = "usuario123@dominio.com"
match = re.match(r"([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", correo)
if match:
    usuario, dominio = match.groups()
    print("Ejercicio 6: Usuario:", usuario, "Dominio:", dominio)


# =====================================================
# 7) Validar si un texto es una fecha en formato DD/MM/AAAA
# =====================================================
def validar_fecha(fecha):
    return re.match(r"^\d{2}/\d{2}/\d{4}$", fecha) is not None

print("Ejercicio 7:", validar_fecha("24/06/2025"))  # True
print("Ejercicio 7:", validar_fecha("2025/06/24"))  # False


# =====================================================
# 8) Encontrar todas las palabras que empiezan con mayúscula
# =====================================================
texto4 = "Ayer Franco visitó Buenos Aires con Maria"
capitalizadas = re.findall(r"\b[A-Z][a-zA-Záéíóúñ]+\b", texto4)
print("Ejercicio 8:", capitalizadas)  # ['Ayer', 'Franco', 'Buenos', 'Aires', 'Maria']


# =====================================================
# 9) Validar si una contraseña es segura
# (mínimo 8 caracteres, una mayúscula, una minúscula, un número)
# =====================================================
def validar_password(password):
    patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    return re.match(patron, password) is not None

print("Ejercicio 9:", validar_password("Abc12345"))  # True
print("Ejercicio 9:", validar_password("abc123"))    # False


# =====================================================
# 10) Extraer hashtags de un texto
# =====================================================
texto5 = "Hoy aprendí #Python y #Regex en la clase #23"
hashtags = re.findall(r"#\w+", texto5)
print("Ejercicio 10:", hashtags)  # ['#Python', '#Regex', '#23']
