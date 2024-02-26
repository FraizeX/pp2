import re

def func(txt):
    ans = re.findall("[A-Z][a-z0-9]*", txt)
    return ans

txt = input()
ans = func(txt)
print(ans)