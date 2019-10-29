# Template file for Project Euler questions

if __name__=="__main__":
    lastfib = 1
    curfib = 2
    total = 0
    while curfib <= 4e6:
        if curfib % 2 == 0:
            total += curfib

        # Iterate fib vars
        newfib = lastfib + curfib
        lastfib = curfib
        curfib = newfib

    print(total)
