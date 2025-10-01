# ----------------------------------------
# CLASE 27: ENCAPSULAMIENTO Y PROPERTIESO - EJERCICIOS RESUELTOS
# ----------------------------------------

# ========================================
# EJERCICIO 1: Atributo privado
# Consigna: Crear una clase Usuario con atributo __password.
# Protegerlo para que solo se pueda acceder mediante un método.
# ========================================

class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.__password = password  # privado

    def verificar_password(self, intento):
        return intento == self.__password

u = Usuario("Franco", "1234")
print(u.verificar_password("1234"))  # True
print(u.verificar_password("0000"))  # False


# ========================================
# EJERCICIO 2: Atributo protegido
# Consigna: Crear una clase Cuenta con _saldo protegido.
# Acceder solo mediante métodos depositar y retirar.
# ========================================

class Cuenta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, monto):
        self._saldo += monto

    def retirar(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar(self):
        print(f"Saldo actual: {self._saldo}")

c = Cuenta(500)
c.depositar(200)
c.retirar(100)
c.mostrar()


# ========================================
# EJERCICIO 3: Property simple
# Consigna: Clase Persona con atributo edad validado (0-120).
# Usar property para controlarlo.
# ========================================

class Persona:
    def __init__(self, edad):
        self._edad = None
        self.edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if 0 <= valor <= 120:
            self._edad = valor
        else:
            print("Edad inválida")

p = Persona(25)
print(p.edad)
p.edad = 150  # ❌ inválido


# ========================================
# EJERCICIO 4: Property con deleter
# Consigna: Clase Producto con atributo precio.
# Se puede borrar con del usando @deleter.
# ========================================

class Producto:
    def __init__(self, precio):
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor >= 0:
            self._precio = valor
        else:
            print("El precio no puede ser negativo")

    @precio.deleter
    def precio(self):
        print("El precio ha sido eliminado")
        del self._precio

prod = Producto(100)
print(prod.precio)
prod.precio = 200
del prod.precio


# ========================================
# EJERCICIO 5: Validación en property
# Consigna: Clase Alumno con atributo nota (0-10).
# Evitar valores fuera de rango.
# ========================================

class Alumno:
    def __init__(self, nota):
        self._nota = None
        self.nota = nota

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("❌ Nota inválida")

a = Alumno(8)
print(a.nota)
a.nota = 15  # ❌


# ========================================
# EJERCICIO 6: Encapsulamiento en jerarquía
# Consigna: Clase Animal con _energia protegida.
# Subclase Perro que accede mediante métodos.
# ========================================

class Animal:
    def __init__(self, energia=100):
        self._energia = energia

    def mostrar_energia(self):
        print(f"Energía: {self._energia}")

class Perro(Animal):
    def correr(self):
        self._energia -= 10

dog = Perro()
dog.mostrar_energia()
dog.correr()
dog.mostrar_energia()


# ========================================
# EJERCICIO 7: Read-only property
# Consigna: Clase Libro con atributo titulo solo de lectura.
# ========================================

class Libro:
    def __init__(self, titulo):
        self._titulo = titulo

    @property
    def titulo(self):
        return self._titulo  # solo lectura

lib = Libro("1984")
print(lib.titulo)
# lib.titulo = "Otro"  # ❌ no se puede


# ========================================
# EJERCICIO 8: Property calculada
# Consigna: Clase Rectangulo con atributos ancho y alto.
# Crear property area que calcule automáticamente.
# ========================================

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return self.ancho * self.alto

r = Rectangulo(5, 4)
print("Área:", r.area)


# ========================================
# EJERCICIO 9: Encapsulamiento con métodos
# Consigna: Clase Tarjeta con __numero privado.
# Permitir mostrar solo los últimos 4 dígitos.
# ========================================

class Tarjeta:
    def __init__(self, numero):
        self.__numero = numero

    def mostrar(self):
        return "**** **** **** " + self.__numero[-4:]

t = Tarjeta("1234567812345678")
print(t.mostrar())


# ========================================
# EJERCICIO 10: Mini proyecto Usuario con saldo
# Consigna: Crear una clase UsuarioBanco con:
# - nombre público
# - _saldo protegido
# - property saldo (con validación de no negativo)
# ========================================

class UsuarioBanco:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self._saldo = None
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("❌ El saldo no puede ser negativo")

    def mostrar_info(self):
        print(f"Usuario: {self.nombre}, Saldo: {self._saldo}")

u = UsuarioBanco("Lucía", 500)
u.mostrar_info()
u.saldo = -100  # ❌ inválido
u.mostrar_info()

# ----------------------------------------
# ✅ Fin de los 10 ejercicios resueltos
# ----------------------------------------
