# Clase base (padre) con 3 métodos
class Parent(object):

    def override(self):
        print("PARENT override()")  # Puede ser sobreescrito por clases hijas

    def implicit(self):
        print("PARENT implicit()")  # Será heredado sin necesidad de redefinirlo

    def altered(self):
        print("PARENT altered()")  # Puede ser llamado con super() desde una subclase



# Otra clase independiente que no hereda de Parent
# Se usará para composición en la clase Child
class Other(object):
    
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")



# Clase hija que NO hereda directamente de Parent, sino que usa composición
class Child(object):

    def __init__(self):
        self.other = Other()  # Composición: Child tiene un objeto Other

    def implicit(self):
        # En lugar de heredar de Parent, redirige a Other
        self.other.implicit()
    
    def override(self):
        print("CHILD override()")  # Sobrescribe completamente el comportamiento

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()  # Llama al método 'altered' de Other
        print("CHILD, AFTER OTHER altered()")



# Una clase adicional que hereda de Parent para usar super()
class ChildWithInheritance(Parent):

    def override(self):
        print("CHILD override()")  # Sobrescribe el método de Parent

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super().altered()  # Llama al método 'altered' de la clase padre (Parent)
        print("CHILD, AFTER PARENT altered()")



# Esta clase fue mencionada pero no definida, así que la agregamos
class BadStuff(object):
    def danger(self):
        print("BAD STUFF happening!")



class SuperFun(Child, BadStuff):
    
    def __init__(self):
        super().__init__()  # Llama al constructor de Child (que crea self.other)
    
    def do_all_the_things(self):
        print("SUPERFUN is doing all the things!")

        # Usamos método de Child
        self.override()

        # Usamos método de Other (por composición)
        self.implicit()

        # Usamos método alterado de Child (que llama a Other.altered())
        self.altered()

        # Usamos método heredado de BadStuff
        self.danger()

        print("SUPERFUN finished everything!")




# Instancias
dad = Parent()               # Objeto de la clase padre
son = Child()                # Objeto que usa composición con Other
son2 = ChildWithInheritance()  # Objeto que hereda de Parent

# Métodos implícitos
print("\n=== IMPLICIT ===")
dad.implicit()       # PARENT implicit()
son.implicit()       # OTHER implicit()
son2.implicit()      # PARENT implicit()

# Métodos override (polimorfismo)
print("\n=== OVERRIDE ===")
dad.override()       # PARENT override()
son.override()       # CHILD override()
son2.override()      # CHILD override()

# Métodos alterados
print("\n=== ALTERED ===")
dad.altered()        # PARENT altered()
son.altered()        # CHILD + OTHER altered()
son2.altered()       # CHILD + PARENT altered()

# Probando SuperFun
print("\n=== SUPERFUN DEMO ===")
sf = SuperFun()
sf.do_all_the_things()
