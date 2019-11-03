# Template file for Project Euler questions
import is_prime_jason
import q3_jason as p
import math

# O(sqrt(n))... looks sketchy tho
def number_divisors(num):
    divisors = 0

    for val in range(1, int(math.sqrt(num)) + 1):
        if num % val == 0:
            divisors += 1

    return divisors * 2

# Found a formula for triangle numbers to reduce loopage
def triangle_num(num):
    tri_num = (num * (num + 1)) / 2

    return tri_num


def triangle_divisors(num):
    tri_num_counter = 1
    tri_num = 0
    num_divs = 0

    while num_divs <= num:
        tri_num = triangle_num(tri_num_counter)
        num_divs = number_divisors(tri_num)
        tri_num_counter += 1

    return int(tri_num)


if __name__ == "__main__":
    # print(number_divisors(76576500))
    print(triangle_divisors(500))
