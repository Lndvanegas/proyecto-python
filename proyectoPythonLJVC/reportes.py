from almacenar import cargarDatos

def campersIncritos():
    data = cargarDatos()
    return [c for c in data["campers"] if c.get("estado") == "Inscrito"]

def campersAprobados():
    data = cargarDatos()
    return [c for c in data["campers"] if c.get("estado") == "Aprobado"]

def trainersActivos():
    data = cargarDatos()
    return data["trainers"]

def campersBajoR():
    data = cargarDatos()
    ids_bajo = set()
    for e in data["evaluaciones"]:
        if e.get("tipo") == "modulo" and e.get("nota_final", 0) < 60:
            ids_bajo.add(e["id_camper"])
    return [c for c in data["campers"] if c["id"] in ids_bajo]


def campersAltoR():
    data = cargarDatos()
    
    return [c for c in data["campers"] if c.get("riesgo") == "Alto"]


def trainerRutaCamper(nombre_ruta):
    data = cargarDatos()
    
    campers_en_ruta = []
    for ruta in data.get("rutas", []):
        if ruta["nombre"].lower() == nombre_ruta.lower():
            for id_camper in ruta["campers"]:
                
                camper_data = next((c for c in data["campers"] if c["id"] == id_camper), None)
                if camper_data:
                    campers_en_ruta.append(camper_data)
            break
    
    
    trainers_en_ruta = [
        t for t in data.get("trainers", []) 
        if nombre_ruta.lower() in [r.lower() for r in t.get("rutas", [])]
    ]

    print(f"\n--- CAMPERS en la Ruta '{nombre_ruta}' ---")
    if campers_en_ruta:
        for c in campers_en_ruta: print(c)
    else:
        print("No hay campers asignados a esta ruta.")

    print(f"\nㅤㅤㅤㅤTRAINERS en la Ruta '{nombre_ruta}'ㅤㅤㅤㅤ")
    if trainers_en_ruta:
        for t in trainers_en_ruta: print(t)
    else:
        print("No hay trainers asignados a esta ruta.")


def reporte_modulos_aprobados_perdidos(nombre_ruta):
    data = cargarDatos()
    
    
    modulos_ruta = []
    for r in data.get("rutas", []):
        if r["nombre"].lower() == nombre_ruta.lower():
            modulos_ruta = r.get("modulos", [])
            break
    
    if not modulos_ruta:
        print(f"Ruta '{nombre_ruta}' no encontrada o sin modulos.")
        return

    
    matriculas_ruta = [m for m in data.get("matriculas", []) if m["ruta"].lower() == nombre_ruta.lower()]
    
    resultados_modulos = {}
    for modulo in modulos_ruta:
        resultados_modulos[modulo] = {"Aprobados": 0, "Perdidos": 0, "Por Trainer": {}}

    
    for e in data.get("evaluaciones", []):
        if e.get("tipo") == "modulo" and e["modulo"] in modulos_ruta:
            nota = e.get("nota_final", 0)
            id_camper = e["id_camper"]
            matricula = next((m for m in matriculas_ruta if m["id_camper"] == id_camper), None)

            if matricula:
                id_trainer = matricula["id_trainer"]
                
                estado = "Aprobados" if nota >= 60 else "Perdidos"
                resultados_modulos[e["modulo"]][estado] += 1
                
                
                if id_trainer not in resultados_modulos[e["modulo"]]["Por Trainer"]:
                    resultados_modulos[e["modulo"]]["Por Trainer"][id_trainer] = {"Aprobados": 0, "Perdidos": 0}
                
                resultados_modulos[e["modulo"]]["Por Trainer"][id_trainer][estado] += 1

    print(f"\nㅤㅤㅤㅤRESULTADOS DE MÓDULOS para la Ruta '{nombre_ruta}'ㅤㅤㅤㅤ")
    for modulo, resultados in resultados_modulos.items():
        print(f"\n Modulo: {modulo}")
        print(f"Aprobados (Total): {resultados['Aprobados']}")
        print(f"Perdidos (Total): {resultados['Perdidos']}")
        print(f"Detalle por Trainer:")
        if resultados["Por Trainer"]:
            for trainer, res in resultados["Por Trainer"].items():
                print(f"Trainer {trainer}: Aprobados={res['Aprobados']}, Perdidos={res['Perdidos']}")
        else:
            print("No hay evaluaciones registradas con matrícula completa para este modulo")