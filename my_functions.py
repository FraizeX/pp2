def histogram(values):
    for i in values:
        print("*" * i)

def is_palindrome(string):
    rev = ''.join(reversed(string))
    if rev == string:
        ans = "palindrome"
    else:
        ans = "not palindrome"
    return ans

def reverse(string):
    string = string.split()
    rev = ' '.join(reversed(string))
    return rev

def filter_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True