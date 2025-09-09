# ----------------------------------------
# EJERCICIO 5 - Cálculo de salario
# ----------------------------------------
# Se ingresa nombre, horas trabajadas y valor por hora
# Se calcula y muestra el salario

# ========== MÉTODO 1: Código básico ==========
print("\n🔹 MÉTODO 1: Código básico")
nombre = input("Ingrese el nombre del empleado: ")
horas = int(input("Ingrese las horas trabajadas: "))
valor = float(input("Ingrese el valor de la hora: "))
salario = horas * valor
print(f"Hola {nombre}, tu salario es: ${salario:.2f}")


# ========== MÉTODO 2: Función que retorna salario ==========
print("\n🔹 MÉTODO 2: Función para calcular salario")

def calcular_salario(horas, valor_hora):
    return horas * valor_hora

nombre2 = input("Nombre: ")
horas2 = int(input("Horas trabajadas: "))
valor2 = float(input("Valor por hora: "))
salario2 = calcular_salario(horas2, valor2)
print(f"Hola {nombre2}, tu salario es: ${salario2:.2f}")


# ========== MÉTODO 3: Validación simple de input ==========
print("\n🔹 MÉTODO 3: Validación básica")

nombre3 = input("Nombre: ")

while True:
    try:
        horas3 = int(input("Horas trabajadas: "))
        if horas3 < 0:
            print("No puede ser negativo")
            continue
        break
    except ValueError:
        print("Ingresa un número entero válido")

while True:
    try:
        valor3 = float(input("Valor por hora: "))
        if valor3 < 0:
            print("No puede ser negativo")
            continue
        break
    except ValueError:
        print("Ingresa un número válido")

salario3 = horas3 * valor3
print(f"Hola {nombre3}, tu salario es: ${salario3:.2f}")


# ========== MÉTODO 4: Usando función y f-string ==========
print("\n🔹 MÉTODO 4: Función + f-string")

def mostrar_salario(nombre, horas, valor):
    salario = horas * valor
    print(f"Hola {nombre}, tu salario es: ${salario:.2f}")

nombre4 = input("Nombre: ")
horas4 = int(input("Horas: "))
valor4 = float(input("Valor hora: "))
mostrar_salario(nombre4, horas4, valor4)


# ========== MÉTODO 5: Uso de lambda ==========
print("\n🔹 MÉTODO 5: Lambda para calcular salario")

calcular = lambda h, v: h * v

nombre5 = input("Nombre: ")
horas5 = int(input("Horas trabajadas: "))
valor5 = float(input("Valor hora: "))
salario5 = calcular(horas5, valor5)
print(f"Hola {nombre5}, tu salario es: ${salario5:.2f}")
