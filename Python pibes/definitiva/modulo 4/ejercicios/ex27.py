# ----------------------------------------
# CLASE 28: OPERATOR OVERLOADING - EJERCICIOS RESUELTOS
# ----------------------------------------

# ========================================
# EJERCICIO 1: Sobrecarga de __add__
# Consigna: Crear una clase Complejo que permita sumar dos números complejos con +
# ========================================

class Complejo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, otro):
        return Complejo(self.real + otro.real, self.imag + otro.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complejo(2, 3)
c2 = Complejo(1, 4)
print(c1 + c2)  # 3 + 7i


# ========================================
# EJERCICIO 2: Sobrecarga de __sub__
# Consigna: Implementar resta de puntos en un plano cartesiano.
# ========================================

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, otro):
        return Punto(self.x - otro.x, self.y - otro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Punto(5, 4)
p2 = Punto(2, 1)
print(p1 - p2)  # (3, 3)


# ========================================
# EJERCICIO 3: Sobrecarga de __mul__
# Consigna: Clase Vector que permita multiplicar por un escalar usando *.
# ========================================

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)

    def __str__(self):
        return f"<{self.x}, {self.y}>"

v = Vector(2, 3)
print(v * 4)  # <8, 12>


# ========================================
# EJERCICIO 4: Sobrecarga de __eq__ y __ne__
# Consigna: Crear clase Persona donde dos personas son iguales si tienen misma edad.
# ========================================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otro):
        return self.edad == otro.edad

    def __ne__(self, otro):
        return self.edad != otro.edad

p1 = Persona("Ana", 25)
p2 = Persona("Juan", 25)
print(p1 == p2)  # True
print(p1 != p2)  # False


# ========================================
# EJERCICIO 5: Sobrecarga de __len__
# Consigna: Clase Documento donde len(obj) devuelva la cantidad de palabras.
# ========================================

class Documento:
    def __init__(self, texto):
        self.texto = texto

    def __len__(self):
        return len(self.texto.split())

doc = Documento("Python es divertido de aprender")
print(len(doc))  # 5


# ========================================
# EJERCICIO 6: Sobrecarga de __getitem__ y __setitem__
# Consigna: Crear clase ListaEnteros que permita acceder y modificar valores con [].
# ========================================

class ListaEnteros:
    def __init__(self, datos):
        self.datos = datos

    def __getitem__(self, i):
        return self.datos[i]

    def __setitem__(self, i, valor):
        self.datos[i] = valor

le = ListaEnteros([1, 2, 3])
print(le[1])  # 2
le[1] = 99
print(le[1])  # 99


# ========================================
# EJERCICIO 7: Sobrecarga de __gt__ y __lt__
# Consigna: Clase Caja que compara según cantidad de elementos.
# ========================================

class Caja:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __gt__(self, otra):
        return len(self) > len(otra)

    def __lt__(self, otra):
        return len(self) < len(otra)

c1 = Caja([1, 2, 3])
c2 = Caja([1, 2])
print(c1 > c2)  # True
print(c1 < c2)  # False


# ========================================
# EJERCICIO 8: Sobrecarga de __contains__
# Consigna: Clase Inventario que soporte "obj in inventario".
# ========================================

class Inventario:
    def __init__(self, productos):
        self.productos = productos

    def __contains__(self, item):
        return item in self.productos

inv = Inventario(["pan", "leche", "huevos"])
print("pan" in inv)      # True
print("queso" in inv)    # False


# ========================================
# EJERCICIO 9: Sobrecarga de __str__ y __repr__
# Consigna: Clase Fraccion con representación en str y repr.
# ========================================

class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraccion({self.num}, {self.den})"

f = Fraccion(3, 4)
print(str(f))   # 3/4
print(repr(f))  # Fraccion(3, 4)


# ========================================
# EJERCICIO 10: Mini Proyecto - Matriz
# Consigna: Crear clase Matriz con:
# - __add__ para sumar matrices
# - __getitem__ para acceder a elementos
# - __str__ para imprimir bonito
# ========================================

class Matriz:
    def __init__(self, datos):
        self.datos = datos

    def __add__(self, otra):
        resultado = []
        for fila1, fila2 in zip(self.datos, otra.datos):
            resultado.append([a+b for a, b in zip(fila1, fila2)])
        return Matriz(resultado)

    def __getitem__(self, idx):
        return self.datos[idx]

    def __str__(self):
        return "\n".join(str(fila) for fila in self.datos)

m1 = Matriz([[1, 2], [3, 4]])
m2 = Matriz([[5, 6], [7, 8]])
print(m1 + m2)
print((m1 + m2)[0])  # [6, 8]


# ----------------------------------------
# ✅ Fin de los 10 ejercicios resueltos
# ----------------------------------------
