¡Perfecto, Franco! Siguiendo la continuidad lógica, en la **Clase 4** vamos a profundizar en el uso de listas en Python: cómo recorrerlas, ordenarlas, hacer slicing y usar más métodos útiles. Esto ayudará a que tus alumnos pasen de simplemente tener listas a **trabajar activamente con ellas**.

---

## 🛠️ Clase 4: **Trabajando con Listas en Python**

---

### 🧠 1. Resumen del tema

En la clase anterior aprendiste qué es una lista y cómo manipularla.
Ahora vas a aprender a **recorrer listas**, **ordenarlas**, **filtrarlas** y usar **métodos avanzados** para sacarles provecho real.

---

### 🔁 Recorrer listas con `for`

```python
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)
```

También se puede usar `range()` y `len()` si necesitás el índice:

```python
for i in range(len(colores)):
    print(f"Color #{i + 1}: {colores[i]}")
```

---

### 🔪 Slicing (rebanado)

Permite tomar solo una parte de la lista:

```python
numeros = [10, 20, 30, 40, 50]
print(numeros[1:4])    # [20, 30, 40]
print(numeros[:3])     # [10, 20, 30]
print(numeros[-2:])    # [40, 50]
```

---

### 🧰 Métodos adicionales útiles

```python
numeros = [3, 7, 1, 9, 4]
numeros.sort()        # Ordena la lista (ascendente)
numeros.reverse()     # Invierte el orden
print(max(numeros))   # Mayor valor
print(min(numeros))   # Menor valor
print(sum(numeros))   # Suma de todos los valores
```

---

### 📦 Copiar listas (¡evitá errores!)

```python
lista1 = [1, 2, 3]
lista2 = lista1       # Esto apunta a la misma lista
lista3 = lista1[:]    # Esto crea una copia real
```

---

### 🎥 2. Video explicativo

📌 **\[Espacio para el video donde mostrás el trabajo con listas paso a paso]**

> En este video podés mostrar:
>
> * Cómo recorrer listas con `for`
> * Cómo usar `range(len(...))`
> * Qué es el slicing y cómo aplicarlo
> * Ordenar, invertir y copiar listas
> * Buenas prácticas y errores comunes (como modificar una lista mientras se recorre)

---

### 🔗 3. Links útiles para profundizar

* 🔁 [Recorrer listas – W3Schools](https://www.w3schools.com/python/python_lists_loop.asp)
* 🔪 [Slicing – Programiz](https://www.programiz.com/python-programming/list)
* 📘 [Métodos de listas – Documentación oficial](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
* 🧠 [Funciones útiles con listas – Real Python (inglés)](https://realpython.com/python-lists-tuples/)

---

### 🚀 4. Mini proyecto

**📄 Proyecto: “Organizador de tareas”**

Objetivo: aplicar recorrido de listas, métodos y slicing.

#### Instrucciones:

1. Creá una lista con al menos 6 tareas.
2. Mostrá solo las primeras 3 tareas del día.
3. Agregá una nueva tarea al final.
4. Ordená las tareas alfabéticamente.
5. Mostrá todas las tareas con un índice numerado.
6. Mostrá la última tarea con slicing.
7. Mostrá cuántas tareas hay en total.

#### 💡 Ejemplo esperado:

```python
tareas = ["estudiar", "limpiar", "leer", "programar", "hacer ejercicio", "comprar comida"]

print("Tareas para hoy (primeras 3):", tareas[:3])

tareas.append("meditar")
tareas.sort()

print("\nTodas las tareas ordenadas:")
for i in range(len(tareas)):
    print(f"{i + 1}. {tareas[i]}")

print("\nÚltima tarea:", tareas[-1])
print("Total de tareas:", len(tareas))
```

> ✨ **Bonus:** permití que el usuario agregue nuevas tareas con `input()` y las agregue a la lista.

---

¿Querés que sigamos con la **Clase 5** (por ejemplo: `input()`, `print()` avanzado y `f-strings`), o preferís que te entregue estas 4 clases en formato PDF o presentación? También te puedo armar un índice general con enlaces internos para todo el curso.
