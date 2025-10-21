import json
import os

REPORTE = "reporte_bajo_rendimiento.json"

def inicialEstructura():
    
        return{
            "campers": [],
        }


def cargarDatos(nombre_archivo=REPORTE):
    
    if not os.path.exists(nombre_archivo):
        datos = inicialEstructura()
        guardarDatos(datos, nombre_archivo)
        return datos
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            datos = inicialEstructura()
            guardarDatos(datos, nombre_archivo)
            return datos

def guardarDatos(data, nombre_archivo=REPORTE):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def campersBajoR():
    data = cargarDatos()
    ids_bajo = set()
    for e in data["evaluaciones"]:
        if e.get("tipo") == "modulo" and e.get("nota_final", 0) < 60:
            ids_bajo.add(e["id_camper"])
    return [c for c in data["campers"] if c["id"] in ids_bajo]
