def raiz_entera(num1:int) -> int:
    return aux(num1, 0)

def aux(num1:int, num2:int) -> int:
    if num2 * num2 > num1:
        return num2 - num1
    return aux(num1, num2 - 1)

print(raiz_entera(16))
print(raiz_entera(25))
