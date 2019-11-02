# Template file for Project Euler questions
# Sum of all primes below num
import math
import is_prime_jason as check


def sum_primes(num):
    total = 2
    for oddNum in range(3, num+1, 2):
        if check.is_prime_jason(oddNum):
            total += oddNum
            print("Current Total: ", total, "Current Prime: ", oddNum)
    return total


if __name__ == "__main__":
    print(sum_primes(2000000))
