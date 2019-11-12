
def power_of(num):
    twos = 2 ** num
    twos_string = str(twos)
    sum = 0
    for char in twos_string:
        sum += int(char)
    return sum


if __name__=="__main__":
    print(power_of(1000))
