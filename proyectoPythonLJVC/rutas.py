from almacenar import cargarDatos, guardarDatos

def mostrarRutas():
    data = cargarDatos()
    return data.get("rutas", [])

def asignarRCamper(camperId, nombre_ruta):
    data = cargarDatos()
    for ruta in data["rutas"]:
        if ruta["nombre"].lower() == nombre_ruta.lower():
            if camperId not in ruta["campers"]:
                ruta["campers"].append(camperId)
                guardarDatos(data)
                print("Camper asignado a la ruta")
                return
    raise ValueError("Ruta no encontrada.")