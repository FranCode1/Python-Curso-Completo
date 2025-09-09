# Se define una excepción personalizada para errores del parser
class ParserError(Exception):
    pass

# Clase que representa una oración con sujeto, verbo y objeto
class Sentence(object):
    def __init__(self, subject, verb, obj):
        # Cada uno es una tupla como ('noun', 'princess'), y aquí se toma solo el valor
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

# Funciones auxiliares para el análisis de la oración:

# Mira el tipo de la primera palabra sin eliminarla
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

# Intenta emparejar el primer tipo de palabra con el esperado
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

# Salta todas las palabras de tipo "stop"
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

# Extrae el verbo de la lista de palabras
def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

# Extrae el objeto (sustantivo o dirección) de la lista
def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

# Extrae el sujeto de la oración; si empieza por verbo, asume sujeto implícito 'player'
def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a noun or verb next.")

# Analiza la lista de palabras y crea una instancia de Sentence
def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
