# ----------------------------------------
# CLASE 34: DECORADORES AVANZADOS
# ----------------------------------------

from functools import wraps
import time

# ============================================================
# EJERCICIO 1: Decorador básico de logging
# ============================================================
# Consigna:
# Crea un decorador que muestre un mensaje antes y después de ejecutar la función.

def log(func):
    def wrapper(*args, **kwargs):
        print(f"➡ Ejecutando {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"⬅ Terminó {func.__name__}")
        return resultado
    return wrapper

@log
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Franco")


# ============================================================
# EJERCICIO 2: Decorador para medir tiempo
# ============================================================
# Consigna:
# Implementa un decorador que mida cuánto tarda en ejecutarse una función.

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱ {func.__name__} tardó {fin - inicio:.5f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def calcular():
    return sum([i**2 for i in range(1000000)])

print(calcular())


# ============================================================
# EJERCICIO 3: Decoradores anidados
# ============================================================
# Consigna:
# Usa dos decoradores que conviertan el texto a mayúsculas y agreguen signos de exclamación.

def mayusculas(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def exclamacion(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!!!"
    return wrapper

@exclamacion
@mayusculas
def mensaje():
    return "python decorators"

print(mensaje())


# ============================================================
# EJERCICIO 4: Decorador con argumentos
# ============================================================
# Consigna:
# Crea un decorador que repita la ejecución de la función N veces.

def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def hola():
    print("Hola!")

hola()


# ============================================================
# EJERCICIO 5: Preservar metadata con functools.wraps
# ============================================================
# Consigna:
# Usa wraps para que el decorador no pierda el __name__ ni __doc__ de la función original.

def decorador_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Ejecutando función decorada...")
        return func(*args, **kwargs)
    return wrapper

@decorador_info
def sumar(a, b):
    """Suma dos números"""
    return a + b

print(sumar(2, 5))
print(sumar.__name__)
print(sumar.__doc__)


# ============================================================
# EJERCICIO 6: Decorar métodos de clase
# ============================================================
# Consigna:
# Haz un decorador que muestre los argumentos al llamar a un método de una clase.

def log_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Llamando {func.__name__} con {args[1:]} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

class Calculadora:
    @log_args
    def multiplicar(self, a, b):
        return a * b

calc = Calculadora()
print(calc.multiplicar(4, 6))


# ============================================================
# EJERCICIO 7: Decorador para cache (memoización simple)
# ============================================================
# Consigna:
# Implementa un decorador que guarde resultados de funciones costosas para no recalcularlos.

def cache(func):
    resultados = {}
    @wraps(func)
    def wrapper(*args):
        if args in resultados:
            print("⚡ Usando valor en caché")
            return resultados[args]
        print("🔄 Calculando...")
        res = func(*args)
        resultados[args] = res
        return res
    return wrapper

@cache
def potencia(base, exp):
    return base ** exp

print(potencia(2, 10))
print(potencia(2, 10))


# ============================================================
# EJERCICIO 8: Decorador para validar argumentos
# ============================================================
# Consigna:
# Haz un decorador que valide que todos los argumentos de una función sean positivos.

def validar_positivos(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if any(a < 0 for a in args if isinstance(a, (int, float))):
            raise ValueError("⚠️ Todos los argumentos deben ser positivos")
        return func(*args, **kwargs)
    return wrapper

@validar_positivos
def dividir(a, b):
    return a / b

print(dividir(10, 2))
# print(dividir(-5, 3))  # Probar error


# ============================================================
# EJERCICIO 9: Decorador que cuenta llamadas
# ============================================================
# Consigna:
# Crea un decorador que cuente cuántas veces fue llamada una función.

def contar_llamadas(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.contador += 1
        print(f"📞 {func.__name__} llamada #{wrapper.contador}")
        return func(*args, **kwargs)
    wrapper.contador = 0
    return wrapper

@contar_llamadas
def saludo(nombre):
    print(f"Hola {nombre}")

saludo("Ana")
saludo("Luis")


# ============================================================
# EJERCICIO 10: Decorador para funciones asincrónicas
# ============================================================
# Consigna:
# Haz un decorador que mida el tiempo de ejecución de una función async.

def medir_async(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = await func(*args, **kwargs)
        fin = time.time()
        print(f"⏱ Async {func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

import asyncio

@medir_async
async def tarea():
    await asyncio.sleep(1)
    return "Tarea completada"

async def main():
    print(await tarea())

asyncio.run(main())
