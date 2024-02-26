import re

def func(txt):
    pattern = r'\b[a-z]+_[a-z]+\b'
    sequences = re.findall(pattern, txt)
    return sequences

txt = input()
ans = func(txt)
if ans:
    for seq in ans:
        print(seq)
