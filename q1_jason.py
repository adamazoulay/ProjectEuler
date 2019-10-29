
if __name__=="__main__":
    index = 334
    max = 1000
    sum = 0

    for x in range(index):
        if x * 3 < max:
            sum += x*3
        if (x * 5 < max) and ((x * 5) % 3 != 0):
            sum += x*5
        print(sum)
    print(sum)
