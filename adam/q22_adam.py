def str_2_num(str_in):
    total = 0
    for letter in str_in:
        total += ord(letter) - 64

    return total

if __name__=="__main__":
    with open("p022_names.txt") as inf:
        names = inf.read().replace('"', "").split(",")

    names.sort()

    total = 0
    for i in range(len(names)):
        pos = i + 1
        total += pos * str_2_num(names[i])

    print(total)
