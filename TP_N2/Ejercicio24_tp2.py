pila = []

pila.append(("Iron Man", 10))
pila.append(("Groot", 6))
pila.append(("Rocket Raccoon", 7))
pila.append(("Black Widow", 8))
pila.append(("Captain America", 9))
pila.append(("Doctor Strange", 4))

posicion = 1

for personaje in reversed(pila):

    nombre, peliculas = personaje

    if nombre == "Rocket Raccoon" or nombre == "Groot":

        print(nombre, "está en la posición", posicion)

    posicion += 1

print("\nMás de 5 películas:")

for personaje in pila:

    nombre, peliculas = personaje

    if peliculas > 5:

        print(nombre, "-", peliculas)

for personaje in pila:

    nombre, peliculas = personaje

    if nombre == "Black Widow":

        print("\nBlack Widow participó en", peliculas, "películas")

print("\nEmpiezan con C, D o G:")

for personaje in pila:

    nombre, peliculas = personaje

    if nombre[0] == "C" or nombre[0] == "D" or nombre[0] == "G":

        print(nombre)