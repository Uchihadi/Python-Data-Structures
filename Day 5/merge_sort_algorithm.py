#lex_auth_0127667368801157123532
# Use the algorithm to get your answer
def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    low=0                   # 1. Initialise low as 0 (start index of the list)
    high=len(num_list)-1    # 2. Initialise high as last index of list
    if(low==high):          # 3. If low == high then return the list
       return num_list
    else:                   # 4. Else
       mid=(low+high)//2                        # a. Divide the list into two halves,left list and right list
       l1=merge_sort(num_list[0:mid+1])         # b. Invoke Merge_Sort() by passing left list
       l2=merge_sort(num_list[mid+1:high+1])    # c. Invoke Merge_Sort() by passing right list
       sorted_list=merge(l1,l2)                 # d. Invoke Merge() by passing the lists returned in step 4b and 4c respectively
    return sorted_list                          # e. Return the sorted list which is returned in step 4d
    
def merge(left_list,right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    i=j=0                                           # 1. Initialize i, j as 0
    sorted_list=[]                                  # 2. Create an empty sorted_list
    while(i<len(left_list) and j<len(right_list)):  # 3. While((i < number of elements in left list ) and (j < number of elements in right list) do
        if(left_list[i]<=right_list[j]):            # a. If(left_list[i]<=right_list[j]) then append left_list[i] to the sorted_list and increment i
           sorted_list.append(left_list[i])         
           i+=1
        else:
           sorted_list.append(right_list[j])        # b. Else append right_list[j] to sorted_list and increment j
           j+=1
    while(i<=len(left_list)-1):                     # 4. If there are any elements left in left_list, append it to sorted_list
       sorted_list.append(left_list[i])
       i+=1
    while(j<=len(right_list)-1):                    # 5. If there are any elements left in right_list, append it to sorted_list
       sorted_list.append(right_list[j])
       j+=1
    return sorted_list                              # 6. Return the sorted_list

num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)
