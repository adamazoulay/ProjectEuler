# Template file for Project Euler questions
# 10001st PrimeNumber
import math


def is_prime(num):
    prime = True
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(num)) + 1, 2):
        if num % x == 0:
            prime = False
    return prime


def find_prime(num):
    prime_num = 1
    counter = 3
    while prime_num != num:
        if is_prime(counter):
            prime_num += 1
        if prime_num == num:
            return counter
        counter += 2
    return


if __name__ == "__main__":
    print(find_prime(10001))
