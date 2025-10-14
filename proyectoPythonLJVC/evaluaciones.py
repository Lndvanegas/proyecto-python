from almacenar import cargarDatos, guardarDatos
from campers import actualizarEstado, camperRiesggo


def validarN(n):
    if not isinstance(n, (int, float)):
        raise ValueError("la nota debe ser un numero")
    if n < 0 or n > 100:
        raise ValueError("nota invalida (0-100)")

def notaExIn(camperId, teorica, practica):
    validarN(teorica); validarN(practica)
    promedio = (practica + teorica) / 2
    data = cargarDatos()
    data["evaluaciones"].append({
        "camperId": camperId,
        "tipo": "examen_inicial",
        "teorica": teorica,
        "practica": practica,
        "promedio": promedio
    })
    if promedio >= 60:
        actualizarEstado(camperId, "Aprobado")
    guardarDatos(data)
    return promedio

def notaModulo(camperId, modulo, teorica, practica, quices):
    validarN(teorica); validarN(practica); validarN(quices)
    
    nota_final = teorica * 0.3 + practica * 0.6 + quices * 0.1
    data = cargarDatos()
    data["evaluaciones"].append({
        "camperId": camperId,
        "tipo": "modulo",
        "modulo": modulo,
        "nota_final": nota_final
    })
    guardarDatos(data)
    
    
    if nota_final < 60:
        camperRiesggo(camperId, "Alto")
        print(f"Camper {camperId} ha quedado en Riesgo Alto por nota de modulo ({nota_final:.2f}).")
    
    return nota_final

def mostrarNotCamp(camperId):
    data = cargarDatos()
    return [e for e in data["evaluaciones"] if e["camperId"] == camperId]