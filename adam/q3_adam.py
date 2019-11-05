# Template file for Project Euler questions
def is_prime(num):
    for val in range(2, num):
        if num % val == 0:
            return False
    return True

if __name__=="__main__":
    target = 600851475143
    prime = False
    test = 1
    while not prime:
        test += 1
        if target % test == 0:
            check = int(target / test)
            prime = is_prime(check)

    print(check)
