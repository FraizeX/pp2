list = list(map(int, input().split()))
factor = 1
for x in range(0, len(list) - 1):
    factor = factor * list[x+1]
    
# n = 0
# anslist = []
# while n < factor:
#     anslist.append(list[0])  #second variant
#     n += 1
# ans = sum(anslist)
# print(ans)
print(sum([list[0] * factor]))