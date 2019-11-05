# Template file for Project Euler questions
import math


def special_pyth(num):
    c = 0

    for a in range(1, num):
        for b in range(1, num):
            csquare = (a * a) + (b * b)
            c = math.sqrt(csquare)
            if (a + b + c) == num:
                print("a: ", a, " b: ", b, " c: ", c)
                return int(a * b * c)


if __name__ == "__main__":
    print(special_pyth(1000))
