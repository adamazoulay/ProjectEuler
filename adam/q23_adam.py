def d(a):
    total = 0
    if a == 1:
        return 1
    for n in range(1, int(a/2) + 1):
        if a % n == 0:
            total += n
    return total

if __name__=="__main__":
    abundant = []
    max = 28124
    for i in range(1, max):
        sum_d = d(i)
        if sum_d > i and sum_d < max:
            abundant.append(i)

    # Find all combos of sums
    sums = []
    for num_1 in abundant:
        for num_2 in abundant:
            sum_cur = num_1 + num_2
            if sum_cur < 28124:
                sums.append(num_1 + num_2)

    sum_set = set(sums)
    total = 0
    for i in range(28124):
        total += i

    print(total - sum(sum_set))
