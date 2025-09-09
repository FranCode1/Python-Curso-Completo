# ---------- STRINGS Y VARIABLES DE TEXTO ----------

# Guardamos diferentes mensajes como texto (strings)
message1 = "Hello Python World!"
message2 = 'Hello Python Crash Course Reader!'
message3 = 'This is a string.'
message4 = 'This is also a string.'

# ---------- MANIPULACIÓN DE STRINGS ----------

# Guardamos nombre completo separado y luego lo unimos
name = 'ada lovelace'
first_name = 'ada'
last_name = 'lovelace'

# Creamos el nombre completo usando una f-string
full_name = f'{first_name} {last_name}'

# Creamos un saludo con formato capitalizado
message5 = f'Hello, {full_name.title()}!'

# ---------- MÉTODOS DE STRINGS ----------

# Remueve el prefijo 'https://' de una URL
nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')

# Un mensaje que incluye una comilla interna
message6 = "One of Python's strengths is its diverse community."

# ---------- NÚMEROS Y CONSTANTES ----------

# Variable con separadores visuales para miles (14 mil millones)
universe_age = 14_000_000_000

# Asignación múltiple de variables a cero
x, y, z = 0, 0, 0

# Constante escrita en mayúsculas por convención
MAX_CONNECTIONS = 500

# ---------- COMENTARIOS ----------

# Say hello to everyone, this is a comment (esto no se ejecuta)

# ---------- IMPRESIÓN DE RESULTADOS ----------

print(message1)                          # Muestra el mensaje1
print(full_name)                         # Muestra el nombre completo en minúsculas
print(name.title())                      # Capitaliza cada palabra del nombre
print(name.upper())                      # Convierte todo a mayúsculas
print(name.lower())                      # Convierte todo a minúsculas
print(f'Hello, {full_name.title()}!')    # Saludo con el nombre completo capitalizado
print(message5)                          # Imprime el mensaje5 ya creado
print(message6)                          # Mensaje con apóstrofe
print(universe_age)                      # Imprime la edad del universo
