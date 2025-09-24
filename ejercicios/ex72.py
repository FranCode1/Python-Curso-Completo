# =====================================================================
# EJERCICIO 72: Carrito de Compras
# ---------------------------------------------------------------------
# Crear un diccionario que represente un carrito de compras
# donde las claves sean los productos y los valores cantidades
# El menu debe tener:
# • Agregar producto (si el producto ya existe, sumar a cantidad)
# • Modificar cantidad
# • Eliminar producto
# • Salir
# =====================================================================


carrito = {
    "detergente": 3,
    "cereal": 1,
    "chocolates": 2,
}

while True:
    print("Que desea hacer?: ")
    print("1 - Agregar producto")
    print("2 - Modificar cantidad")
    print("3 - Eliminar producto")
    print("4 - Mostrar Carrito")
    print("5 - Salir")

    decision = input("Elija una opcion de 1-5 \n")

    if decision == "1":
        producto = input("Ingrese el nombre del producto: ")
        if producto in carrito:
            print("Ya existe este producto en el carrito")
            print("Cantidad a agregar: ")
            nueva_cantidad = int(input("Ingrese la cantidad: "))
            cantidad_actualizada = carrito[producto] + nueva_cantidad
            print(f"Nota actualizada: {producto}: {cantidad_actualizada}")
        else:
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            carrito[producto] = cantidad_producto
            print(f"Producto Agregado: {producto}: {cantidad_producto}")

    elif decision == "2":
        producto = input("Ingrese el nombre del producto: ")
        if producto in carrito:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            carrito[producto] = nueva_cantidad
            print(f"Nota actualizada: {producto}: {nueva_cantidad}")
        else:
            print("Materia no encontrada.")

    elif decision == "3":
        producto = input("Ingrese el nombre del producto a eliminar: ")
        if producto in carrito:
            del carrito[producto]
            print("Producto eliminado")
        else:
            print("Producto no encontrado.")

    elif decision == "4":
        if not carrito:
            print("No hay productos registrados.")
        else:
            print("Listado de productos:")
            for producto, cantidad in carrito.items():
                print(f"• {producto}: {cantidad}")

    elif decision == "5":
        print("Hasta luego")
        break

    else:
        print("Decision Erronea")