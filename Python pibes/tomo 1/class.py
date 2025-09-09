¡Excelente, Franco! Acá tenés la **Clase 2: Variables y Tipos de Datos (Data Types)**, siguiendo la misma estructura que en la clase anterior. Esta clase es fundamental para que tus alumnos entiendan cómo manejar información en Python.

---

## 🧠 Clase 2: **Variables y Tipos de Datos en Python**

---

### 🧠 1. Resumen del tema

#### ¿Qué es una variable?

Una **variable** es un nombre que usamos para guardar un valor. Nos permite almacenar datos y usarlos más adelante.

#### ¿Cómo se crea una variable?

En Python es muy simple:

```python
nombre = "Franco"
edad = 22
```

> No hace falta indicar el tipo, Python lo detecta automáticamente.

#### Reglas para nombrar variables:

* Deben empezar con una **letra** o un **guion bajo** (`_`)
* No pueden comenzar con un número
* No pueden tener espacios ni caracteres especiales
* Son sensibles a mayúsculas/minúsculas: `nombre` ≠ `Nombre`

---

#### Tipos de datos básicos en Python:

| Tipo    | Ejemplo         | Descripción                         |
| ------- | --------------- | ----------------------------------- |
| `int`   | `10`, `-5`      | Números enteros                     |
| `float` | `3.14`, `-0.5`  | Números decimales                   |
| `str`   | `"Hola"`        | Cadenas de texto                    |
| `bool`  | `True`, `False` | Valores booleanos (verdadero/falso) |

```python
edad = 20             # int
altura = 1.75         # float
nombre = "Lucía"      # str
estudiante = True     # bool
```

---

#### La función `type()`

Podés usarla para saber qué tipo de dato tiene una variable:

```python
print(type(edad))      # <class 'int'>
print(type(nombre))    # <class 'str'>
```

---

### 🎥 2. Video explicativo

📌 **\[Espacio para tu video sobre variables y tipos de datos]**

> En este video podés mostrar:
>
> * Qué es una variable y cómo se usa
> * Crear variables con distintos tipos
> * Errores comunes (como usar nombres inválidos)
> * `type()` para mostrar el tipo de dato
> * Comparar una variable `int` con una `str`, etc.

---

### 🔗 3. Links útiles para profundizar

* 📚 [Variables en Python – W3Schools](https://www.w3schools.com/python/python_variables.asp)
* 💡 [Tipos de datos – Programiz](https://www.programiz.com/python-programming/variables-datatypes)
* 📘 [Tipos de datos – Documentación oficial de Python](https://docs.python.org/es/3/library/stdtypes.html)
* ✏️ [Variables y tipos en Python – Real Python (inglés)](https://realpython.com/python-data-types/)

---

### 🚀 4. Mini proyecto

**📄 Proyecto: “Ficha de usuario”**

Objetivo: aplicar variables y tipos de datos para mostrar información personal.

#### Instrucciones:

1. Creá variables para:

   * Tu nombre (str)
   * Tu edad (int)
   * Tu altura en metros (float)
   * Si estás aprendiendo Python (bool)

2. Mostralas con `print()` usando un formato claro.

#### 💡 Ejemplo esperado:

```python
nombre = "Franco Lugo"
edad = 22
altura = 1.78
aprendiendo_python = True

print("=== FICHA DE USUARIO ===")
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura, "m")
print("¿Aprendiendo Python?", aprendiendo_python)
```

> ✨ **Opcional:** usá `type()` para imprimir el tipo de cada variable al lado.

---

¿Seguimos con la **Clase 3** (podría ser: Strings y texto), o querés que prepare esto en PDF o presentación? También puedo darte una estructura para organizar todas las clases en carpetas o en Google Drive.
