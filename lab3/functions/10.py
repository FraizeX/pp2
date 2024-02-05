def unique(list):
    unique_list = []
    for i in range(len(list)):
        is_unique = True
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                is_unique = False
                
        if is_unique:
            unique_list.append(list[i])
                
    return unique_list

list = [1, 2, 2, 3, 4, 4, 5]
print(unique(list))
                