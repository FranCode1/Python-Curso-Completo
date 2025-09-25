# =====================================================================
# EJERCICIO 78: Clase Coche
# ---------------------------------------------------------------------
# Crear una clase Coche con los siguientes atributos:
# • marca
# • modelo
# • año
# Crear un metodo para mostrar la info
# =====================================================================

class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_datos(self):
        print(f"Marca: {self.marca} \nModelo: {self.marca} \nAño: {self.año}")

print("_____________________Primer Coche_____________________")
objeto1 = Coche("Peugeot", 308, 2014)
objeto1.mostrar_datos()

print("_____________________Segundo Coche____________________")
objeto2 = Coche("Volkswagen", "Bora", 2012)
objeto2.mostrar_datos()

print("_____________________Tercer Coche_____________________")
objeto3 = Coche("Fiat", "Palio", 2009)
objeto3.mostrar_datos()