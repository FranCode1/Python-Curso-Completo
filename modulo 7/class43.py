# ============================================================
# CLASE 43: Introducción a APIs con requests
# ============================================================
# En esta clase aprenderemos a consumir APIs usando la librería "requests".
# Veremos cómo hacer peticiones GET, POST y cómo manejar respuestas en formato JSON.
# ============================================================

import requests

# ------------------------------------------------------------
# 1. Petición GET simple
# ------------------------------------------------------------
# Ejemplo: obtener información de un usuario desde la API de JSONPlaceholder
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

print("=== GET ===")
if response.status_code == 200:
    data = response.json()
    print("Nombre:", data["name"])
    print("Email:", data["email"])
else:
    print("Error en la petición:", response.status_code)


# ------------------------------------------------------------
# 2. Petición GET con parámetros
# ------------------------------------------------------------
# Ejemplo: obtener publicaciones de un usuario
url_posts = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}
response_posts = requests.get(url_posts, params=params)

print("\n=== GET con parámetros ===")
if response_posts.status_code == 200:
    posts = response_posts.json()
    for post in posts[:3]:  # Mostramos solo los 3 primeros
        print(f"Título: {post['title']}")
else:
    print("Error en la petición:", response_posts.status_code)


# ------------------------------------------------------------
# 3. Petición POST
# ------------------------------------------------------------
# Ejemplo: enviar un nuevo post (aunque en JSONPlaceholder no se guarda realmente)
new_post = {
    "title": "Mi primer post con requests",
    "body": "Este es un ejemplo de envío con POST",
    "userId": 1
}
response_post = requests.post(url_posts, json=new_post)

print("\n=== POST ===")
if response_post.status_code == 201:
    created_post = response_post.json()
    print("Post creado con ID:", created_post["id"])
else:
    print("Error en el POST:", response_post.status_code)


# ------------------------------------------------------------
# 4. Manejo de errores y timeouts
# ------------------------------------------------------------
print("\n=== Manejo de errores ===")
try:
    response_error = requests.get("https://jsonplaceholder.typicode.com/404", timeout=5)
    if response_error.status_code == 404:
        print("Recurso no encontrado (404)")
except requests.exceptions.Timeout:
    print("La petición tardó demasiado")
except requests.exceptions.RequestException as e:
    print("Error en la petición:", e)


# ------------------------------------------------------------
# CONCLUSIÓN:
# - requests facilita la interacción con APIs.
# - Aprendimos GET, POST, parámetros y manejo de errores.
# ============================================================
