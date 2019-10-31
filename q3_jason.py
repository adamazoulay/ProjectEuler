import math


def prime_factors(number):
    big_prime = 1

    if number % 2 == 0:
        big_prime = 2
    for oddNum in range(3, int(math.sqrt(number)) + 1, 2):
        if number % oddNum == 0:
            big_prime = oddNum
            number /= oddNum

    return big_prime


if __name__ == "__main__":
    print(prime_factors(600851475143))
