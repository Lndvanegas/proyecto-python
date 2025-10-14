from almacenar import cargarDatos, guardarDatos

def validarCA(area):
    return len(area.get("campers", [])) < area.get("capacidad", 0)

def asignarCA(camperId, nombre_area):
    data = cargarDatos()
    for i in data["areas"]:
        if i["nombre"].lower() == nombre_area.lower():
            if not validarCA(i):
                raise ValueError("Área sin capacidad disponible.")
            if camperId not in i["campers"]:
                i["campers"].append(camperId)
                guardarDatos(data)
                print("Camper asignado al area")
                return
    raise ValueError("Área no encontrada.")

def mostrarAreas():
    data = cargarDatos()
    return data.get("areas", [])