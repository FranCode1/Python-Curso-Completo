¡Genial, Franco! Vamos con la **Clase 8: Funciones**, uno de los pilares de la programación. A partir de acá tus alumnos podrán escribir **código reutilizable**, modular y mucho más organizado.

---

## 🧩 Clase 8: **Funciones en Python**

---

### 🧠 1. Resumen del tema

#### ¿Qué es una función?

Una **función** es un bloque de código que se puede **reutilizar**. Sirve para organizar tareas específicas, evitar repetir código y hacer que los programas sean más claros y ordenados.

---

### 🔧 Sintaxis básica:

```python
def saludar():
    print("Hola, mundo")
```

#### Llamar a la función:

```python
saludar()
```

---

### 🔡 Parámetros y argumentos:

Podés pasar datos a una función mediante **parámetros**:

```python
def saludar(nombre):
    print("Hola,", nombre)

saludar("Franco")
```

Podés usar múltiples parámetros:

```python
def sumar(a, b):
    print(a + b)

sumar(3, 7)
```

---

### 🔙 Return (retornar valores)

Una función puede **devolver un resultado** en lugar de solo imprimir:

```python
def multiplicar(x, y):
    return x * y

resultado = multiplicar(4, 5)
print("Resultado:", resultado)
```

---

### 🔁 Ventajas de usar funciones:

* Reutilización de código
* Facilita la lectura y mantenimiento
* Permite dividir programas en partes lógicas

---

### 🎥 2. Video explicativo

📌 **\[Espacio para tu video sobre funciones]**

> Mostrá:
>
> * Qué es una función
> * Cómo definir y llamar funciones
> * Qué son parámetros, argumentos y return
> * Diferencia entre imprimir (`print()`) y retornar (`return`)
> * Casos prácticos: saludar, sumar, verificar edad, etc.

---

### 🔗 3. Links útiles para profundizar

* 📘 [Funciones en Python – W3Schools](https://www.w3schools.com/python/python_functions.asp)
* 🧠 [Funciones – Programiz](https://www.programiz.com/python-programming/function)
* 📖 [Funciones definidas por el usuario – Docs oficiales](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* 🔄 [Retorno de funciones – Real Python (inglés)](https://realpython.com/defining-your-own-python-function/)

---

### 🚀 4. Mini proyecto

**📄 Proyecto: “Calculadora de IMC (Índice de Masa Corporal)”**

Objetivo: usar funciones con parámetros, operaciones y retorno de valores.

#### Instrucciones:

1. Creá una función que reciba peso (kg) y altura (m).
2. Que calcule el IMC con la fórmula:
   `imc = peso / (altura ** 2)`
3. Que retorne el resultado.
4. Usá `input()` para pedir los datos al usuario.
5. Mostrá el IMC con 2 decimales y un mensaje según el resultado.

#### 💡 Ejemplo esperado:

```python
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("¿Cuál es tu peso en kg? "))
altura = float(input("¿Cuál es tu altura en metros? "))

imc = calcular_imc(peso, altura)
print(f"Tu IMC es {imc:.2f}")

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Peso normal")
else:
    print("Sobrepeso o más")
```

> ✨ **Bonus:** convertí la función para que también clasifique automáticamente el IMC (bajo, normal, alto).

---

¿Seguimos con la **Clase 9** (puede ser lógica booleana, operadores lógicos o incluso manejo de errores), o preferís compilar las primeras 8 clases en PDF, PowerPoint o guía general para compartir con tus alumnos? También puedo ayudarte a armar una estructura de carpetas o plan de publicación si lo estás subiendo a redes o a una plataforma de cursos.
