# Template file for Project Euler questions
import math

def sum_square_dif(max):
    sum_square = 0
    square_sum = 0

    for num in range(1, max+1):
        sum_square += num * num
        square_sum += num
    square_sum = square_sum * square_sum

    return square_sum - sum_square
if __name__=="__main__":
    print(sum_square_dif(100))
