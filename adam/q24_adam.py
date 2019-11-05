# Kinda cheating but it's python so fuck it
import itertools

if __name__=="__main__":
    perms = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(perms[999999])
