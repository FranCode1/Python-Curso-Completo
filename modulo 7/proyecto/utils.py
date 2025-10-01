import json
import requests
from db import listar_tareas

def exportar_json(nombre_archivo="tareas.json"):
    tareas = listar_tareas()
    data = [{"id": t[0], "titulo": t[1], "estado": t[2]} for t in tareas]
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ Tareas exportadas a {nombre_archivo}")

def obtener_frase_motivacional():
    try:
        resp = requests.get("https://api.quotable.io/random", timeout=5)
        if resp.status_code == 200:
            return resp.json()["content"]
    except Exception:
        return "Sigue adelante, ¡puedes lograrlo!"
