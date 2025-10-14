from almacenar import cargarDatos, guardarDatos

def buscarTrainer(data, id_trainer):
    for t in data["trainers"]:
        if t["id"] == id_trainer:
            return t
    return None

def trainerRegistro(trainer):
    data = cargarDatos()
    if buscarTrainer(data, trainer["id"]):
        raise ValueError(f"Ya existe un trainer con ID {trainer['id']}")
    trainer.setdefault("rutas", [])
    data["trainers"].append(trainer)
    guardarDatos(data)

def trainerRegistro_input():
    trainer = {
        "id": input("ID trainer: ").strip(),
        "nombres": input("Nombres: ").strip(),
        "apellidos": input("Apellidos: ").strip(),
        "especialidad": input("Especialidad: ").strip(),
        "rutas": []
    }
    trainerRegistro(trainer)
    print("Trainer registrado.")

def mostrarTrainers():
    data = cargarDatos()
    return data.get("trainers", [])

def rutaTrainer(id_trainer, nombre_ruta):
    data = cargarDatos()
    trainer = buscarTrainer(data, id_trainer)
    if not trainer:
        raise ValueError("Trainer no encontrado")
    if nombre_ruta not in trainer["rutas"]:
        trainer["rutas"].append(nombre_ruta)
    guardarDatos(data)