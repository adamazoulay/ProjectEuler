# Template file for Project Euler questions
def EvenFibonacci(max):
    sum = 2
    prevSum = 1
    next = 0
    total = 0

    while sum <= max:
        next = sum + prevSum
        prevSum = sum
        sum = next

        if(sum % 2 == 0):
            print(sum)
            total += sum

    return total + 2





if __name__=="__main__":
    print(EvenFibonacci(4000000))
