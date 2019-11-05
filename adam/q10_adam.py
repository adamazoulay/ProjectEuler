
if __name__=="__main__":
    # Import prime list previously generated
    with open('primes.txt') as f:
        primes = f.read().replace('\n', '\t').split('\t')

    total = 0
    for prime in primes:
        prime = int(prime)
        if prime > 2e6:
            break
        total += prime

    print(total)
