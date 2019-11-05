
if __name__=="__main__":
    max = 1000
    total = 0

    # Stop if we find divisible by 3, else check for 5
    for num in range(max):
        if num % 3 == 0:
            total += num
        elif num % 5 == 0:
            total += num

    print(total)
