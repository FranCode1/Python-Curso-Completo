¡Genial, Franco! Vamos con la **Clase 3: Introducción a Listas**, uno de los conceptos más importantes y versátiles en Python. Como siempre, siguiendo el esquema:

---

## 📚 Clase 3: **Introducción a Listas (Lists) en Python**

---

### 🧠 1. Resumen del tema

#### ¿Qué es una lista?

Una **lista** es una estructura de datos que puede contener múltiples valores, **ordenados**, **modificables** y **permiten duplicados**. Son como "cajas" que pueden guardar varios datos en una sola variable.

#### ¿Cómo se crea una lista?

```python
frutas = ["manzana", "banana", "naranja"]
numeros = [1, 2, 3, 4, 5]
mezcla = ["hola", 10, True, 3.14]
```

#### Acceder a elementos:

Se accede por **índice**, empezando desde 0:

```python
print(frutas[0])  # "manzana"
print(frutas[2])  # "naranja"
```

#### Modificar valores:

```python
frutas[1] = "sandía"
```

#### Métodos útiles de listas:

```python
frutas.append("uva")        # Agrega al final
frutas.insert(1, "pera")    # Inserta en posición 1
frutas.remove("naranja")    # Elimina por valor
frutas.pop()                # Elimina el último
print(len(frutas))          # Cantidad de elementos
```

---

### 🎥 2. Video explicativo

📌 **\[Espacio para tu video de listas]**

> En este video podrías:
>
> * Mostrar qué es una lista
> * Crear listas de strings, ints, mezcladas
> * Mostrar cómo acceder, modificar y agregar elementos
> * Explicar qué pasa si usás un índice fuera del rango
> * Mostrar `append()`, `insert()`, `remove()` y `len()`

---

### 🔗 3. Links útiles para profundizar

* 📚 [Listas en Python – W3Schools](https://www.w3schools.com/python/python_lists.asp)
* 💡 [Introducción a listas – Programiz](https://www.programiz.com/python-programming/list)
* 📘 [Listas – Documentación oficial de Python](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
* 🧠 [Métodos de listas – Real Python (en inglés)](https://realpython.com/python-lists-tuples/)

---

### 🚀 4. Mini proyecto

**📄 Proyecto: “Mi lista de compras”**

Objetivo: practicar creación y manipulación de listas con operaciones básicas.

#### Instrucciones:

1. Creá una lista con al menos 5 productos que querés comprar.
2. Imprimí toda la lista.
3. Mostrá el primer y el último producto.
4. Agregá un nuevo producto con `append()`.
5. Reemplazá uno de los productos por otro.
6. Eliminá uno con `remove()`.
7. Mostrá cuántos productos hay en total.

#### 💡 Ejemplo esperado:

```python
compras = ["pan", "leche", "huevos", "arroz", "queso"]

print("Lista completa:", compras)
print("Primero:", compras[0])
print("Último:", compras[-1])

compras.append("café")
compras[2] = "yogur"
compras.remove("pan")

print("Lista actualizada:", compras)
print("Total de productos:", len(compras))
```

> ✨ **Opcional:** imprimí cada elemento de la lista en una línea usando un `for`.

---

¿Avanzamos con la **Clase 4** (por ejemplo: bucles `for` y recorrido de listas), o querés que prepare esta clase como PDF o presentación? También puedo armarte una estructura con carpetas para que organices todo tu curso.
