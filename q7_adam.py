import adam_helpers

def gen_primes(n):
    # Find the nth prime
    # Start with 2 already counted
    num_primes = 1
    test = 1
    while num_primes != n:
        test += 2
        num_primes += adam_helpers.is_prime(test)
    return test


if __name__=="__main__":
    # Takes a long time, maybe do it another way?
    print(gen_primes(10001))
