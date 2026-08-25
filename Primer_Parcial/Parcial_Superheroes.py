from super_heroes_data import superheroes
from queue import Queue
from stack import Stack
# Import de list_: Se agregó la importación del list_ para integrar la clase List.
from list_ import List

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

print("EJERCICIO 1")

print("\nLista de 15 superheroes:")
listar_heroes_recursivo(lista_15_heroes)

encontrado = buscar_capitan_america(lista_15_heroes)
if encontrado:
    print("\nSI - Captain America esta en la lista.")
else:
    print("\nNO - Captain America NO esta en la lista.")

# EJERCICIO 2

print("EJERCICIO 2")

# Uso de List: Se reemplazó la lista en el Ejercicio 2 por una instancia de la clase List, usando sus métodos.S
lista_superheroes = List()
lista_superheroes.add_criterion("name", lambda h: h["name"].lower())
lista_superheroes.add_criterion("real_name", lambda h: (h.get("real_name") or "").lower())
lista_superheroes.add_criterion("appearance", lambda h: h["first_appearance"])

for h in superheroes:
    lista_superheroes.append(h)

# 2.1 Listado ordenado de manera ascendente por nombre

print("\n 2.1 Personajes ordenados por nombre (ascendente)")
lista_superheroes.sort_by_criterion("name")
for h in lista_superheroes:
    print(f"  {h['name']}")

# 2.2 Determinar en que posicion estan The Thing y Rocket Raccoon

print("\n 2.2 Posicion de The Thing y Rocket Raccoon")

for personaje in ["the thing", "rocket raccoon"]:
    pos = lista_superheroes.search(personaje, "name")
    if pos is not None:
        print(f"  '{lista_superheroes[pos]['name']}' esta en la posicion {pos + 1}.")
    else:
        print(f"  '{personaje}' no se encontro en la lista.")

# 2.3 Listar todos los villanos

print("\n 2.3 Villanos de la lista")
villanos = [h for h in lista_superheroes if h["is_villain"]]
for v in villanos:
    print(f"  {v['name']} ({v['real_name']})")

# 2.4 Cola de villanos para determinar cuales aparecieron antes de 1980

print("\n 2.4 Villanos en cola -> aparecieron antes de 1980")

cola_villanos = Queue()
for v in villanos:
    cola_villanos.arrive(v)

print("Villanos que aparecieron antes de 1980:")
# Cola no destructiva en 2.4: Se utilizó el método move_to_end() de la clase Queue para poder recorrer los villanos e imprimir las fechas sin borrarlos de la cola.
for _ in range(cola_villanos.size()):
    villano = cola_villanos.move_to_end()
    if villano["first_appearance"] < 1980:
        print(f"    - {villano['name']} ({villano['first_appearance']})")

# 2.5 Heroes que comienzan con Bl, G, My y W

print("\n 2.5 Heroes que comienzan con Bl, G, My y W")
prefijos = ("Bl", "G", "My", "W")
for h in lista_superheroes:
    if h["name"].startswith(prefijos):
        print(f"  {h['name']}")

# 2.6 Listado por nombre real de manera ascendente

print("\n 2.6 Personajes ordenados por nombre real (ascendente)")
lista_superheroes.sort_by_criterion("real_name")
for h in lista_superheroes:
    print(f"  {h['name']} -> {h['real_name']}")

# 2.7 Superheroes ordenados por fecha de aparicion

print("\n 2.7 Superheroes ordenados por fecha de aparicion")
lista_superheroes.sort_by_criterion("appearance")
for h in lista_superheroes:
    if not h["is_villain"]:
        print(f"  {h['first_appearance']} - {h['name']}")

# 2.8 Modificar el nombre real de Ant Man a Scott Lang

print("\n 2.8 Modificar nombre real de Ant Man a Scott Lang")
pos_antman = lista_superheroes.search("ant man", "name")
if pos_antman is not None:
    h = lista_superheroes[pos_antman]
    print(f"  Antes:  real_name = '{h['real_name']}'")
    h["real_name"] = "Scott Lang"
    print(f"  Despues: real_name = '{h['real_name']}'")

# 2.9 Personajes cuya biografia incluya 'time-traveling' o 'suit'

print("\n 2.9 Personajes con 'time-traveling' o 'suit' en su biografia")
palabras_clave = ["time-traveling", "suit"]
for h in lista_superheroes:
    bio = h["short_bio"].lower()
    encontradas = [p for p in palabras_clave if p in bio]
    if encontradas:
        print(f"  {h['name']} -> palabras encontradas: {encontradas}")
        print(f"    Bio: {h['short_bio']}")

# 2.10 Eliminar a Electro y Baron Zemo de la lista

print("\n 2.10 Eliminar Electro y Baron Zemo de la lista")
a_eliminar = ["electro", "baron zemo"]
for nombre in a_eliminar:
    eliminado = lista_superheroes.delete_value(nombre, "name")
    if eliminado:
        print(f"  '{eliminado['name']}' eliminado. Informacion:")
        for clave, valor in eliminado.items():
            print(f"    {clave}: {valor}")
    else:
        print(f"  '{nombre}' no estaba en la lista.")

print(f"\n  Total de personajes tras las eliminaciones: {lista_superheroes.size()}")

# Devolucion del primer parcial, el ejercicio 1 esta como antes y ya aplique las correcicones correspondientes con clases List, Queue y Stack.