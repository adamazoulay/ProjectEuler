# Template file for Project Euler questions
def is_palindrome(num):
    num = str(num)
    half = int(len(num) / 2)
    p1 = num[:half]
    p2 = num[half:][::-1]
    if p1 == p2:
        return True
    return False


if __name__=="__main__":
    prod1 = 999

    palilist = []
    while prod1 > 0:
        prod2 = 999
        while prod2 > 0:
            total = prod1 * prod2
            if is_palindrome(total):
                palilist.append(total)
            prod2 -= 1
        prod1 -= 1

    print(max(palilist))
