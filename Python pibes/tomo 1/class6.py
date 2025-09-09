¡Genial, Franco! La **Clase 6: Diccionarios** introduce una de las estructuras de datos más poderosas y usadas de Python: los **`dict`**. Es una evolución lógica después de listas y condicionales, y esencial para proyectos más complejos.

---

## 📖 Clase 6: **Diccionarios en Python**

---

### 🧠 1. Resumen del tema

#### ¿Qué es un diccionario?

Un **diccionario** (`dict`) es una estructura que almacena datos en **pares clave-valor** (key-value).
A diferencia de las listas, los diccionarios **no usan índices numéricos**, sino **claves** que pueden ser strings, números, etc.

---

### ✅ Sintaxis básica

```python
persona = {
    "nombre": "Franco",
    "edad": 22,
    "ciudad": "Córdoba"
}
```

Acceder a valores:

```python
print(persona["nombre"])  # "Franco"
```

Modificar valores:

```python
persona["edad"] = 23
```

Agregar nuevos pares:

```python
persona["profesion"] = "Diseñador"
```

Eliminar claves:

```python
del persona["ciudad"]
```

---

### 🔧 Métodos útiles

| Método          | Descripción                            |
| --------------- | -------------------------------------- |
| `.keys()`       | Retorna las claves                     |
| `.values()`     | Retorna los valores                    |
| `.items()`      | Retorna los pares clave-valor          |
| `.get("clave")` | Accede sin error si no existe la clave |

```python
print(persona.keys())
print(persona.values())
print(persona.get("altura", "No especificado"))
```

---

### 📚 Diccionarios anidados

Un diccionario puede contener otros diccionarios:

```python
usuarios = {
    "usuario1": {"nombre": "Lucía", "edad": 20},
    "usuario2": {"nombre": "Pedro", "edad": 25}
}
```

---

### 🎥 2. Video explicativo

📌 **\[Espacio para tu video sobre diccionarios]**

> Mostrá:
>
> * Qué es un diccionario
> * Cómo acceder, modificar, agregar y eliminar claves
> * Mostrar `.get()`, `.keys()`, `.items()`
> * Mostrar ejemplos de diccionarios anidados y cómo recorrerlos con `for`

---

### 🔗 3. Links útiles para profundizar

* 📘 [Diccionarios en Python – W3Schools](https://www.w3schools.com/python/python_dictionaries.asp)
* 🔎 [Diccionarios – Programiz](https://www.programiz.com/python-programming/dictionary)
* 📖 [Dict – Documentación oficial](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
* 🧠 [Anidamiento de diccionarios – Real Python (en inglés)](https://realpython.com/python-dicts/)

---

### 🚀 4. Mini proyecto

**📄 Proyecto: “Ficha de usuario con diccionario”**

Objetivo: practicar creación, modificación y acceso a diccionarios.

#### Instrucciones:

1. Creá un diccionario llamado `usuario` con los siguientes datos:

   * nombre
   * edad
   * email
   * ciudad

2. Mostrá cada dato con `print()`.

3. Agregá una nueva clave: `"ocupacion"`.

4. Mostrá todas las claves y todos los valores.

5. Permití que el usuario cambie su ciudad usando `input()`.

#### 💡 Ejemplo esperado:

```python
usuario = {
    "nombre": "Franco Lugo",
    "edad": 22,
    "email": "franco@email.com",
    "ciudad": "Córdoba"
}

print("Nombre:", usuario["nombre"])
print("Edad:", usuario["edad"])
print("Email:", usuario["email"])
print("Ciudad:", usuario["ciudad"])

usuario["ocupacion"] = "Diseñador Web"

print("\nClaves:", list(usuario.keys()))
print("Valores:", list(usuario.values()))

nueva_ciudad = input("¿En qué ciudad vivís ahora? ")
usuario["ciudad"] = nueva_ciudad

print("\nDatos actualizados:", usuario)
```

> ✨ **Bonus:** agregá más usuarios como diccionarios anidados.

---

¿Querés que pasemos ahora a la **Clase 7** (por ejemplo, bucles `while`, o funciones), o te preparo una carpeta con PDFs o presentaciones de estas 6 clases? También puedo armarte un índice del curso para distribuirlo mejor.
