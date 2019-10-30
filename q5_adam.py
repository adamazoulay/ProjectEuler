# Template file for Project Euler questions
def is_divisible_20(num):
    div = True
    for test in range(2, 21):
        div = div and (num % test == 0)
    return div


if __name__=="__main__":
    start = 20
    while not is_divisible_20(start):
        start += 20
    print(start)
