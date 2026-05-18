cola = [
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitan America", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"}
]

for personaje in cola:

    if personaje["superheroe"] == "Capitana Marvel":

        print("Capitana Marvel es:", personaje["personaje"])


print("\nsuperheroes femeninos:")

for personaje in cola:

    if personaje["genero"] == "F":

        print(personaje["personaje"])

print("\nsuperheroes masculinos:")

for personaje in cola:
    if personaje["genero"] == "M":

        print(personaje["personaje"])

for personaje in cola:

    if personaje["personaje"] == "scott lang":

        print("Scott Lang es:", personaje["superheroe"])

print("\nNombres que empiezan con S:")

for personaje in cola:

    if personaje["personaje"][0] == "S" or personaje["superheroe"][0] == "S":

        print(personaje)

encontrado = False

for personaje in cola:

    if personaje["personaje"] == "Carol Danvers":

        encontrado = True

        print("\nCarol Danvers está en la cola")
        print("Su superheroe es:", personaje["superheroe"])

if not encontrado:

    print("Carol Danvers no está en la cola")