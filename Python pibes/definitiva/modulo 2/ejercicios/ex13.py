# ============================================
# PRÁCTICA 13 - FUNCIONES COMO OBJETOS Y CLOSURES
# Autor: Franco Lugo
# ============================================

# --------------------------------------------
# ✅ Ejercicio 1: Usar lambda para restar dos números
# Consigna: Crear una función que reciba otra función y la ejecute dos veces seguidas.
# --------------------------------------------

def ejecutar_dos_veces(funcion):
    funcion()
    funcion()

def decir_hola():
    print("¡Hola!")

ejecutar_dos_veces(decir_hola)


# --------------------------------------------
# ✅ Ejercicio 2:
# Consigna: Crear una función que retorne otra función que sume un número específico a su argumento.
# --------------------------------------------

def crear_sumador(valor):
    def sumar(n):
        return n + valor
    return sumar

sumar_cinco = crear_sumador(5)
print(sumar_cinco(10))  # 15


# --------------------------------------------
# ✅ Ejercicio 3:
# Consigna: Crear un contador con estado interno que cuente cuántas veces fue llamado.
# --------------------------------------------

def contador():
    cuenta = 0
    def aumentar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return aumentar

c = contador()
print(c())  # 1
print(c())  # 2
print(c())  # 3


# --------------------------------------------
# ✅ Ejercicio 4:
# Consigna: Crear una función que almacene varios saludos y devuelva el que corresponde al idioma.
# --------------------------------------------

def crear_saludo_personalizado():
    saludos = {
        'es': "Hola",
        'en': "Hello",
        'fr': "Bonjour"
    }
    def saludar(idioma, nombre):
        return f"{saludos.get(idioma, 'Hola')}, {nombre}!"
    return saludar

saludo = crear_saludo_personalizado()
print(saludo('fr', 'Jean'))  # Bonjour, Jean!


# --------------------------------------------
# ✅ Ejercicio 5:
# Consigna: Crear una función que devuelva otra función que verifique si un número es mayor a un límite.
# --------------------------------------------

def mayor_que(limite):
    def comparar(n):
        return n > limite
    return comparar

es_mayor_10 = mayor_que(10)
print(es_mayor_10(12))  # True
print(es_mayor_10(5))   # False


# --------------------------------------------
# ✅ Ejercicio 6:
# Consigna: Crear una función que reciba una lista de funciones y las ejecute en orden.
# --------------------------------------------

def ejecutar_lista(funciones):
    for f in funciones:
        f()

def uno(): print("Uno")
def dos(): print("Dos")
def tres(): print("Tres")

ejecutar_lista([uno, dos, tres])


# --------------------------------------------
# ✅ Ejercicio 7:
# Consigna: Crear un sistema de login básico usando closure que recuerde el usuario permitido.
# --------------------------------------------

def crear_login(usuario_correcto):
    def login(usuario_intento):
        return usuario_intento == usuario_correcto
    return login

login_franco = crear_login("franco.luggo")
print(login_franco("admin"))       # False
print(login_franco("franco.luggo"))# True


# --------------------------------------------
# ✅ Ejercicio 8:
# Consigna: Crear una función que retorne un multiplicador y que almacene el total de multiplicaciones hechas.
# --------------------------------------------

def multiplicador_con_contador(factor):
    contador = 0
    def multiplicar(n):
        nonlocal contador
        contador += 1
        print(f"Multiplicaciones hechas: {contador}")
        return n * factor
    return multiplicar

multi = multiplicador_con_contador(4)
print(multi(2))  # 8
print(multi(3))  # 12


# --------------------------------------------
# ✅ Ejercicio 9:
# Consigna: Crear una función que genere funciones con mensajes personalizados y los imprima cuando se llame.
# --------------------------------------------

def crear_mensaje(msg):
    def mostrar():
        print(f"Mensaje: {msg}")
    return mostrar

m1 = crear_mensaje("Bienvenido")
m2 = crear_mensaje("Error de acceso")

m1()  # Mensaje: Bienvenido
m2()  # Mensaje: Error de acceso


# --------------------------------------------
# ✅ Ejercicio 10:
# Consigna: Crear un sistema que almacene tareas pendientes, y que devuelva una función para agregarlas y mostrarlas.
# --------------------------------------------

def crear_lista_tareas():
    tareas = []
    def agregar_tarea(tarea=None):
        if tarea:
            tareas.append(tarea)
        return tareas
    return agregar_tarea

mis_tareas = crear_lista_tareas()
print(mis_tareas("Estudiar closures"))
print(mis_tareas("Leer documentación"))
print(mis_tareas())  # ['Estudiar closures', 'Leer documentación']

# ============================================
# Fin del archivo
# ============================================