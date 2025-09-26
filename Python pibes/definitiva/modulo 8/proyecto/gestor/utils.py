import json
import csv
from db import DBManager

def exportar_json(nombre_archivo="tareas.json"):
    db = DBManager()
    tareas = db.obtener_tareas()
    data = [
        {"id": t[0], "titulo": t[1], "descripcion": t[2], "estado": t[3], "fecha": t[4]}
        for t in tareas
    ]
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ Exportado a {nombre_archivo}")

def exportar_csv(nombre_archivo="tareas.csv"):
    db = DBManager()
    tareas = db.obtener_tareas()
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "titulo", "descripcion", "estado", "fecha"])
        writer.writerows(tareas)
    print(f"✅ Exportado a {nombre_archivo}")
