import re

def func(txt):
    pattern = r'a.*b$'
    ans = re.search(pattern, txt)
    if ans:
        return True
    else:
        return False

txt = input()
if func(txt):
    print(txt)
