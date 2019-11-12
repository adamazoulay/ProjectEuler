def number_to_letter(number):
    file = open("q17.txt", "r+")
    file_strings = file.read().split("\n")
    number_strings = file_strings[0].split(" ")
    double_strings = file_strings[1].split(" ")
    teens = file_strings[2].split(" ")
    big_strings = file_strings[3].split(" ")
    num = str(number)
    total_string = ""


    while len(num) < 4:
        num = "0" + num
    if num[0] != "0":
        for x in range (1, 10):
            if int(num[0]) == x:
                total_string += number_strings[x-1] + " thousand "
    if num[1] != "0":
        for x in range (1, 10):
            if int(num[1]) == x:
                total_string += number_strings[x-1] + " hundred "
    if num[2] == "1" and num[3] != "0":
            for x in range(1, 10):
                if int(num[3]) == x:
                    if num[1] != "0":
                        total_string += "and " + teens[x-1]
                    else:
                        total_string += teens[x-1]
            return total_string
    elif num[2] != "0":
        for x in range (1, 10):
            if int(num[2]) == x:
                if num[1] != "0":
                    total_string += "and " + double_strings[x-1]
                else:
                    total_string += double_strings[x-1]
    if num[3] != "0" and int(num[2]) > 1:
        for x in range (1, 10):
            if int(num[3]) == x:
                total_string += " " + number_strings[x-1]
    elif num[3] != "0" and num[1] != "0":
        for x in range (1, 10):
            if int(num[3]) == x:
                total_string += "and " + number_strings[x-1]
    elif num[3] != "0" and num[2] == "0" and num[1] == "0" and num[0] == "0":
        for x in range (1, 10):
            if int(num[3]) == x:
                total_string += number_strings[x-1]

    return total_string



def number_letters(number):
    total_string = ""
    for num in range(1, number + 1):
        total_string += number_to_letter(num)

    return len(total_string.replace(" ", ""))


if __name__=="__main__":
    print(number_letters(1000))
    #print(number_to_letter(801))
