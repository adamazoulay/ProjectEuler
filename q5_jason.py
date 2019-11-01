# Template file for Project Euler questions
# Smallest Multiple

# num is the number to check, div is the range of values to check


def pass_div(num, div):
    for x in range(1, div):
        if num % x != 0:
            return False
    return True


def smallest_mul(div):
    num = div
    while not pass_div(num, div):
        num += div
    return num


if __name__ == "__main__":
    print(smallest_mul(20))
    #print(pass_div(10, 10))
