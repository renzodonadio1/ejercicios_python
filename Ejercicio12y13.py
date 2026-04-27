def mcd(num1:int, num2:int) -> int:
    if num2 == 0:
        return num1
    else:
        return mcd(num2, num1 % num2)
    
print(mcd(12,6))
print(mcd(48,18))

# Ejercicio 13

def mcm(num1:int, num2:int) -> int:
    return (num1 * num2) // mcd(num1, num2)

print(mcm(12,6))
print(mcm(48,18))