def is_palindrome(string):
    rev = ''.join(reversed(string))
    if rev == string:
        ans = "palindrome"
    else:
        ans = "not palindrome"
    return ans

string = str(input())
print(is_palindrome(string))