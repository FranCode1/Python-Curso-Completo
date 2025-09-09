#4. DFD(Diagrama de Flujo):
#Dibujar un DFD para un algoritmo que pida tres numero y muestre el mayor.

#Comparar tres numeros, mostrar el mayor.

first_number = float(input('Ingrese el primer número: '))
second_number = float(input('Ingrese el segundo número: '))
third_number = float(input('Ingrese el tercer número: '))

if first_number > second_number and first_number > third_number:
    print('El primer número es mayor')
elif second_number > first_number and second_number > third_number:
    print('El segundo número es mayor')
elif third_number > first_number and third_number > second_number:
    print('El tercer número es mayor')
elif first_number == second_number and second_number == third_number:
    print('Los tres números son iguales')
elif first_number == second_number and first_number > third_number:
    print("El primer y segundo número son los mayores")
elif second_number == third_number and second_number > first_number:
    print("El segundo y tercer número son los mayores")
elif first_number == third_number and third_number > second_number:
    print("El primer y tercer número son los mayores")
else:
    print('Valores ingresados incorrectos')