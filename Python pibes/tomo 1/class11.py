¡Excelente, Franco! En esta **Clase 11** vamos a introducir el **testing (pruebas)**, una habilidad crucial para escribir código **confiable y mantenible**. Aunque muchas veces se deja para programadores avanzados, es bueno enseñar desde el principio a **probar y verificar que el código funciona como se espera**.

---

## ✅ Clase 11: **Testing Your Code en Python**

---

### 🧠 1. Resumen del tema

### 🧪 ¿Qué es un test?

Un **test** es una verificación automática que se hace sobre el código para asegurarse de que devuelve el resultado correcto.
Hay muchos tipos de test, pero el más básico y común es el **test unitario**, que prueba una función específica.

---

### 🧰 ¿Por qué hacer testing?

* Evita errores invisibles
* Asegura que los cambios no rompan cosas
* Facilita el mantenimiento del código
* Te obliga a pensar en los posibles errores

---

### 🧪 Ejemplo básico sin librerías

```python
def sumar(a, b):
    return a + b

# test manual
if sumar(2, 3) == 5:
    print("✅ Test pasado")
else:
    print("❌ Test fallado")
```

---

### ✅ Usando la librería `unittest` (incluida en Python)

```python
import unittest

def multiplicar(a, b):
    return a * b

class TestMultiplicacion(unittest.TestCase):
    def test_positivo(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_cero(self):
        self.assertEqual(multiplicar(0, 100), 0)

    def test_negativos(self):
        self.assertEqual(multiplicar(-2, 3), -6)

if __name__ == "__main__":
    unittest.main()
```

📝 Cada `def test_algo(self):` es un test distinto.

---

### 🎥 2. Video explicativo

📌 **\[Espacio para tu video sobre testing]**

> Mostrá:
>
> * Qué es un test unitario
> * Cómo hacer uno a mano
> * Cómo usar `unittest`
> * Qué pasa cuando falla un test
> * Cómo se corre el archivo
> * (Bonus) Cómo hacer tests para funciones que piden `input()` (mocking)

---

### 🔗 3. Links útiles para profundizar

* 📘 [Testing en Python – W3Schools](https://www.w3schools.com/python/python_try_except.asp)
* 🧪 [unittest – Docs oficiales](https://docs.python.org/3/library/unittest.html)
* 📚 [Guía práctica de testing – Real Python (inglés)](https://realpython.com/python-testing/)
* 🧠 [Conceptos de testing para principiantes – Programiz](https://www.programiz.com/python-programming/unittest)

---

### 🚀 4. Mini proyecto

**📄 Proyecto: “Verificador de funciones matemáticas”**

Objetivo: crear y probar funciones con `unittest`.

#### Instrucciones:

1. Escribí tres funciones:

   * `es_par(numero)` → devuelve `True` si el número es par
   * `cuadrado(numero)` → devuelve el cuadrado del número
   * `dividir(a, b)` → devuelve la división (usá try/except para dividir por cero)

2. Escribí una clase de test para cada función usando `unittest`.

#### 💡 Ejemplo esperado:

```python
import unittest

def es_par(n):
    return n % 2 == 0

def cuadrado(n):
    return n ** 2

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"

class TestFunciones(unittest.TestCase):
    def test_es_par(self):
        self.assertTrue(es_par(4))
        self.assertFalse(es_par(5))

    def test_cuadrado(self):
        self.assertEqual(cuadrado(3), 9)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(10, 0), "No se puede dividir por cero")

if __name__ == "__main__":
    unittest.main()
```

> ✨ **Bonus:** Mostrá cómo se ve cuando uno de los tests falla y cómo lo corregís.

---

¿Seguimos con la **Clase 12** (por ejemplo, manejo de módulos o librerías externas como `math`, `random`, o `datetime`) o querés que compile estas 11 clases como PDF, presentación o curso en carpetas? También puedo ayudarte a preparar una clase final con proyecto integrador.
