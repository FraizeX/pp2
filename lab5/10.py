import re

txt = input()
ans = re.sub(r"[A-Z]",lambda x: "_" + x[0].lower(), txt)

if ans:
    print(ans)
