def convertir_binario(num:int) -> list:
    lista=[]

    while num > 0:
        lista.append(num % 2)
        num = num // 2
    return lista[::-1] #se invierte la lista para que el numero binario se muestre bien

print(convertir_binario(25))


