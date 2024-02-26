import re

def func(txt):
    pattern = r'[ ,.]'
    ans = re.sub(pattern, ':', txt)
    return ans

txt = input()
ans = func(txt)
print(ans)