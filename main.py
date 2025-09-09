#COMENTARIO 1#
"""COMENTARIO 2"""
"""
print("hola")
print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

print(3 + 2 + 1-5 + 4 % 2-1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5-7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh,that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > - 2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)"""

#VARIABLES Y NOMENCLATURAS#

#CamelCase#
camelCase = "textoEjemplo"

#SnakeCase#
variable_ejemplo = "xd"

#se púeden combinar las dos#
variable_De_Ejemplo = "waza"

#LAS CONSTANTES SIEMPRE SE NOMBRAN EN MAYUSCULAS#
CONSTANTE = 323423
#se hace asi para diferenciar de las variables#

#Tipos de Datos#

texto = "ejemplo"
numero1 = 55 #un numero entero es int#
numero2 = 23,4 #un numero con coma es float#
booleano = True #o puede ser False#

a = 3
b = 2
c = "3"
z = a != c
print(z)


#hacer ejercicio que escanee numeros para ver si son par o impar#
num = int(input("ingrese un numero: "))
if num % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar ")
    
#pedir una nota y calificarla si es mayor a 6 aprovado y sino ingreso mal la nota#
nota = int(input("ingrese nota: "))
if nota < 6:
    print("desaprobado")
elif nota > 6 and nota > 10:
    print("aprobado")
else:
    print("nota incorrecta")
    
#pedir un monto si supera los 10k pesos dar un 10% de descuento y mostrar el precio final#
monto = int(input("ingrese monto: "))
if monto > 10000:
    monto_nuevo = monto * 0.10
    print("el nuevo monto es: {monto_nuevo}")
    
#operador ternario:
#var variable = condicion?verdadero:falso
