# Template file for Project Euler questions

if __name__=="__main__":
    # Difference is just square sum minus all diagonal terms (i.e. -2^2, 8^2, etc)
    total = 0
    for x in range (1, 101):
        for y in range(1, 101):
            if x != y:
                total += x*y
    print(total)
