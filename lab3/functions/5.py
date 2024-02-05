from itertools import permutations

def next_permutations(string):
    perms = permutations(string)
    for i in perms:
        print(''.join(i))

string = input()
next_permutations(string)