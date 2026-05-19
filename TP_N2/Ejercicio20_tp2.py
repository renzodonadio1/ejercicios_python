pila = []

pila.append(("norte", 3))
pila.append(("este", 2))
pila.append(("sur", 1))

opuestos = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste"
}

print("Camino de regreso:")

while pila:

    direccion, pasos = pila.pop()

    print(opuestos[direccion], pasos)