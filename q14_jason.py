# Template file for Project Euler questions
# Longest Collatz Sequence

def length_of_chain(num):
    current_number = num
    chain_len = 1
    while current_number != 1:
        if current_number % 2 == 0:
            current_number = current_number / 2
        else:
            current_number = (3 * current_number) + 1
        chain_len += 1
    return chain_len


def longest_collatz():
    longest_chain = 0
    current_start = 0
    for start_number in range(1, 1000000):
        chain_len = length_of_chain(start_number)
        if chain_len > longest_chain:
            longest_chain = chain_len
            current_start = start_number

    return current_start


if __name__ == "__main__":
    print(longest_collatz())

