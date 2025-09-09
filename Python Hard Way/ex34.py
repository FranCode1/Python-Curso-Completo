# Importa librerías necesarias
import random                      # Para seleccionar elementos aleatorios
from urllib.request import urlopen # Para leer palabras desde una URL
import sys                         # Para leer argumentos desde la consola

# URL donde se encuentran las palabras para usar en los ejercicios
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []  # Lista que guardará las palabras descargadas

# Diccionario con patrones de código como claves, y sus explicaciones como valores
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# Verifica si el usuario pasó "english" como argumento en consola
# Si lo hizo, mostrará la descripción en inglés primero (en vez del código)
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# Carga las palabras desde la URL y las guarda en la lista WORDS
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))


# Función que toma un fragmento de código y su frase asociada
# y reemplaza los marcadores especiales por palabras aleatorias
def convert(snippet, phrase):
    # Reemplaza %%% por nombres de clases (con mayúscula inicial)
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    
    # Reemplaza *** por nombres de variables o funciones
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []      # Guarda los resultados finales
    param_names = []  # Guarda listas de parámetros (para @@@)

    # Por cada @@@ genera una lista de 1 a 3 nombres de parámetros aleatorios
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    # Aplica reemplazos tanto al código como a su explicación
    for sentence in snippet, phrase:
        result = sentence[:]

        # Reemplaza %%% con nombres de clase
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # Reemplaza *** con nombres de funciones/variables
        for word in other_names:
            result = result.replace("***", word, 1)

        # Reemplaza @@@ con listas de parámetros
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# Bucle principal: se repite hasta que el usuario presione CTRL+D (EOF)
try:
    while True:
        # Toma todos los patrones de código, los mezcla aleatoriamente
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        # Por cada patrón:
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)

            # Si el usuario pidió primero el texto en inglés, se invierte
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            # Espera que el usuario presione Enter (sirve como pausa)
            input("> ")
            print(f"ANSWER:  {answer}\n\n")

# Si se detecta EOF (CTRL+D), se termina el programa
except EOFError:
    print("\nBye")
