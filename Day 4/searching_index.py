#lex_auth_0127667385795952643524

def find_decreasing_start(list1, start, end):
    for i in range (start, end):
        if list1[i] > list1[i+1]:
            return i+1
    return None

#Use different values for list1 and test your program
list1=[1,4,7,8,9,5,4]
start=0
end=len(list1)-1
result=find_decreasing_start(list1,start,end)
print("The index position at which the increasing array starts decreasing is:",result)