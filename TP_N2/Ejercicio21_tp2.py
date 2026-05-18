despegues = []
aterrizajes = []

vuelo = {
    "empresa": "Aerolineas",
    "hora_de_salida": 10,
    "hora_de_llegada": 12,
    "origen": "Cordoba",
    "destino": "Buenos Aires",
    "tipo": "pasajeros"
}

despegues.append(vuelo)

aterrizajes.append({
    "empresa": "Latam",
    "hora_de_llegada": 11,
    "origen": "Chile",
    "destino": "Buenos Aires",
    "tipo": "carga"
})

tiempos = {
    "pasajeros": {"aterrizaje": 10, "despegue": 5},
    "negocios": {"aterrizaje": 5, "despegue": 3},
    "carga": {"aterrizaje": 12, "despegue": 9}
}

while aterrizajes or despegues:

    if aterrizajes:

        vuelo_aterrizaje = aterrizajes.pop(0)

        tiempo_aterrizaje = tiempos[vuelo_aterrizaje["tipo"]]["aterrizaje"]

        print(f"Vuelo de {vuelo_aterrizaje['empresa']} aterrizando.")
        print(f"Tiempo: {tiempo_aterrizaje} minutos")

    elif despegues:

        vuelo_despegue = despegues.pop(0)

        tiempo_despegue = tiempos[vuelo_despegue["tipo"]]["despegue"]

        print(f"Vuelo de {vuelo_despegue['empresa']} despegando.")
        print(f"Tiempo: {tiempo_despegue} minutos")