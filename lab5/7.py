import re

def func(txt):
    pattern = r"_(\w)"
    ans = re.sub(pattern, lambda x: x[1].upper(), txt)
    return ans

txt = input()
ans = func(txt)
print(ans)