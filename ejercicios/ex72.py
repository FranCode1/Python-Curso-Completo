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
    print("4 - Salir")

    decision = input("Elija una opcion de 1-4 \n")

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
        nombre = input("Ingrese el nombre de la materia a modificar: ")
        if nombre in materias:
            nuevo_nota = int(input("Ingrese la nueva nota: "))
            materias[nombre] = nuevo_nota
            print(f"Nota actualizada: {nombre}: {nuevo_nota}")
        else:
            print("Materia no encontrada.")

    elif decision == "3":
        if not materias:
            print("No hay materias registradas.")
        else:
            print("Listado de materias:")
            suma=0
            for nota in materias.values():
                #print(f"• {nombre}: {nota}")
                suma += nota
            promedio = suma/len(materias)
            print(f"El promedio de las notas es: {promedio}")

    elif decision == "4":
        print("Hasta luego")
        break

    else:
        print("Decision Erronea")