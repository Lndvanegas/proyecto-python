from almacenar import cargarDatos, guardarDatos
from campers import encontraCamper 
from trainers import buscarTrainer 

def crearMatricula(camperId, ruta, area, id_trainer, fecha_inicio, fecha_fin):
    data = cargarDatos()
    camper = encontraCamper(data, camperId)
    trainer = buscarTrainer(data, id_trainer)

    
    if not camper:
        raise ValueError("Camper no encontrado.")
    if camper.get("estado") != "Aprobado":
        raise ValueError(f"El camper debe estar en estado 'Aprobado' para matricularse. Estado actual: {camper.get('estado')}")

    
    if not trainer:
        raise ValueError("Trainer no encontrado.")
    if ruta.lower() not in [r.lower() for r in trainer.get("rutas", [])]:
        raise ValueError(f"El Trainer {id_trainer} no está asignado a la ruta {ruta}.")

    
    
    
    matricula = {
        "camperId": camperId,
        "ruta": ruta,
        "area": area,
        "id_trainer": id_trainer, 
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin 
    }
    data["matriculas"].append(matricula)
    
    
    camper["estado"] = "Cursando"

    guardarDatos(data)
    print("Matricula creada y camper actualizado a 'Cursando'")

def mostrarMatriculas():
    data = cargarDatos()
    return data.get("matriculas", [])