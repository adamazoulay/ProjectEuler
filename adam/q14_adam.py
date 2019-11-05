def get_chain_length(n):
    length = 1
    while n > 1:
        length += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3*n + 1
    return length

if __name__=="__main__":
    max_length = 0
    max_num = 0
    for i in range(2, 1000000):
        chain_i = get_chain_length(i)
        if chain_i > max_length:
            max_length = chain_i
            max_num = i
    print(max_num)
