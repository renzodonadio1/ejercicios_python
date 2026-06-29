# la mochila es un vector
# el jedi:
# saca un objeto (uno por vez), cuenta cuantos saco, se detiene si encuentra el sable de luz

mochila = ["comida", "mapa", "sable de luz", "botella"]

def usar_la_fuerza(mochila, i=0):
    if i >= len(mochila): # caso base: no quedan objetos por revisar
        return False, i
    
    if mochila[i] == "sable de luz": # caso si encuentra el sable de luz
        return True, i
    
    return usar_la_fuerza(mochila, i + 1) # caso recursivo: revisar el siguiente objeto

encontrado, posicion = usar_la_fuerza(mochila)

if encontrado:
    print(f"¡El sable de luz se encuentra en la posición {posicion}!")
else:
    print("No se encontró el sable de luz en la mochila.")
