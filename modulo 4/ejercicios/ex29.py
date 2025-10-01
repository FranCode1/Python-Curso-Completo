# ----------------------------------------
# CLASE 30: METAPROGRAMACIÓN EN PYTHON
# ----------------------------------------
# Ejercicios resueltos con consignas incluidas
# ----------------------------------------

# ======================================================
# EJERCICIO 1: Uso básico de getattr
# Consigna: Crea una clase Coche con atributos "marca" y "modelo".
#           Obtén dinámicamente el valor de "marca" usando getattr.
# ======================================================
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

c = Coche("Toyota", "Corolla")
print("Ejercicio 1 →", getattr(c, "marca"))  # Toyota


# ======================================================
# EJERCICIO 2: Verificar atributos con hasattr
# Consigna: Crea una clase Libro con atributos "titulo" y "autor".
#           Verifica si existe un atributo "precio".
# ======================================================
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

l = Libro("1984", "George Orwell")
print("Ejercicio 2 →", hasattr(l, "precio"))  # False


# ======================================================
# EJERCICIO 3: Asignar atributos con setattr
# Consigna: Crea un objeto y agrega dinámicamente el atributo "edad".
# ======================================================
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

p = Persona("Franco")
setattr(p, "edad", 22)
print("Ejercicio 3 →", p.nombre, p.edad)  # Franco 22


# ======================================================
# EJERCICIO 4: Eliminar atributos con delattr
# Consigna: Crea una clase Animal con atributo "especie".
#           Luego elimina ese atributo dinámicamente.
# ======================================================
class Animal:
    def __init__(self, especie):
        self.especie = especie

a = Animal("Perro")
delattr(a, "especie")
print("Ejercicio 4 →", hasattr(a, "especie"))  # False


# ======================================================
# EJERCICIO 5: Introspección de atributos
# Consigna: Muestra todos los atributos de un objeto usando dir()
#           y su diccionario interno con __dict__.
# ======================================================
print("Ejercicio 5 →", dir(p)[:5])  # primeros 5 atributos
print("Ejercicio 5 →", p.__dict__)  # {'nombre': 'Franco', 'edad': 22}


# ======================================================
# EJERCICIO 6: Crear clase con type()
# Consigna: Crea dinámicamente una clase "Producto" con atributo "precio".
# ======================================================
Producto = type("Producto", (), {"precio": 100})
producto = Producto()
print("Ejercicio 6 →", producto.precio)  # 100


# ======================================================
# EJERCICIO 7: Invocar métodos dinámicamente
# Consigna: Crea una clase Calculadora con métodos sumar y restar.
#           Invoca "restar" usando getattr con un string.
# ======================================================
class Calculadora:
    def sumar(self, x, y): return x + y
    def restar(self, x, y): return x - y

calc = Calculadora()
operacion = "restar"
print("Ejercicio 7 →", getattr(calc, operacion)(10, 3))  # 7


# ======================================================
# EJERCICIO 8: Convertir objeto a diccionario
# Consigna: Crea una función genérica que convierta cualquier
#           objeto en diccionario con sus atributos.
# ======================================================
def objeto_a_diccionario(obj):
    return {k: v for k, v in obj.__dict__.items()}

print("Ejercicio 8 →", objeto_a_diccionario(p))  
# {'nombre': 'Franco', 'edad': 22}


# ======================================================
# EJERCICIO 9: Añadir método dinámicamente
# Consigna: Usa setattr para añadir un método "saludar"
#           a la clase Persona en tiempo de ejecución.
# ======================================================
def saludar(self):
    return f"Hola, soy {self.nombre}"

setattr(Persona, "saludar", saludar)
print("Ejercicio 9 →", p.saludar())  # Hola, soy Franco


# ======================================================
# EJERCICIO 10: Modificar clase ya existente
# Consigna: Crea una clase Vacía y en tiempo de ejecución
#           agrégale un atributo y un método.
# ======================================================
class Vacia: pass

obj = Vacia()
setattr(obj, "dato", 123)
setattr(Vacia, "mostrar", lambda self: f"Dato = {self.dato}")

print("Ejercicio 10 →", obj.mostrar())  # Dato = 123
