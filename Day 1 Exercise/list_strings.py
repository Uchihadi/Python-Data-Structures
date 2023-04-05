# lex_auth_0127426166978887681375
# Given two lists with String elements, write a python program using python lists to create a new string as per the rule given below
# First element in list1 should be merged with last element in list2
# Second element in list1 should be merged with second last element in list2
# If an element in list1/list2 is None, then the corresponding element in the other list should be kept as it is in the merged list

def merge_list(list1, list2):
    list2 = list2.reverse()
    merged_data=""
    # for i in list1:
    #     for j in list2:
            
    #write your logic here
    pass

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)