# This is going to suck
# Super ugly and can be made waaaayyyyy cleaner but here we are

def num_2_word_ones(n):
    n = int(n)
    if n == 0:
        return ""
    if n == 1:
        return "one"
    if n == 2:
        return "two"
    if n == 3:
        return "three"
    if n == 4:
        return "four"
    if n == 5:
        return "five"
    if n == 6:
        return "six"
    if n == 7:
        return "seven"
    if n == 8:
        return "eight"
    if n == 9:
        return "nine"

def num_2_word_tens(n):
    n = int(n)
    if n < 10:
        return num_2_word_ones(n)
    if n == 10:
        return "ten"
    if n == 11:
        return "eleven"
    if n == 12:
        return "twelve"
    if n == 13:
        return "thirteen"
    if n == 14:
        return "fourteen"
    if n == 15:
        return "fifteen"
    if n == 16:
        return "sixteen"
    if n == 17:
        return "seventeen"
    if n == 18:
        return "eighteen"
    if n == 19:
        return "nineteen"
    if str(n)[0] == "2":
        return "twenty" + num_2_word_ones(str(n)[1])
    if str(n)[0] == "3":
        return "thirty" + num_2_word_ones(str(n)[1])
    if str(n)[0] == "4":
        return "forty" + num_2_word_ones(str(n)[1])
    if str(n)[0] == "5":
        return "fifty" + num_2_word_ones(str(n)[1])
    if str(n)[0] == "6":
        return "sixty" + num_2_word_ones(str(n)[1])
    if str(n)[0] == "7":
        return "seventy" + num_2_word_ones(str(n)[1])
    if str(n)[0] == "8":
        return "eighty" + num_2_word_ones(str(n)[1])
    if str(n)[0] == "9":
        return "ninety" + num_2_word_ones(str(n)[1])

def num_2_word_hunds(n):
    n = int(n)
    if n == 0:
        return ""
    if n == 1:
        return "onehundred"
    if n == 2:
        return "twohundred"
    if n == 3:
        return "threehundred"
    if n == 4:
        return "fourhundred"
    if n == 5:
        return "fivehundred"
    if n == 6:
        return "sixhundred"
    if n == 7:
        return "sevenhundred"
    if n == 8:
        return "eighthundred"
    if n == 9:
        return "ninehundred"


if __name__=="__main__":
    total = 0
    for n in range(1, 1001):
        num_str = ""
        n = str("{0:04d}").format(n)
        if n[0] == "1":
            num_str += "onethousand"
        elif int(n[1]) > 0:
            num_str = num_2_word_hunds(n[1])
            if n[2:] != "00":
                num_str += "and"
        num_str += num_2_word_tens(n[2:])
        total += len(num_str)
        #print(num_str)

    print(total)
