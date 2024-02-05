def reverse(string):
    string = string.split()
    rev = ' '.join(reversed(string))
    return rev
    
string = input()
print(reverse(string))