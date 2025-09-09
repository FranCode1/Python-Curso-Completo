# Parte 1 - Practica (en papel)
#1. Escribir un programa en Python que:
#   - Pida al usuario un numero entero
#   - Muestre la tabla de multiplica de ese numero del 1 al 10
#   - Guarde la tabla en un archivo de texto llamado tabla.txt
def tablas():
    num = int(input("Ingrese un numero entero: "))
    # texto = open('tabla.txt', 'w')
    with open('tabla.txt', 'w') as texto:
        for i in range(1, 11):
            # print(f"{num}x", i, " es: ", num*i)
            # texto.write(f"{num}x", i, " es: ", num*i)
            linea = f"{num} x {i} = {num * i}"
            print(linea)
            texto.write(linea + "\n")
    
    # texto.close()


#2. Crear un funcion es_primo(n) que reciba un numero que retorne True si es primo y False si no lo es.
def es_primo1(n):
    # if n==2:
    #     return True # único primo par
    # elif (n%n==0 and n%1==0) and (n%2==0 or n%3==0 or n%4==0):
    #     return False
    # elif n%n==0 and n%1==0:
    #     return True
    # else:
    #     return False
    if n==2:
        return True # unico primo par
    if n < 2 or n % 2 == 0:
        return False # Descarta numero menores a 2 y pares mayores a 2
    
    for i in range(3, n):
        if n % 1 == 0:
            return False
    return True

def es_primo2(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# numero primo: entero y solo puede ser divisible por 1 y si mismo, el 2 es el unico numero primo par

# Luego, usar esa funcion para mostrar todos los primos del 1 al 50.
def todos_primos():
    for i in range(1, 51):
        # if i==2:
        #     print(i)
        # elif (i/i==0 and i/1==0) and (i/2==0 or i/3==0 or i/4==0):
        #     continue
        # elif i/i==0 and i/1==0:
        #     print(i)
        # else:
        #     continue
        if es_primo2(i):
            print(i)


#3. Crear un diccionario con 3 productos y sus precios.
# El usuario debe ingresar el nombre de un producto y mostrar su precio, o indicar que no existe.
productos = {
    "leche": 50,
    "azucar": 5,
    "trigo": 20,
}
# asi es en JS productos.leche
# en Python es asi productos["leche"]

compra = input("Ingrese el nombre del producto: ").lower()

if compra in productos:
    print(f"El precio de {compra} es: ${productos[compra]}")
else:
    print("Producto no encontrado")


# Parte 2 - Diagrama de flujo
#   - Dibujar el diagrama de flujo para el punto 1.
# Dalo por valido, se hacer esto


# Parte 3 - Preguntas Teoricas
#1. Que diferencia hay enter un bucle for y un bucle while?
#El bucle for recorre una secuencia conocida (lista, rango, cadena) y suele tener un número de repeticiones definido.
#El while repite un bloque de código mientras una condición sea verdadera, sin saber cuántas veces se repetirá.


#2. Que es una variable global y como se define en Python?
#Una variable global es aquella que se declara fuera de cualquier función y puede ser usada desde cualquier parte del programa.
# x = 5  # global

# def cambiar():
#     global x
#     x = 10



#3. Explica que hace este codigo:
#   lista = [2, 4, 6]
#   lista = [x**2 for x in lista if x > 2]
#Este código crea una nueva lista con los cuadrados de los números en lista solo si son mayores que 2.
#Resultado final: [16, 36].


#4. Que es un algoritmo y cuales son sus caracteristicas principales?
#Un algoritmo es una secuencia finita de pasos lógicos que resuelven un problema o realizan una tarea.
#Características: finito, ordenado, claro, preciso y con un resultado definido.


#5. Que diferencia hay entre un error de sintaxis y un error de ejecucion?
#Error de sintaxis: se produce cuando el código no cumple las reglas del lenguaje (ej. falta de paréntesis, indentación incorrecta). El programa no se ejecuta.

#Error de ejecución: ocurre mientras el programa se está ejecutando (ej. división por cero, acceso a índice inexistente en una lista).