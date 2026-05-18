cola = [
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitan America", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"}
]

for personaje in cola:

for personaje in cola:

    if personaje["superheroe"] == "Capitana Marvel":

        print("Capitana Marvel es:", personaje["personaje"])


print("\nPersonajes femeninos:")

for personaje in cola:

    if personaje["genero"] == "F":

        print(personaje["personaje"])