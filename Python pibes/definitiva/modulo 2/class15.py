# ----------------------------------------
# CLASE 15: GENERADORES EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es un generador?

# Un generador es una función especial que en lugar de `return`, usa `yield`.
# No devuelve el resultado de una sola vez, sino que "produce" valores uno por uno.

# Esto permite trabajar con grandes cantidades de datos sin cargarlos todos en memoria.


# ==========================
# 🔹 FUNCIÓN NORMAL VS GENERADOR
# ==========================

# Función normal:
def cuadrados_lista(n):
    lista = []
    for i in range(n):
        lista.append(i**2)
    return lista

print(cuadrados_lista(5))  # [0, 1, 4, 9, 16]


# Generador:
def cuadrados_generador(n):
    for i in range(n):
        yield i**2  # pausa y devuelve un valor por vez

# El generador no devuelve una lista directamente
gen = cuadrados_generador(5)
print(gen)  # <generator object...>

# Obtener los valores uno por uno
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9
print(next(gen))  # 16

# print(next(gen))  # StopIteration (porque ya no hay más valores)


# ==========================
# 🔹 USO EN BUCLES
# ==========================

# En la práctica, se usa con for-in:
for valor in cuadrados_generador(5):
    print("Valor generado:", valor)


# ==========================
# 🔹 GENERADOR INFINITO
# ==========================

def contador_infinito():
    n = 0
    while True:
        yield n
        n += 1

# gen_inf = contador_infinito()
# for i in range(10):
#     print(next(gen_inf))  # Va generando 0, 1, 2, ...


# ==========================
# 🔹 VENTAJAS DE LOS GENERADORES
# ==========================

# ✅ No ocupan memoria con toda la lista en RAM
# ✅ Se usan en procesamiento de datos, archivos, streams
# ✅ Se integran fácilmente con otras funciones como map, filter, etc.


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# Crear un generador de palabras letra por letra

# def deletrear(palabra):
#     for letra in palabra:
#         yield letra

# palabra = deletrear("Python")

# for letra in palabra:
#     print(letra)


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es un generador y para qué sirve
# - Cómo usar `yield` y `next()` para producir valores uno por uno
# - Cómo recorrer generadores con `for`
# - Las ventajas de usar generadores vs listas comunes
# - Cómo construir generadores útiles y eficientes

# Próxima clase: Módulos – organización, imports, reutilización de código.
