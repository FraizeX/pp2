import re

txt = input()
pattern = r'ab*'

ans = re.search(pattern, txt)

print(ans.string)