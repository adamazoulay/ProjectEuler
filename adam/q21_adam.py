def d(a):
    total = 0
    if a == 1:
        return 1
    for n in range(1, int(a/2) + 1):
        if a % n == 0:
            total += n
    return total

if __name__=="__main__":
    d_list = []
    for n in range(1, 10001):
        d_list.append((n, d(n)))

    ami_list = []
    for row in d_list:
        a = row[0]
        d_a = row[1]

        for row_2 in d_list:
            b = row_2[0]
            d_b = row_2[1]

            if d_a == b and d_b == a and a != b:
                if (a not in ami_list and b not in ami_list):
                    ami_list.append(a)
                    ami_list.append(b)

    print(sum(ami_list))
