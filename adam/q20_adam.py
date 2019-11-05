def factorial(n):
    total = 1
    while n > 0:
        total *= n
        n -= 1
    return total

if __name__=="__main__":
    fact_str = str(factorial(100))
    total = 0
    for digi in fact_str:
        total += int(digi)
    print(total)
