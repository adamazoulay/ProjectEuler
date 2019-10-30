# Template file for Project Euler questions

if __name__=="__main__":
    a, b, c, = 1, 2, 3
    # Let's just find all a+b+c=1000 combinations and then enforce the other
    #  conditions after (a_max is 333 for a<b<c)
    sums = []
    for a in range(334):
        for b in range(a, 999):
            c = 1000 - a - b
            if (a**2 + b**2 == c**2) and (a < b) and (b < c):
                print(a * b * c)
