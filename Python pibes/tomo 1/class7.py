¡Perfecto, Franco! La **Clase 7: Inputs del usuario y bucles `while`** combina dos herramientas fundamentales para crear programas **interactivos** y **dinámicos**. Acá te va todo el contenido, bien estructurado como venís pidiendo:

---

## 🔁 Clase 7: **User Input y Bucles While en Python**

---

### 🧠 1. Resumen del tema

#### 🧑‍💻 `input()` – Entrada del usuario

Permite **leer datos que escribe el usuario** en la terminal. Siempre devuelve un **`str`** (string), aunque lo que escriba sea un número.

```python
nombre = input("¿Cómo te llamás? ")
print("Hola,", nombre)
```

> Para usar números, necesitás convertir el string:

```python
edad = int(input("¿Qué edad tenés? "))
```

---

#### 🔁 `while` loop – Bucle mientras

Permite ejecutar una parte del código **mientras una condición sea verdadera**.

```python
contador = 1
while contador <= 5:
    print("Número:", contador)
    contador += 1
```

⚠️ ¡Cuidado con los **bucles infinitos**! Siempre asegurate de que la condición cambie.

---

#### 🔚 Cómo detener un bucle:

* `break` → interrumpe el bucle
* `continue` → salta al siguiente ciclo sin terminar el actual

```python
while True:
    entrada = input("Escribí 'salir' para terminar: ")
    if entrada == "salir":
        break
```

---

### 🎥 2. Video explicativo

📌 **\[Espacio para tu video sobre `input()` y `while`]**

> Mostrá:
>
> * Cómo leer datos del usuario con `input()`
> * Cómo convertir a `int` o `float`
> * Qué es un bucle `while`, cómo evitar infinitos
> * Uso de `break` y `continue`
> * Un mini juego o interacción en consola

---

### 🔗 3. Links útiles para profundizar

* 🔤 [Input del usuario – Programiz](https://www.programiz.com/python-programming/input-output)
* 🔁 [Bucles While – W3Schools](https://www.w3schools.com/python/python_while_loops.asp)
* 📘 [Control de flujo – Documentación oficial](https://docs.python.org/3/tutorial/controlflow.html#while-statements)
* 🧠 [Bucles interactivos – Real Python (en inglés)](https://realpython.com/python-while-loop/)

---

### 🚀 4. Mini proyecto

**📄 Proyecto: “Adiviná el número”**

Objetivo: combinar `input()` con `while` para hacer un juego interactivo.

#### Instrucciones:

1. Guardá un número secreto (ej: 7).
2. Pedí al usuario que intente adivinarlo.
3. Mientras no acierte, pedíle otro número.
4. Si adivina, mostrale un mensaje de felicitación.
5. Mostrá cuántos intentos le llevó.

#### 💡 Ejemplo esperado:

```python
secreto = 7
intentos = 0

while True:
    guess = int(input("Adiviná el número (entre 1 y 10): "))
    intentos += 1
    
    if guess == secreto:
        print("¡Correcto! Adivinaste en", intentos, "intentos.")
        break
    else:
        print("Incorrecto. Probá de nuevo.")
```

> ✨ **Bonus:** agregá validación para que el número esté entre 1 y 10.

---

¿Querés que prepare ahora la **Clase 8** (por ejemplo, funciones), o te gustaría que compile todas estas clases en un PDF, presentación o guía del curso para subir a Drive o Classroom? También puedo prepararte un índice general con todos los temas y accesos rápidos.
