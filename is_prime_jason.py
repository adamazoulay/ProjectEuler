# Template file for Project Euler questions
import math


def is_prime_jason(num):
    if num % 2 == 0 and num != 2:
        return False
    elif num == 2:
        return True
    elif num == 1:
        return False
    for val in range(3, int(math.sqrt(num))+1, 2):
        if num % val == 0 and num != val:
            return False
    return True

