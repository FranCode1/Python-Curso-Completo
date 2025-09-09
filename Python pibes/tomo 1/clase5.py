¡Vamos con la Clase 5, Franco! Esta va a estar enfocada en **Strings y manejo de texto en Python**, algo esencial para cualquier programador, ya sea para mostrar mensajes, procesar datos o interactuar con usuarios.

---

## 🧵 Clase 5: **Strings y Manejo de Texto**

### 1. 🧠 Resumen teórico

#### ¿Qué es un string?

Un **string** (cadena de texto) es un tipo de dato que representa texto.
Se escribe entre **comillas simples (' ')** o **comillas dobles (" ")**:

```python
mensaje = "Hola mundo"
nombre = 'Franco'
```

#### Caracteres especiales útiles:

* `\n` → salto de línea
* `\t` → tabulación
* `\\` → barra invertida
* `\"` → comilla doble literal

```python
print("Hola\n¿Cómo estás?")  # Salto de línea
```

---

### ✂️ Operaciones comunes con strings:

| Acción               | Ejemplo             | Resultado      |
| -------------------- | ------------------- | -------------- |
| Concatenar textos    | `"Hola " + "mundo"` | `"Hola mundo"` |
| Repetir texto        | `"ha" * 3`          | `"hahaha"`     |
| Saber longitud       | `len("Python")`     | `6`            |
| Acceder a letras     | `"Python"[0]`       | `'P'`          |
| Slicing (substrings) | `"Python"[0:3]`     | `'Pyt'`        |

---

### 🧰 Métodos útiles de strings:

```python
texto = "Hola Mundo"

print(texto.lower())      # "hola mundo"
print(texto.upper())      # "HOLA MUNDO"
print(texto.capitalize()) # "Hola mundo"
print(texto.replace("o", "0")) # "H0la Mund0"
print("mundo" in texto)   # False (ojo con mayúsculas)
```

> *Los strings en Python son inmutables: no se pueden cambiar directamente, pero podés crear uno nuevo basado en otro.*

---

### 2. 🎥 Video explicativo

📌 *\[Espacio para tu video]*

> Mostrá qué es un string, cómo se declara, cómo concatenar, cómo usar métodos y slicing. Usá ejemplos visuales.

---

### 3. 🧪 Ejercicio práctico con solución

#### ✅ Ejercicio:

1. Creá una variable con tu nombre completo.
2. Mostralo en:

   * Todo mayúsculas
   * Todo minúsculas
   * Solo la primera letra en mayúscula
3. Imprimí cuántas letras tiene tu nombre (sin contar espacios).

#### 🧩 Solución ejemplo:

```python
nombre = "Franco Lugo"

print(nombre.upper())       # MAYÚSCULAS
print(nombre.lower())       # minúsculas
print(nombre.capitalize())  # Capitalizado

sin_espacios = nombre.replace(" ", "")
print(len(sin_espacios))    # Cantidad de letras sin espacios
```

---

### 4. 🔗 Links recomendados

* 🧵 [Métodos de strings – W3Schools](https://www.w3schools.com/python/python_strings_methods.asp)
* 🔠 [Slicing de strings – Programiz](https://www.programiz.com/python-programming/string)
* 📘 [Strings – Documentación oficial de Python](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

---

### 5. 🚀 Desafío corto

**Desafío:**
Pedí el nombre de un usuario y mostralo en un formato tipo etiqueta con estilo:

```python
# Entrada
nombre = "martin rodriguez"

# Salida esperada
print("===== ETIQUETA =====")
print(f"Nombre completo: {nombre.title()}")
print(f"Número de letras (sin espacios): {len(nombre.replace(' ', ''))}")
print("=====================")
```

> Bonus: agregá la opción de ingresar el nombre usando `input()`.

---

¿Querés que sigamos con la Clase 6 (por ejemplo, estructuras de decisión: `if`, `else`, `elif`)? También puedo prepararte una carpeta organizada con todo el contenido listo para presentar, imprimir o subir a una plataforma.
