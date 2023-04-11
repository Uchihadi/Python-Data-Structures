#DSA-Tryout

import random

def find_it(num,element_list):
    #Remove pass and copy the solution earlier written for this function here
    #Modify it, if required
    pass

def initialize_list_of_elements(n):
    #Modify the code to initialize the list of elements in ascending order
    #Try with descending order also
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    mid=n//2
    for j in range(0,n):
        index1=random.randrange(0,mid)
        index2=random.randrange(mid,n)
        num1=list_of_elements[index1]
        list_of_elements[index1]=list_of_elements[index2]
        list_of_elements[index2]=num1
    return list_of_elements

def play(n):
    #Remove pass and copy the solution earlier written for this function here
    pass

#Pass different values to play() and observe the output
play(400)