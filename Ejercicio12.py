def mcd(num1:int, num2:int) -> int:
    if num2 == 0:
        return num1
    else:
        return mcd(num2, num1 % num2)
    
print(mcd(12,6))
print(mcd(48,18))