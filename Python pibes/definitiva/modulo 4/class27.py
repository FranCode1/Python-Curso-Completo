# ----------------------------------------
# CLASE 28: OPERATOR OVERLOADING EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es la sobrecarga de operadores?
# Es la capacidad de redefinir el comportamiento de los operadores (+, -, *, etc.)
# para que funcionen con objetos de clases personalizadas.
#
# Esto se hace implementando métodos especiales llamados "dunder methods"
# (porque comienzan y terminan con doble guion bajo, ej: __add__, __len__).

# ==========================
# 🔹 EJEMPLO BÁSICO CON __add__
# ==========================

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Sobrecarga del operador +
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    # Sobrecarga del método __str__ para imprimir
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Punto(2, 3)
p2 = Punto(4, 1)
p3 = p1 + p2  # usa __add__
print(p3)     # (6, 4)


# ==========================
# 🔹 OTROS OPERADORES ÚTILES
# ==========================

class Caja:
    def __init__(self, items):
        self.items = items

    def __len__(self):       # len(obj)
        return len(self.items)

    def __getitem__(self, i):  # obj[i]
        return self.items[i]

    def __eq__(self, otro):  # obj1 == obj2
        return self.items == otro.items

    def __str__(self):       # print(obj)
        return f"Caja con {len(self)} elementos"

c1 = Caja([1, 2, 3])
c2 = Caja([1, 2, 3])
c3 = Caja([4, 5])

print(len(c1))      # 3
print(c1[1])        # 2
print(c1 == c2)     # True
print(c1 == c3)     # False
print(c1)           # Caja con 3 elementos


# ==========================
# 🔹 LISTA DE MÉTODOS ESPECIALES MÁS COMUNES
# ==========================
# __str__     → str(obj) o print(obj)
# __len__     → len(obj)
# __getitem__ → obj[i]
# __setitem__ → obj[i] = valor
# __delitem__ → del obj[i]
# __add__     → obj1 + obj2
# __sub__     → obj1 - obj2
# __mul__     → obj1 * obj2
# __eq__      → obj1 == obj2
# __lt__      → obj1 < obj2
# __gt__      → obj1 > obj2
# __contains__→ elem in obj


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================
# 🎯 Clase Vector que soporte:
# - Suma de vectores (+)
# - Comparación por magnitud (==, <, >)
# - Representación en string (__str__)

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, otro):
        return self.magnitud() == otro.magnitud()

    def __lt__(self, otro):
        return self.magnitud() < otro.magnitud()

    def __gt__(self, otro):
        return self.magnitud() > otro.magnitud()

    def __str__(self):
        return f"<{self.x}, {self.y}>"

# Probar mini proyecto
v1 = Vector(3, 4)   # magnitud = 5
v2 = Vector(1, 7)   # magnitud ≈ 7.07
v3 = v1 + v2

print(v1)       # <3, 4>
print(v2)       # <1, 7>
print(v3)       # <4, 11>
print(v1 < v2)  # True
print(v1 == v2) # False


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es la sobrecarga de operadores (operator overloading)
# - Cómo redefinir operadores comunes con métodos especiales
# - Ejemplos prácticos: __add__, __len__, __eq__, __getitem__
# - Mini proyecto: clase Vector con suma y comparación de magnitud

# Próxima clase: Programación funcional en Python (map, filter, reduce, etc.)
