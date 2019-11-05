def is_prime(num):
    for val in range(2, num):
        if num % val == 0:
            return False
    return True
