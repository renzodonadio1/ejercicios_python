import random

cabina = []
cabina2 = []
cabina3 = []

vehiculo = {    
    "auto": 47,
    "camioneta": 59,
    "camion": 71,
    "colectivo" : 64    
}

for i in range(30):
    tipo = random.choice(list(vehiculo.keys()))
    cabina = random.choice([cabina, cabina2, cabina3])

    cabina.append(tipo)

recaudacion = [0, 0, 0]

conteo = [
    {"auto": 0, "camioneta": 0, "camion": 0, "colectivo": 0},
    {"auto": 0, "camioneta": 0, "camion": 0, "colectivo": 0},
    {"auto": 0, "camioneta": 0, "camion": 0, "colectivo": 0}
]

cabinas = [cabina, cabina2, cabina3]

for i in range(3):
    while cabinas[i]:
        vehiculo_tipo = cabinas[i].pop()
        recaudacion[i] += vehiculo[vehiculo_tipo]
        conteo[i][vehiculo_tipo] += 1

for i in range(3):
     print(f"Cabina {i+1}: ${recaudacion[i]}")


     
mayor = max(recaudacion)
pos = recaudacion.index(mayor)
print(f"la cabina {pos+1} recaudo mas: ${mayor}")

for i in range(3):
    print(f"\nCabina {i+1}:")

    for tipo in conteo[i]:
        print(f"{tipo}: {conteo[i][tipo]}")
