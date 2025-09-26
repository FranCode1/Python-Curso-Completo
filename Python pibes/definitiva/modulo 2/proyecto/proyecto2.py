import time

# ===============================
# Decorador para medir tiempos
# ===============================
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"⏱ Tiempo de ejecución: {fin - inicio:.5f} segundos")
        return resultado
    return wrapper


# ===============================
# Funciones y scope
# ===============================
STOPWORDS = {"el", "la", "los", "las", "y", "de", "a"}

def limpiar_texto(texto):
    """Convierte el texto a minúsculas y lo separa en palabras."""
    return texto.lower().replace(".", "").replace(",", "").split()


# ===============================
# Funciones avanzadas
# ===============================
def procesar_texto(texto):
    palabras = limpiar_texto(texto)

    # Usamos filter para quitar stopwords
    filtradas = list(filter(lambda w: w not in STOPWORDS, palabras))

    # Usamos map para calcular la longitud de cada palabra
    longitudes = list(map(len, filtradas))

    # Usamos enumerate para mostrar índices
    for i, palabra in enumerate(filtradas, start=1):
        print(f"{i}. {palabra} ({len(palabra)} letras)")

    # Usamos zip para emparejar palabra-longitud
    pares = list(zip(filtradas, longitudes))
    return pares


# ===============================
# Closures
# ===============================
def contador_palabra(palabra):
    """Devuelve una función que cuenta cuántas veces aparece `palabra` en un texto"""
    def contar(texto):
        palabras = limpiar_texto(texto)
        return palabras.count(palabra)
    return contar


# ===============================
# Recursividad
# ===============================
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ===============================
# Generadores
# ===============================
def lector_lineas(texto):
    """Simula leer un archivo línea por línea"""
    for linea in texto.split("\n"):
        yield linea


# ===============================
# Programa principal
# ===============================
@medir_tiempo
def main():
    texto = """Python es un lenguaje de programación.
    La programación con Python es divertida y poderosa.
    El lenguaje Python es muy usado en ciencia de datos y web."""

    print("\n--- Procesar texto ---")
    pares = procesar_texto(texto)
    print("\nPares palabra-longitud:", pares)

    print("\n--- Closure contador de palabra ---")
    contar_python = contador_palabra("python")
    print("La palabra 'python' aparece:", contar_python(texto), "veces")

    print("\n--- Factorial recursivo ---")
    print("Factorial de 5:", factorial(5))

    print("\n--- Generador de líneas ---")
    for linea in lector_lineas(texto):
        print(">>", linea.strip())


if __name__ == "__main__":
    main()
