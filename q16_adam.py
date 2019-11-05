
if __name__=="__main__":
    sum = 0
    pwr_num = str(2**1000)

    for digit in pwr_num:
        sum += int(digit)

    print(sum)
