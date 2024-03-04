def calculator(string):
    counter_upper = 0
    counter_lower = 0
    for x in string:
        if x.isupper():
            counter_upper += 1
        
        if x.islower():
            counter_lower += 1
            
    return counter_upper, counter_lower

str = str(input())
ans = calculator(str)
print(list(ans))