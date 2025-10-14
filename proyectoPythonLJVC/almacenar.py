import json
import os

ARCHIVO = "data.json"

def inicialEstructura():
    
    return {
        "campers": [],
        "trainers": [],
        "rutas": [
            {"nombre": "Fundamentos", "modulos": ["Python Basico", "Logica"], "campers": []},
            {"nombre": "Backend", "modulos": ["Bases de Datos"], "campers": []},
            {"nombre": "Frontend", "modulos": ["HTML", "CSS", "JavaScript"], "campers": []}
        ],
        "areas": [
            
            {"nombre": "Desarrollo Web", "capacidad": 33, "campers": []},
            {"nombre": "Desarrollo Movil", "capacidad": 33, "campers": []},
            {"nombre": "Desarrollo de Videojuegos", "capacidad": 33, "campers": []}
        ],
        "matriculas": [],
        "evaluaciones": [],
        "usuarios": [
            {"usuario": "coordinador", "clave": "0258", "rol": "coordinador"},
            {"usuario": "trainer", "clave": "8520", "rol": "trainer"},
            {"usuario": "camper", "clave": "campus2023", "rol": "camper"}
        ]
    }

def cargarDatos(nombre_archivo=ARCHIVO):
    
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

def guardarDatos(data, nombre_archivo=ARCHIVO):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)