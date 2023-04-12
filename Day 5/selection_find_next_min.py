#lex_auth_0127667370895278083332

def find_next_min(num_list,start_index):
    #Remove pass and write the logic to find the minimum element in a sub-list and return the index of the identified element in the num_list.
    #start_index indicates the start index of the sub-list
    min=num_list[start_index]
    min_index=start_index
    for i in range(start_index+1,len(num_list)):
       if(num_list[i]<min):
          min=num_list[i]
          min_index=i
    return min_index

#Pass different values to the function and test your program
num_list=[10,2,100,67]
start_index=1
print("Index of the next minimum element is", find_next_min(num_list,start_index))