# ----------------------------------------
# CLASE 32: ITERADORES PERSONALIZADOS (__iter__, __next__)
# ----------------------------------------

# 📌 Recordatorio rápido:
# - Un "iterable" es un objeto que se puede recorrer con un bucle (ej: listas, strings, diccionarios).
# - Un "iterador" es un objeto que produce elementos de uno en uno cuando se le llama con next().
# - Python usa los métodos especiales __iter__() y __next__() para crear iteradores personalizados.


# ============================================================
# EJERCICIO 1: Iterador de números ascendentes hasta un límite
# ============================================================
# Consigna:
# Crea un iterador llamado "Ascendente" que recorra números desde 1 hasta un límite dado.
# Demuestra su uso recorriendo hasta 5.

class Ascendente:
    def __init__(self, limite):
        self.limite = limite
        self.actual = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual <= self.limite:
            valor = self.actual
            self.actual += 1
            return valor
        else:
            raise StopIteration

print("EJ 1:", list(Ascendente(5)))  # [1, 2, 3, 4, 5]


# ============================================================
# EJERCICIO 2: Iterador de números impares
# ============================================================
# Consigna:
# Implementa un iterador que genere solo números impares hasta un máximo dado.

class Impares:
    def __init__(self, maximo):
        self.maximo = maximo
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.maximo:
            actual = self.num
            self.num += 2
            return actual
        else:
            raise StopIteration

print("EJ 2:", list(Impares(10)))  # [1, 3, 5, 7, 9]


# ============================================================
# EJERCICIO 3: Iterador de caracteres de una cadena
# ============================================================
# Consigna:
# Crea un iterador que recorra una cadena carácter por carácter.

class IteradorCadena:
    def __init__(self, texto):
        self.texto = texto
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.texto):
            char = self.texto[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration

print("EJ 3:", list(IteradorCadena("Python")))  # ['P','y','t','h','o','n']


# ============================================================
# EJERCICIO 4: Iterador de cuadrados de números
# ============================================================
# Consigna:
# Crea un iterador que genere los cuadrados de los primeros N números enteros.

class Cuadrados:
    def __init__(self, n):
        self.n = n
        self.actual = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual <= self.n:
            valor = self.actual ** 2
            self.actual += 1
            return valor
        else:
            raise StopIteration

print("EJ 4:", list(Cuadrados(5)))  # [1, 4, 9, 16, 25]


# ============================================================
# EJERCICIO 5: Iterador de cuenta regresiva
# ============================================================
# Consigna:
# Implementa un iterador que haga una cuenta regresiva desde un número hasta 0.

class CuentaRegresiva:
    def __init__(self, inicio):
        self.inicio = inicio

    def __iter__(self):
        return self

    def __next__(self):
        if self.inicio >= 0:
            valor = self.inicio
            self.inicio -= 1
            return valor
        else:
            raise StopIteration

print("EJ 5:", list(CuentaRegresiva(5)))  # [5, 4, 3, 2, 1, 0]


# ============================================================
# EJERCICIO 6: Iterador de vocales en un texto
# ============================================================
# Consigna:
# Crea un iterador que devuelva solo las vocales de un texto dado.

class Vocales:
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

print("EJ 6:", list(Vocales("Iteradores en Python")))  
# ['i', 'e', 'a', 'o', 'e', 'e', 'o']


# ============================================================
# EJERCICIO 7: Iterador de múltiplos de un número
# ============================================================
# Consigna:
# Implementa un iterador que genere múltiplos de un número base hasta un límite.

class Multiplos:
    def __init__(self, base, limite):
        self.base = base
        self.limite = limite
        self.actual = base

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual <= self.limite:
            valor = self.actual
            self.actual += self.base
            return valor
        else:
            raise StopIteration

print("EJ 7:", list(Multiplos(3, 15)))  # [3, 6, 9, 12, 15]


# ============================================================
# EJERCICIO 8: Iterador infinito (detener manualmente)
# ============================================================
# Consigna:
# Crea un iterador infinito de números naturales. 
# Muestra solo los primeros 5 con un bucle for y break.

class Naturales:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return self.num

nats = Naturales()
res = []
for x in nats:
    if x > 5:
        break
    res.append(x)
print("EJ 8:", res)  # [1, 2, 3, 4, 5]


# ============================================================
# EJERCICIO 9: Iterador de palabras de una frase
# ============================================================
# Consigna:
# Crea un iterador que devuelva palabra por palabra de una frase.

class Palabras:
    def __init__(self, frase):
        self.palabras = frase.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.palabras):
            palabra = self.palabras[self.index]
            self.index += 1
            return palabra
        else:
            raise StopIteration

print("EJ 9:", list(Palabras("Python es genial")))  
# ['Python', 'es', 'genial']


# ============================================================
# EJERCICIO 10: Iterador de Fibonacci
# ============================================================
# Consigna:
# Implementa un iterador que genere los primeros N números de la sucesión de Fibonacci.

class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador < self.n:
            valor = self.a
            self.a, self.b = self.b, self.a + self.b
            self.contador += 1
            return valor
        else:
            raise StopIteration

print("EJ 10:", list(Fibonacci(8)))  
# [0, 1, 1, 2, 3, 5, 8, 13]
