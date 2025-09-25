# # =====================================================================
# EJERCICIO 82: Concesionario
# ---------------------------------------------------------------------
# Crear una clase llamada Auto, con los siguientes campos:
# • marca
# • modelo
# • precio
# Agregar 4 autos
# Mostrar los datos del auto más caro
# =====================================================================

class Auto:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}"


def main():
    autos = []

    # Cargar 4 autos
    for i in range(4):
        print(f"\n--- Auto {i+1} ---")
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        precio = float(input("Ingrese el precio: "))
        autos.append(Auto(marca, modelo, precio))

    # Encontrar el auto más caro
    auto_mas_caro = max(autos, key=lambda x: x.precio)

    print("\nEl auto más caro es:")
    print(auto_mas_caro)


if __name__ == "__main__":
    main()
