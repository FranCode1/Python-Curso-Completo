# ----------------------------------------
# CLASE 32: ITERADORES PERSONALIZADOS (__iter__, __next__)
# ----------------------------------------

# 📌 Recordatorio:
# - Un "iterable" es un objeto que se puede recorrer con un bucle (ej: listas, strings, diccionarios).
# - Un "iterador" es un objeto que produce elementos de uno en uno cuando se le llama con next().
# - Python usa los métodos especiales __iter__() y __next__() para crear iteradores personalizados.


# ==========================
# 🔹 ITERAR SOBRE UNA LISTA (ejemplo básico)
# ==========================

numeros = [1, 2, 3]
it = iter(numeros)  # crea un iterador a partir de la lista

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # Error: StopIteration (ya no quedan elementos)


# ==========================
# 🔹 CREAR UN ITERADOR PERSONALIZADO
# ==========================

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.actual = 0

    def __iter__(self):
        # Devuelve el propio objeto como iterador
        return self

    def __next__(self):
        if self.actual < self.limite:
            valor = self.actual
            self.actual += 1
            return valor
        else:
            # Cuando no hay más elementos → detener la iteración
            raise StopIteration

# Uso
contador = Contador(5)
for num in contador:
    print(num)  # 0, 1, 2, 3, 4


# ==========================
# 🔹 ITERADOR DE NÚMEROS PARES
# ==========================

class Pares:
    def __init__(self, maximo):
        self.maximo = maximo
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.maximo:
            actual = self.num
            self.num += 2
            return actual
        else:
            raise StopIteration

pares = Pares(10)
print(list(pares))  # [0, 2, 4, 6, 8, 10]


# ==========================
# 🔹 MINI PROYECTO PRÁCTICO
# ==========================

# 🎯 Crear un iterador que recorra una cadena y devuelva solo las vocales

class VowelIterator:
    def __init__(self, texto):
        self.texto = texto.lower()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.texto):
            char = self.texto[self.index]
            self.index += 1
            if char in "aeiou":
                return char
        raise StopIteration

mensaje = "Iteradores en Python"
vocales = VowelIterator(mensaje)
print(list(vocales))  # ['i', 'e', 'a', 'o', 'e', 'e', 'o']


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Diferencia entre iterables e iteradores
# - Uso básico de iter() y next()
# - Cómo implementar __iter__ y __next__ en clases personalizadas
# - Mini proyecto: iterador que extrae vocales de un texto

# Próxima clase: Concurrencia y multiprocessing en Python (threads, procesos, async vs multiprocessing)
