# ----------------------------------------
# 📚 PROYECTO MÓDULO 4: SISTEMA DE BIBLIOTECA
# ----------------------------------------

# ==========================
# 🔹 CLASES Y OBJETOS
# ==========================

class Libro:
    def __init__(self, titulo, autor, isbn, stock=1):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.__stock = stock  # encapsulado

    # Encapsulamiento con propiedades
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, cantidad):
        if cantidad >= 0:
            self.__stock = cantidad
        else:
            raise ValueError("El stock no puede ser negativo")

    def __str__(self):
        return f"{self.titulo} de {self.autor} (ISBN: {self.isbn})"

    # Operator overloading: comparar libros por ISBN
    def __eq__(self, other):
        return self.isbn == other.isbn

    def __hash__(self):
        return hash(self.isbn)


# ==========================
# 🔹 HERENCIA Y POLIMORFISMO
# ==========================

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def puede_prestar(self):
        """Por defecto, 3 libros"""
        return len(self.libros_prestados) < 3

    def __str__(self):
        return f"Usuario: {self.nombre}"


class Estudiante(Usuario):
    def puede_prestar(self):
        """Estudiante puede prestar hasta 5 libros"""
        return len(self.libros_prestados) < 5


class Profesor(Usuario):
    def puede_prestar(self):
        """Profesor puede prestar libros ilimitados"""
        return True


# ==========================
# 🔹 METACLASES
# ==========================

class ModeloMeta(type):
    def __new__(cls, name, bases, attrs):
        if "id" not in attrs and name != "BaseModel":
            raise TypeError(f"La clase {name} debe tener un atributo 'id'")
        return super().__new__(cls, name, bases, attrs)


class BaseModel(metaclass=ModeloMeta):
    pass


class RegistroLibro(BaseModel):
    id = 0
    # cumple con la metaclase


# ==========================
# 🔹 BIBLIOTECA
# ==========================

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = []

    # Operator overloading: sumar libros
    def __add__(self, libro: Libro):
        if libro.isbn in self.libros:
            self.libros[libro.isbn].stock += 1
        else:
            self.libros[libro.isbn] = libro
        return self

    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, usuario: Usuario, isbn: str):
        if isbn not in self.libros:
            print("❌ Libro no encontrado")
            return
        libro = self.libros[isbn]
        if libro.stock > 0 and usuario.puede_prestar():
            libro.stock -= 1
            usuario.libros_prestados.append(libro)
            print(f"📖 {usuario.nombre} tomó prestado '{libro.titulo}'")
        else:
            print("⚠️ No se puede prestar el libro")

    def mostrar_libros(self):
        for libro in self.libros.values():
            print(f"- {libro} | Stock: {libro.stock}")


# ==========================
# 🔹 METAPROGRAMACIÓN
# ==========================

def inspeccionar_objeto(obj):
    print(f"\n🔎 Inspeccionando {obj}:")
    print("Atributos:", dir(obj))
    if hasattr(obj, "__dict__"):
        print("Diccionario interno:", obj.__dict__)
    if hasattr(obj, "__str__"):
        print("Método __str__ encontrado ->", obj.__str__())


# ==========================
# 🧪 DEMO DEL SISTEMA
# ==========================

def main():
    # Crear libros
    libro1 = Libro("1984", "George Orwell", "123")
    libro2 = Libro("Fundación", "Isaac Asimov", "456", stock=2)

    # Crear usuarios
    est = Estudiante("Ana")
    prof = Profesor("Carlos")

    # Crear biblioteca
    biblio = Biblioteca()
    biblio + libro1
    biblio + libro2
    biblio + libro2  # sumar otro ejemplar

    biblio.registrar_usuario(est)
    biblio.registrar_usuario(prof)

    print("\n📚 Catálogo inicial:")
    biblio.mostrar_libros()

    # Préstamos
    biblio.prestar_libro(est, "123")
    biblio.prestar_libro(prof, "456")

    print("\n📚 Catálogo después de préstamos:")
    biblio.mostrar_libros()

    # Metaprogramación
    inspeccionar_objeto(est)
    inspeccionar_objeto(libro1)

if __name__ == "__main__":
    main()
