# Template file for Project Euler questions
def calc_first_10(num_digits):
    sum_10 = 0
    last_10 = []
    file = open("q13.txt", "r+")
    big_number = file.read().split("\n")
    current_val = 0
    total = 0
    for x in range(num_digits + 5):
        digits = 10 ** ((num_digits-1) -x)
        for val in big_number:
            sum_10 += int(val[x]) * digits
           # print(int(val[(len(val)-1) - x]))
       # sum_10 += current_val * digits
       # print(sum_10)
    sum_10 = str(sum_10)

    return sum_10[0:10]

if __name__=="__main__":
    print(calc_first_10(10))

