def has_33(list):
    for i in range(len(list) - 1):
        if list[i] == list[i+1] == 3:
            return True
    return False

list1 = [1, 3, 3]
list2 = [1, 3, 1, 3]
list3 = [3, 1, 3]

print(has_33(list1))
print(has_33(list2))
print(has_33(list3))