def convertir_romanos(romano=str) -> int:
    valores={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    
    total = 0

    for i in range(len(romano)):
        actual = valores[romano[i]]
        
        # si hay siguiente
        if i+1 < len(romano):
            siguiente = valores[romano[i+1]]
            
            if actual < siguiente:
                total -= actual
            else:
                total += actual
        else:
            total += actual
    
    return total

print("numero XII:", convertir_romanos("XII")) 
print("numero IX:", convertir_romanos("IX"))
print("numero MMXXVI:", convertir_romanos("MMXXVI"))