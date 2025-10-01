# ----------------------------------------
# CLASE 27: ENCAPSULAMIENTO Y PROPIEDADES EN PYTHON
# ----------------------------------------

# 📌 ¿Qué es el encapsulamiento?
# Es un principio de la Programación Orientada a Objetos (POO) que busca 
# restringir el acceso directo a los atributos de un objeto, protegiendo 
# los datos y controlando cómo se modifican.
#
# En Python no existe un verdadero "privado", pero se usan convenciones:
# - Público: atributo normal (self.nombre)
# - Protegido: atributo con _guion_bajo (self._saldo)
# - Privado: atributo con __doble_guion (self.__pin)
#
# 📌 ¿Qué son las propiedades (properties)?
# Son una forma de acceder a métodos como si fueran atributos, usando 
# decoradores como @property, @getter y @setter.


# ==========================
# 🔹 ENCAPSULAMIENTO BÁSICO
# ==========================

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular   # público
        self._saldo = saldo      # protegido
        self.__pin = 1234        # privado

    def mostrar_saldo(self):
        return self._saldo

    def depositar(self, cantidad):
        self._saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            print("Fondos insuficientes")

cuenta = CuentaBancaria("Franco", 1000)
cuenta.depositar(500)
print(cuenta.mostrar_saldo())  # 1500
# print(cuenta.__pin)  # ❌ Error: atributo privado


# ==========================
# 🔹 USO DE PROPERTIES
# ==========================

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio  # atributo protegido

    # Getter (acceso al valor)
    @property
    def precio(self):
        return self._precio

    # Setter (modifica el valor con validación)
    @precio.setter
    def precio(self, valor):
        if valor < 0:
            print("El precio no puede ser negativo.")
        else:
            self._precio = valor

    # Deleter (opcional, elimina el atributo)
    @precio.deleter
    def precio(self):
        print("El precio ha sido eliminado.")
        del self._precio

p = Producto("Laptop", 1500)
print(p.precio)   # Accede al getter
p.precio = 2000   # Usa el setter
print(p.precio)
p.precio = -50    # ❌ No se permite


# ==========================
# 🔹 ENCAPSULAMIENTO + PROPIEDADES
# ==========================

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            print("❌ El salario no puede ser negativo.")
        else:
            self._salario = valor

emp = Empleado("Lucía", 3000)
print(emp.salario)
emp.salario = 3500
print(emp.salario)


# ==========================
# 🧪 MINI PROYECTO PRÁCTICO
# ==========================
# 🎯 Crear una clase Estudiante con:
# - nombre (público)
# - _nota (protegido, solo 0 a 10)
# - Una property para validar la nota
# - Método mostrar_info para imprimir datos

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self._nota = None
        self.nota = nota  # usar setter

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("❌ La nota debe estar entre 0 y 10.")

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, Nota: {self._nota}")

# Probar mini proyecto
alumno = Estudiante("Franco", 8)
alumno.mostrar_info()
alumno.nota = 11   # ❌ No permitido
alumno.mostrar_info()


# ----------------------------------------
# CONCLUSIÓN DE LA CLASE
# ----------------------------------------

# En esta clase aprendiste:
# - Qué es el encapsulamiento y cómo se aplica en Python
# - Diferencia entre atributos públicos, protegidos y privados
# - Cómo usar propiedades (properties) para validar y controlar acceso
# - Mini proyecto: clase Estudiante con property para validar nota

# Próxima clase: Sobrecarga de operadores en Python (__add__, __len__, etc.)
