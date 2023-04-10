#lex_auth_0127426336682147841449

#If the double of an element in list1 is present in list2, then add it to the new list.

def check_double(list1,list2):
    new_list=[]
    for i in list1:
        if i*2 in list2:
            new_list.append(i)
    #write your logic here
    
    return new_list
#If the double of an element in list 1 is present in list 2, then add it to New List
#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))