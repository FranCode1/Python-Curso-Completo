# ----------------------------------------
# CLASE 13: CLOSURES Y FUNCIONES COMO OBJETOS
# ----------------------------------------

# En Python, las funciones son objetos.
# Eso significa que pueden:
# - Ser asignadas a variables
# - Pasarse como argumentos
# - Retornarse desde otras funciones
# - Tener propiedades propias


# ==========================
# 🔹 FUNCIONES COMO OBJETOS
# ==========================

def saludar():
    print("¡Hola!")

# Asignar a otra variable
otra = saludar
otra()  # ¡Hola!

# Pasar como parámetro
def ejecutar(funcion):
    print("Ejecutando función...")
    funcion()

ejecutar(saludar)


# ==========================
# 🔹 FUNCIONES DENTRO DE FUNCIONES
# ==========================

def operacion(mensaje):
    def imprimir():
        print(mensaje)
    imprimir()

operacion("Esto está dentro de otra función")


# ==========================
# 🔹 CLOSURES (Cierre)
# ==========================

# Un closure es una función que "recuerda" el entorno donde fue creada.

def crear_multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar  # devuelve la función

por_dos = crear_multiplicador(2)
por_tres = crear_multiplicador(3)

print(por_dos(5))   # 10
print(por_tres(5))  # 15

# ✔️ La función `multiplicar` recuerda el valor de `factor` aunque la función externa ya terminó


# ==========================
# 🔹 FUNCIONES CON ESTADO (sin usar clases)
# ==========================

def contador():
    cuenta = 0
    def aumentar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return aumentar

mi_contador = contador()

print(mi_contador())  # 1
print(mi_contador())  # 2
print(mi_contador())  # 3


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================

# Crear un generador de saludos personalizados

# def crear_saludo(saludo_inicial):
#     def saludar(nombre):
#         return f"{saludo_inicial}, {nombre}!"
#     return saludar

# saludar_en_espanol = crear_saludo("Hola")
# saludar_en_ingles = crear_saludo("Hi")

# print(saludar_en_espanol("Franco"))  # Hola, Franco!
# print(saludar_en_ingles("Max"))      # Hi, Max!


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Que las funciones en Python son objetos
# - Cómo pasar funciones como argumentos y retornarlas
# - Qué es un closure y cómo se comporta
# - Cómo usar funciones con estado (sin clases)
# - Aplicaciones prácticas para lógica dinámica y encapsulada

# Próxima clase: Decoradores – cómo extender funciones con closures.
