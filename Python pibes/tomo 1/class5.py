¡Perfecto, Franco! Vamos con la **Clase 5: If Statements**, que introduce la **toma de decisiones en Python**. Este es un punto clave donde los alumnos empiezan a crear programas que **responden a condiciones**.

---

## 🔀 Clase 5: **Sentencias condicionales `if` en Python**

---

### 🧠 1. Resumen del tema

#### ¿Qué es una sentencia `if`?

Una sentencia `if` permite que un programa **tome decisiones**.
Ejecuta una parte del código **solo si se cumple una condición**.

#### Sintaxis básica:

```python
if condición:
    # bloque de código que se ejecuta si la condición es verdadera
```

#### También podemos usar:

* `else`: si la condición **no se cumple**
* `elif`: para evaluar **más condiciones** si la primera no fue verdadera

---

### ✅ Ejemplos:

```python
edad = 18

if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")
```

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
```

---

### ℹ️ Comparadores comunes:

| Operador | Significado       | Ejemplo   |
| -------- | ----------------- | --------- |
| `==`     | Igual a           | `x == 5`  |
| `!=`     | Distinto de       | `x != 10` |
| `<`      | Menor que         | `x < 100` |
| `>`      | Mayor que         | `x > 0`   |
| `<=`     | Menor o igual que | `x <= 5`  |
| `>=`     | Mayor o igual que | `x >= 3`  |

---

### 🎥 2. Video explicativo

📌 **\[Espacio para tu video sobre if/else/elif]**

> Mostrá:
>
> * Qué es un `if`, cómo se usa
> * Uso de `else` y `elif`
> * Errores comunes de indentación
> * Usar `input()` para probar condiciones reales con datos del usuario
> * Mostrar múltiples caminos en una decisión

---

### 🔗 3. Links útiles para profundizar

* 🔀 [Condicionales en Python – W3Schools](https://www.w3schools.com/python/python_conditions.asp)
* 🧠 [If, elif, else – Programiz](https://www.programiz.com/python-programming/if-elif-else)
* 📘 [Control de flujo – Documentación oficial](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
* 🔎 [Guía visual de condicionales (inglés) – Real Python](https://realpython.com/python-conditional-statements/)

---

### 🚀 4. Mini proyecto

**📄 Proyecto: “Validador de edad para acceder a un sitio”**

Objetivo: practicar el uso de `if`, `else` y `elif` con entradas del usuario.

#### Instrucciones:

1. Pedí al usuario su nombre y edad con `input()`.
2. Convertí la edad a `int`.
3. Mostrá diferentes mensajes según la edad:

   * Menor de 13: “No podés acceder.”
   * Entre 13 y 17: “Acceso limitado con supervisión.”
   * 18 o más: “Acceso total permitido.”

#### 💡 Ejemplo esperado:

```python
nombre = input("¿Cómo te llamás? ")
edad = int(input("¿Qué edad tenés? "))

print(f"\nHola, {nombre}!")

if edad < 13:
    print("No podés acceder.")
elif edad < 18:
    print("Acceso limitado con supervisión.")
else:
    print("Acceso total permitido.")
```

> ✨ **Bonus:** Agregá un mensaje especial si la edad es exactamente 100:
> `"¡Wow, 100 años! Sos una leyenda."`

---

¿Seguimos con la **Clase 6** (podría ser: lógica booleana y operadores lógicos `and`, `or`, `not`), o querés que prepare un índice de las clases o un PDF agrupado con estas cinco primeras?
