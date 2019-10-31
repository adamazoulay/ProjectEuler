# LargestPalindromeProduct

import math


def is_palidrome(test):
    test = str(test)
    check_val = True
    for i in range(len(test)):
        if test[i] != test[len(test) - 1 - i]:
            check_val = False
    return check_val


def largest_palidrome(digits):
    biggest = int(math.pow(10, digits) - 1)
    big_pal = 0
    test = ""
    for x in range(int(biggest), int(biggest/2), -1):
        for y in range(int(biggest), int(biggest/2), -1):
            if is_palidrome(str(x * y)) and x * y > big_pal:
                big_pal = x * y

    return big_pal


if __name__ == "__main__":
    print(largest_palidrome(3))
    # print(is_palidrome("90900000001909"))
