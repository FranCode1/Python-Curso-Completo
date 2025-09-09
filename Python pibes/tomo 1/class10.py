¡Perfecto, Franco! La **Clase 10: Archivos y Excepciones** es ideal para que tus alumnos aprendan a manejar archivos del sistema (leer/escribir) y a **evitar errores inesperados** en sus programas usando el manejo de **excepciones**. Esta clase marca una transición hacia programas más reales y robustos.

---

## 📂 Clase 10: **Archivos y Excepciones en Python**

---

### 🧠 1. Resumen del tema

### 🗃️ Leer y escribir archivos

#### Abrir un archivo:

```python
archivo = open("datos.txt", "r")  # "r" = read (lectura)
contenido = archivo.read()
archivo.close()
print(contenido)
```

#### Escribir en un archivo:

```python
archivo = open("datos.txt", "w")  # "w" = write (sobrescribe)
archivo.write("Hola mundo!")
archivo.close()
```

#### Agregar contenido (sin borrar lo anterior):

```python
archivo = open("datos.txt", "a")  # "a" = append
archivo.write("\nNueva línea")
archivo.close()
```

#### Leer línea por línea:

```python
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
```

> `with open(...)` es la forma recomendada: cierra el archivo automáticamente.

---

### ⚠️ Excepciones y manejo de errores

Una **excepción** ocurre cuando el programa encuentra un error que lo interrumpe.
Para evitar que el programa se detenga, usamos `try-except`.

#### Ejemplo:

```python
try:
    num = int(input("Ingresá un número: "))
    print(10 / num)
except ValueError:
    print("¡Eso no es un número!")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
```

También podés usar:

* `else`: si no hubo errores
* `finally`: se ejecuta siempre (haya error o no)

---

### 🎥 2. Video explicativo

📌 **\[Espacio para tu video sobre archivos y excepciones]**

> Mostrá:
>
> * Cómo leer y escribir archivos (`open`, `read`, `write`)
> * Uso de `with open()`
> * Qué es una excepción
> * Uso de `try-except`, y ejemplos comunes de errores
> * Aplicación práctica combinando ambos conceptos

---

### 🔗 3. Links útiles para profundizar

* 📄 [Archivos en Python – W3Schools](https://www.w3schools.com/python/python_file_handling.asp)
* 🧠 [Excepciones – Programiz](https://www.programiz.com/python-programming/exception-handling)
* 📘 [Errores y manejo – Docs oficiales](https://docs.python.org/3/tutorial/errors.html)
* 🔎 [Lectura y escritura de archivos – Real Python (en inglés)](https://realpython.com/read-write-files-python/)

---

### 🚀 4. Mini proyecto

**📄 Proyecto: “Registrador de notas con manejo de errores”**

Objetivo: practicar escritura en archivos y manejo de errores con entrada del usuario.

#### Instrucciones:

1. Pedí al usuario su nombre y su nota (entre 0 y 10).
2. Verificá que la nota sea un número válido.
3. Si todo está bien, guardalo en un archivo `notas.txt` así:
   `"Franco - 9"`

#### 💡 Ejemplo esperado:

```python
try:
    nombre = input("Nombre del estudiante: ")
    nota = float(input("Nota (0-10): "))
    
    if nota < 0 or nota > 10:
        raise ValueError("Nota fuera de rango.")

    with open("notas.txt", "a") as archivo:
        archivo.write(f"{nombre} - {nota}\n")
    print("Nota guardada correctamente.")

except ValueError as e:
    print("Error:", e)
```

> ✨ **Bonus:** Mostrá todo el contenido de `notas.txt` después de guardar la nueva entrada.

---

¿Te gustaría que prepare ahora la **Clase 11** (por ejemplo: módulos y paquetes), o que compile estas 10 clases en PDF o presentación general del curso? También puedo ayudarte a preparar ejercicios integradores o un examen final.
