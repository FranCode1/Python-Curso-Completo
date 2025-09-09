Perfecto, Franco. Ahora entramos en terreno más avanzado: la **Programación Orientada a Objetos (POO)**. En esta **Clase 9**, vamos a introducir los conceptos básicos de **clases**, **objetos**, **atributos** y **métodos**.

---

## 🧱 Clase 9: **Clases y conceptos de Programación Orientada a Objetos (POO)**

---

### 🧠 1. Resumen del tema

#### ¿Qué es la Programación Orientada a Objetos?

La POO es un **paradigma de programación** basado en el uso de **objetos**, que son estructuras que combinan **datos** (atributos) y **comportamientos** (métodos).

> Python es un lenguaje orientado a objetos, lo que significa que casi todo en Python es un objeto.

---

### 🔧 ¿Qué es una clase?

Una **clase** es como una **plantilla** o **molde** para crear objetos. Define qué atributos y métodos va a tener el objeto.

#### Sintaxis básica:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
```

---

### 👤 ¿Qué es un objeto?

Un **objeto** es una instancia concreta de una clase.

```python
persona1 = Persona("Franco", 22)
persona1.saludar()  # Hola, me llamo Franco y tengo 22 años.
```

---

### 🔑 Conceptos clave:

| Concepto     | Descripción                                                  |
| ------------ | ------------------------------------------------------------ |
| `__init__()` | Método constructor: se ejecuta al crear un objeto            |
| `self`       | Representa al propio objeto (como `this` en otros lenguajes) |
| Atributos    | Variables internas del objeto                                |
| Métodos      | Funciones dentro de una clase                                |

---

### 🎥 2. Video explicativo

📌 **\[Espacio para tu video sobre POO en Python]**

> En este video podrías:
>
> * Mostrar qué es una clase y cómo se define
> * Explicar `__init__` y `self`
> * Crear un objeto y acceder a sus métodos
> * Comparar esto con funciones normales para mostrar la ventaja

---

### 🔗 3. Links útiles para profundizar

* 📘 [Clases/POO en Python – W3Schools](https://www.w3schools.com/python/python_classes.asp)
* 🔎 [Introducción a clases – Programiz](https://www.programiz.com/python-programming/class)
* 📖 [Tutorial oficial sobre clases](https://docs.python.org/3/tutorial/classes.html)
* 🧠 [POO en Python explicado visualmente – Real Python (inglés)](https://realpython.com/python3-object-oriented-programming/)

---

### 🚀 4. Mini proyecto

**📄 Proyecto: “Sistema de mascotas”**

Objetivo: practicar definición de clases, atributos, métodos y creación de objetos.

#### Instrucciones:

1. Creá una clase llamada `Mascota` con los atributos:

   * `nombre`
   * `especie`
   * `edad`

2. Agregá un método `presentarse()` que imprima:
   `"Hola, soy una mascota. Me llamo [nombre], soy un [especie] y tengo [edad] años."`

3. Creá 2 mascotas distintas y llamá al método `presentarse()` de cada una.

#### 💡 Ejemplo esperado:

```python
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, un {self.especie}, y tengo {self.edad} años.")

mascota1 = Mascota("Firulais", "perro", 5)
mascota2 = Mascota("Mishi", "gato", 3)

mascota1.presentarse()
mascota2.presentarse()
```

> ✨ **Bonus:** Agregá un método `cumplir_años()` que sume 1 a la edad.

---

¿Querés que prepare ahora la **Clase 10** (herencia, por ejemplo), o preferís que compile estas 9 clases en una guía organizada en PDF, presentación, carpeta de curso o índice para web/redes? También puedo ayudarte a preparar los desafíos finales o una sección de ejercicios para repaso.
