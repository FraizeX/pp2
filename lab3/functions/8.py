def spy_game(list):
    count_0 = 0
    count_7 = 0
    for i in list:
        if i == 0 and count_7 == 0:
            count_0 += 1
        if i == 7 and count_0 == 2:
            count_7 += 1
        if count_0 == 2 and count_7 == 1:
            return True
        
    return False
            

list1 = [1,2,4,0,0,7,5]
list2 = [1,0,2,4,0,5,7]
list3 = [1,7,2,0,4,5,0]

print(spy_game(list1))
print(spy_game(list2))
print(spy_game(list3))