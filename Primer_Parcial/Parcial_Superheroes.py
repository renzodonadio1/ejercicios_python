from super_heroes_data import superheroes
from queue import Queue
from stack import Stack

# EJER 1

lista_15_heroes = [
    "Iron Man",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Captain America",
    "Spiderman",
    "Wolverine",
    "Cyclops",
    "Storm",
    "Daredevil",
    "Black Panther",
    "Deadpool",
    "Gamora",
    "Silver Surfer"
]

def buscar_capitan_america(lista, indice=0):

    if indice >= len(lista):
        return False
    if lista[indice] == "Captain America":
        return True
    return buscar_capitan_america(lista, indice + 1)


def listar_heroes_recursivo(lista, indice=0):
   
    if indice >= len(lista):
        return
    print(f"  [{indice + 1}] {lista[indice]}")
    listar_heroes_recursivo(lista, indice + 1)


# Ejer 1
print("=" * 60)
print("EJERCICIO 1")
print("=" * 60)

print("\nLista de 15 superheroes:")
listar_heroes_recursivo(lista_15_heroes)

encontrado = buscar_capitan_america(lista_15_heroes)
if encontrado:
    print("\n✔ Captain America SI esta en la lista.")
else:
    print("\n✘ Captain America NO esta en la lista.")


# EJERCICIO 2

print("\n" + "=" * 60)
print("EJERCICIO 2")
print("=" * 60)

# 2.1 Listado ordenado de manera ascendente por nombre

print("\n--- 2.1 Personajes ordenados por nombre (ascendente) ---")
ordenados_por_nombre = sorted(superheroes, key=lambda h: h["name"].lower())
for h in ordenados_por_nombre:
    print(f"  {h['name']}")

# 2.2 Determinar en que posicion estan The Thing y Rocket Raccoon

print("\n--- 2.2 Posicion de The Thing y Rocket Raccoon ---")

def buscar_posicion(lista, nombre, indice=0):
    if indice >= len(lista):
        return -1
    if lista[indice]["name"].lower() == nombre.lower():
        return indice + 1 
    return buscar_posicion(lista, nombre, indice + 1)

for personaje in ["The Thing", "Rocket Raccoon"]:
    pos = buscar_posicion(superheroes, personaje)
    if pos != -1:
        print(f"  '{personaje}' esta en la posicion {pos} de la lista original.")
    else:
        print(f"  '{personaje}' no se encontro en la lista.")

# 2.3 Listar todos los villanos

print("\n--- 2.3 Villanos de la lista ---")
villanos = [h for h in superheroes if h["is_villain"]]
for v in villanos:
    print(f"  {v['name']} ({v['real_name']})")

# 2.4 Cola de villanos para determinar cuales aparecieron antes de 1980

print("\n--- 2.4 Villanos en cola -> aparecieron antes de 1980 ---")

cola_villanos = Queue()
for v in villanos:
    cola_villanos.arrive(v)

print("  Villanos que aparecieron antes de 1980:")
while cola_villanos.size() > 0:
    villano = cola_villanos.attention()
    if villano["first_appearance"] < 1980:
        print(f"    - {villano['name']} ({villano['first_appearance']})")

# 2.5 Heroes que comienzan con Bl, G, My y W

print("\n--- 2.5 Heroes que comienzan con Bl, G, My y W ---")
prefijos = ("Bl", "G", "My", "W")
for h in superheroes:
    if h["name"].startswith(prefijos):
        print(f"  {h['name']}")

# 2.6 Listado por nombre real de manera ascendente

print("\n--- 2.6 Personajes ordenados por nombre real (ascendente) ---")
ordenados_por_nombre_real = sorted(
    superheroes,
    key=lambda h: (h["real_name"] or "").lower()
)
for h in ordenados_por_nombre_real:
    print(f"  {h['name']} -> {h['real_name']}")

# 2.7 Superheroes ordenados por fecha de aparicion

print("\n--- 2.7 Superheroes ordenados por fecha de aparicion ---")
heroes_no_villanos = [h for h in superheroes if not h["is_villain"]]
heroes_por_fecha = sorted(heroes_no_villanos, key=lambda h: h["first_appearance"])
for h in heroes_por_fecha:
    print(f"  {h['first_appearance']} - {h['name']}")

# 2.8 Modificar el nombre real de Ant Man a Scott Lang

print("\n--- 2.8 Modificar nombre real de Ant Man a Scott Lang ---")
for h in superheroes:
    if h["name"] == "Ant Man":
        print(f"  Antes:  real_name = '{h['real_name']}'")
        h["real_name"] = "Scott Lang"
        print(f"  Despues: real_name = '{h['real_name']}'")
        break

# 2.9 Personajes cuya biografia incluya 'time-traveling' o 'suit'

print("\n--- 2.9 Personajes con 'time-traveling' o 'suit' en su biografia ---")
palabras_clave = ["time-traveling", "suit"]
for h in superheroes:
    bio = h["short_bio"].lower()
    encontradas = [p for p in palabras_clave if p in bio]
    if encontradas:
        print(f"  {h['name']} -> palabras encontradas: {encontradas}")
        print(f"    Bio: {h['short_bio']}")

# 2.10 Eliminar a Electro y Baron Zemo de la lista

print("\n--- 2.10 Eliminar Electro y Baron Zemo ---")
a_eliminar = ["Electro", "Baron Zemo"]
for nombre in a_eliminar:
    eliminado = None
    for i, h in enumerate(superheroes):
        if h["name"] == nombre:
            eliminado = superheroes.pop(i)
            break
    if eliminado:
        print(f"  '{nombre}' eliminado. Informacion:")
        for clave, valor in eliminado.items():
            print(f"    {clave}: {valor}")
    else:
        print(f"  '{nombre}' no estaba en la lista.")

print(f"\n  Total de personajes tras las eliminaciones: {len(superheroes)}")
