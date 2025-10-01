# ============================================================
# CLASE 43: Introducción a APIs con requests
# ============================================================
# En esta clase aprenderemos a consumir APIs usando la librería "requests".
# Veremos cómo hacer peticiones GET, POST, PUT, DELETE y cómo manejar
# respuestas en formato JSON con validaciones y manejo de errores.
# ============================================================

import requests

# ------------------------------------------------------------
# 1. Petición GET simple
# ------------------------------------------------------------
# Consigna: Haz una petición GET para obtener los datos de un usuario
# (id=1) desde la API JSONPlaceholder e imprime su nombre y email.
url_user = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url_user)

print("=== EJERCICIO 1: GET simple ===")
if response.status_code == 200:
    user = response.json()
    print("Nombre:", user["name"])
    print("Email:", user["email"])
else:
    print("Error en la petición:", response.status_code)


# ------------------------------------------------------------
# 2. GET con parámetros
# ------------------------------------------------------------
# Consigna: Obtén todas las publicaciones del usuario con userId=1.
# Muestra solo los títulos de las 3 primeras publicaciones.
url_posts = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}
response = requests.get(url_posts, params=params)

print("\n=== EJERCICIO 2: GET con parámetros ===")
if response.status_code == 200:
    posts = response.json()
    for post in posts[:3]:
        print("Título:", post["title"])
else:
    print("Error en la petición:", response.status_code)


# ------------------------------------------------------------
# 3. POST
# ------------------------------------------------------------
# Consigna: Envía un nuevo post usando POST con título y cuerpo.
# La API devuelve el objeto creado con un ID falso.
new_post = {"title": "Post de prueba", "body": "Contenido del post", "userId": 1}
response = requests.post(url_posts, json=new_post)

print("\n=== EJERCICIO 3: POST ===")
if response.status_code == 201:
    created = response.json()
    print("Post creado con ID:", created["id"])
else:
    print("Error en el POST:", response.status_code)


# ------------------------------------------------------------
# 4. PUT
# ------------------------------------------------------------
# Consigna: Modifica (PUT) un post existente (id=1) cambiando su título.
url_put = "https://jsonplaceholder.typicode.com/posts/1"
updated_post = {"id": 1, "title": "Título actualizado", "body": "Texto nuevo", "userId": 1}
response = requests.put(url_put, json=updated_post)

print("\n=== EJERCICIO 4: PUT ===")
if response.status_code == 200:
    print("Post actualizado:", response.json())
else:
    print("Error en el PUT:", response.status_code)


# ------------------------------------------------------------
# 5. DELETE
# ------------------------------------------------------------
# Consigna: Borra (DELETE) un post con id=1 y muestra el código de estado.
url_delete = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url_delete)

print("\n=== EJERCICIO 5: DELETE ===")
print("Código de estado:", response.status_code)


# ------------------------------------------------------------
# 6. Headers en peticiones
# ------------------------------------------------------------
# Consigna: Haz un GET enviando un header personalizado "User-Agent".
url_headers = "https://jsonplaceholder.typicode.com/posts/1"
headers = {"User-Agent": "MiApp/1.0"}
response = requests.get(url_headers, headers=headers)

print("\n=== EJERCICIO 6: Headers ===")
print("Código de estado:", response.status_code)
print("Datos:", response.json())


# ------------------------------------------------------------
# 7. Manejo de errores
# ------------------------------------------------------------
# Consigna: Haz un GET a una URL inexistente y captura el error 404.
url_error = "https://jsonplaceholder.typicode.com/404"
response = requests.get(url_error)

print("\n=== EJERCICIO 7: Manejo de errores ===")
if response.status_code == 404:
    print("Recurso no encontrado (404)")
else:
    print("Respuesta:", response.status_code)


# ------------------------------------------------------------
# 8. Timeout
# ------------------------------------------------------------
# Consigna: Realiza un GET con un tiempo límite (timeout).
url_timeout = "https://jsonplaceholder.typicode.com/users"
print("\n=== EJERCICIO 8: Timeout ===")
try:
    response = requests.get(url_timeout, timeout=3)
    print("Respuesta recibida con éxito")
except requests.exceptions.Timeout:
    print("La petición tardó demasiado")


# ------------------------------------------------------------
# 9. Validación de datos
# ------------------------------------------------------------
# Consigna: Obtén un post y valida que tenga las claves "userId", "id",
# "title" y "body". Si falta alguna, indica un error.
url_post = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url_post)

print("\n=== EJERCICIO 9: Validación de datos ===")
if response.status_code == 200:
    data = response.json()
    expected_keys = {"userId", "id", "title", "body"}
    if expected_keys.issubset(data.keys()):
        print("Post válido:", data)
    else:
        print("Faltan campos en la respuesta")
else:
    print("Error en la petición:", response.status_code)


# ------------------------------------------------------------
# 10. Iteración sobre recursos
# ------------------------------------------------------------
# Consigna: Obtén todos los comentarios de un post (id=1)
# e imprime los 3 primeros correos de los comentaristas.
url_comments = "https://jsonplaceholder.typicode.com/comments"
params = {"postId": 1}
response = requests.get(url_comments, params=params)

print("\n=== EJERCICIO 10: Iteración sobre recursos ===")
if response.status_code == 200:
    comments = response.json()
    for comment in comments[:3]:
        print("Email:", comment["email"])
else:
    print("Error en la petición:", response.status_code)


# ============================================================
# CONCLUSIÓN:
# - Vimos GET, POST, PUT, DELETE con requests.
# - Aprendimos a usar parámetros, headers, validación, timeouts
#   y manejo de errores.
# - Esto nos da las bases para trabajar con cualquier API REST.
# ============================================================
