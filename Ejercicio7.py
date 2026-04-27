def serie_h(num:int) -> float:
    if num == 1:
        return 1
    else:
        return 1/num + serie_h(num - 1)
    
print(serie_h(5))