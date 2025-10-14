from almacenar import cargarDatos, guardarDatos

VALID_ESTADOS = ["En proceso", "Inscrito", "Aprobado", "Cursando", "Graduado", "Expulsado", "Retirado"]

def encontraCamper(data, camperId):
    for c in data["campers"]:
        if c["id"] == camperId:
            return c
    return None

def registrarCamper(camper):
    data = cargarDatos()
    if encontraCamper(data, camper["id"]):
        raise ValueError(f"Ya existe un camper con ID {camper['id']}")
    data["campers"].append(camper)
    guardarDatos(data)

def registrarCamperInteractivo():
    camper = {
        "id": input("ID: ").strip(),
        "nombres": input("Nombres: ").strip(),
        "apellidos": input("Apellidos: ").strip(),
        "direccion": input("Direccion: ").strip(),
        "acudiente": input("Acudiente: ").strip(),
        "telefono_celular": input("Telefono celular: ").strip(),
        "telefono_fijo": input("Telefono fijo: ").strip(),
        "estado": "Inscrito",
        "riesgo": "Bajo"
    }
    registrarCamper(camper)
    print("Camper registrado con exito")

def mostrarCampers():
    data = cargarDatos()
    return data.get("campers", [])

def consultarCamper(estado):
    data = cargarDatos()
    return [c for c in data["campers"] if c.get("estado", "").lower() == estado.lower()]

def actualizarEstado(camperId, nuevo_estado):
    if nuevo_estado not in VALID_ESTADOS:
        raise ValueError("Estado invalido.")
    data = cargarDatos()
    camper = encontraCamper(data, camperId)
    if not camper:
        raise ValueError("Camper no encontrado")
    camper["estado"] = nuevo_estado
    guardarDatos(data)

def camperRiesggo(camperId, nivel_riesgo):
    data = cargarDatos()
    camper = encontraCamper(data, camperId)
    if not camper:
        raise ValueError("Camper no encontrado")
    camper["riesgo"] = nivel_riesgo
    guardarDatos(data)