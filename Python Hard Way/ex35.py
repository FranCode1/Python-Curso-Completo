# Definimos una clase base llamada Animal. Hereda de 'object' (aunque en Python 3 ya no es necesario explícitamente).
# Esta clase no tiene comportamiento por ahora (usamos 'pass').
class Animal(object):
    pass

# Definimos una clase Dog que hereda de Animal. Es decir, Dog es un tipo de Animal.
class Dog(Animal):

    # Método constructor que recibe un nombre y lo guarda como atributo del objeto.
    def __init__(self, name):
        self.name = name  # 'self.name' es un atributo propio de cada objeto Dog

# Definimos una clase Cat, también hereda de Animal, igual que Dog.
class Cat(Animal):

    def __init__(self, name):
        self.name = name  # Igual que en Dog, guarda el nombre como atributo

# Definimos una clase Person, que NO hereda de Animal.
class Person(object):

    def __init__(self, name):
        self.name = name  # Guarda el nombre de la persona

        # Atributo 'pet' inicializado en None. Luego puede ser asignado a un animal (Dog o Cat).
        self.pet = None

# Clase Employee hereda de Person, lo que significa que un empleado es una persona.
class Employee(Person):

    def __init__(self, name, salary):
        # Usamos 'super()' para llamar al constructor de la clase padre (Person)
        super(Employee, self).__init__(name)

        # Agregamos un nuevo atributo específico de Employee: el salario
        self.salary = salary

# Clase Fish, una clase base para tipos de peces.
class Fish(object):
    pass

# Salmon hereda de Fish
class Salmon(Fish):
    pass

# Halibut también hereda de Fish
class Halibut(Fish):
    pass

# -------------------------------------------------------
# Creación de instancias (objetos)

# Creamos un objeto 'rover' que es una instancia de la clase Dog
rover = Dog("Rover")

# Creamos un objeto 'satan' que es una instancia de la clase Cat
satan = Cat("Satan")

# Creamos una persona llamada Mary
mary = Person("Mary")

# A Mary le asignamos un gato como mascota (satan)
mary.pet = satan

# Creamos un empleado llamado Frank, con un salario de 120000
frank = Employee("Frank", 120000)

# A Frank le asignamos un perro como mascota (rover)
frank.pet = rover

# Creamos una instancia de Fish llamada 'flipper'
flipper = Fish()

# Creamos una instancia de Salmon llamada 'crouse'
crouse = Salmon()

# Creamos una instancia de Halibut llamada 'harry'
harry = Halibut()
