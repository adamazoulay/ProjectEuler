def prime_factors(number):
    prime_nums = []
    index = 0
    while index < number:
        index += 1
        if 0 == number % index:
            prime_nums.append(index)
    return prime_nums

if __name__ == "__main__":
    print(prime_factors(600851475143))
