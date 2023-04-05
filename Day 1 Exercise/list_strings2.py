def merge_list(list1, list2):
    merged_list = []
    for a, b in zip(list1, reversed(list2)):
        if a is None:
            merged_list.append(b)
        elif b is None:
            merged_list.append(a)
        else:
            merged_list.append(a + b)
    return ' '.join(merged_list)

list1=['T', 'sk', None, 'bl']
list2=['ue', 'is', 'y', 'he']
merged_data=merge_list(list1,list2)
print(merged_data)

#How can we solve this method without using the zip method?