import math

def gen_triangle(n):
    tri = 0
    cur = 0
    while cur < n:
        cur += 1
        tri += cur
    return tri

def get_divisors(n):
    divisors = [1, n]
    for denom in range(2, n):
        if (denom in divisors):
            break
        if (n % denom == 0):
            divisors.append(denom)
            divisors.append(int(n / denom))
    return len(divisors)

if __name__=="__main__":
    divisors = 0
    i = 1

    while divisors <= 500:
        tri = gen_triangle(i)
        divisors = get_divisors(tri)
        i += 1
    print(tri)
