def NumberOf1BetweenXAndN_Solution(n, x):
    mult, sumTimes = 1, 0
    while n//mult > 0:
        high, mod = divmod(n, mult*10)
        curNum, low = divmod(mod, mult)
        if curNum > x:
            sumTimes += high*mult + mult
        elif curNum == x:
            sumTimes += high*mult + low + 1
        else:
            sumTimes += high*mult
        mult = mult*10
    return sumTimes

print(NumberOf1BetweenXAndN_Solution(156,5))