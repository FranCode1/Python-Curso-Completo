¡Perfecto, Franco! Vamos con la **Clase 6**, donde vas a profundizar en el uso de `print()`, **secuencias de escape**, y además introducir **`input()`** y **parámetros de `print()`** como `sep` y `end`. Esta clase le da al alumno herramientas clave para interactuar con el usuario y mostrar datos de forma más controlada.

---

## 🧩 Clase 6: **Más sobre `print()`, Secuencias de Escape, Inputs y Parámetros**

### 1. 🧠 Resumen teórico

#### 📤 `print()` avanzado:

Además de mostrar texto, `print()` tiene parámetros útiles:

| Parámetro | Descripción                                             | Ejemplo                                          |
| --------- | ------------------------------------------------------- | ------------------------------------------------ |
| `sep`     | Define el separador entre los valores                   | `print("Hola", "mundo", sep="-")` → `Hola-mundo` |
| `end`     | Define lo que se imprime al final (por defecto es `\n`) | `print("Hola", end="")` no hace salto de línea   |

```python
print("Python", "3", "Rocks", sep=" ~ ", end="!")
# Output: Python ~ 3 ~ Rocks!
```

---

#### 🧵 Secuencias de escape:

Las usamos para agregar símbolos especiales dentro de strings:

| Secuencia | Significado           | Ejemplo                         |
| --------- | --------------------- | ------------------------------- |
| `\n`      | Salto de línea        | `print("Hola\nMundo")`          |
| `\t`      | Tabulación            | `print("Nombre:\tFranco")`      |
| `\\`      | Barra invertida       | `print("C:\\Users\\Franco")`    |
| `\"`      | Comilla doble literal | `print("Dijo: \"Hola mundo\"")` |

---

#### 🔡 `input()` y prompts:

`input()` permite al usuario ingresar datos. Siempre devuelve un **string**.

```python
nombre = input("¿Cómo te llamás? ")
print(f"Hola, {nombre}!")
```

> Si necesitás números, convertí el input:

```python
edad = int(input("¿Qué edad tenés? "))
```

---

### 2. 🎥 Video explicativo

📌 *\[Espacio para tu video]*

> Mostrá usos de `sep`, `end`, ejemplos de `input()` con y sin `int()`, y errores comunes como olvidar convertir valores o usar mal las secuencias de escape.

---

### 3. 🧪 Ejercicio práctico con solución

#### ✅ Ejercicio:

1. Pedí al usuario su nombre, edad y ciudad con `input()`.
2. Mostralo en un formato limpio, usando `\n`, `sep`, `end` o f-strings.

#### 🧩 Solución ejemplo:

```python
nombre = input("¿Cómo te llamás? ")
edad = input("¿Qué edad tenés? ")
ciudad = input("¿De dónde sos? ")

print("\n===== FICHA DE USUARIO =====")
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)
```

---

### 4. 🔗 Links recomendados

* 💬 [print() y sus parámetros – W3Schools](https://www.w3schools.com/python/ref_func_print.asp)
* ⌨️ [input() en Python – Programiz](https://www.programiz.com/python-programming/input-output)
* 🧵 [Secuencias de escape – Real Python](https://realpython.com/python-strings/#escape-sequences)

---

### 5. 🚀 Desafío corto

**Desafío:**
Hacé una mini "entrevista" interactiva que pida al usuario:

* Su nombre
* Una comida favorita
* Un color que no le gusta

Y mostrala como una historia corta. Ejemplo:

```python
nombre = input("¿Tu nombre?: ")
comida = input("¿Tu comida favorita?: ")
color = input("¿Un color que no te guste?: ")

print(f"\nHabía una vez una persona llamada {nombre}.\nLe encantaba comer {comida}, pero no soportaba el color {color}.")
```

> Bonus: probá cambiar `sep` y `end` para que el texto se vea diferente o más estilizado.

---

¿Seguimos con la Clase 7 (podría ser condiciones: `if`, `else`, `elif`), o preferís preparar PDFs, guiones para tus videos o presentaciones antes de seguir? También te puedo armar un índice con todas las clases ya hechas.
