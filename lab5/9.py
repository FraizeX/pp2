import re

def func(txt):
    ans = re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
    return ans

txt = input()
ans = func(txt)
print(ans)