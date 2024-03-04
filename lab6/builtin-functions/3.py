s = str(input())
n = reversed(s)
rev = ''.join(n)

if rev == s:
    print("is palindrome")
else:
    print("not palindrome")