def potencia(base:int, exponente:int) -> int:
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
print("la potencia de 2**3:", potencia(2, 3))

## para hacerlo con el exponente negativo:

def potencia(base:int, exponente:int) -> float:
    if exponente ==0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base,-exponente)
    else:
        return base * potencia(base,exponente-1)
    
print("la potencia de 2**-3:", potencia(2,-3))

