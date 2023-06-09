#lex_auth_0127667356693872643343

def swap(num_list, first_index, second_index):
    temp = 0 
    temp = num_list[first_index]
    num_list[first_index] =num_list[second_index]
    num_list[second_index] = temp
    
def find_next_min(num_list,start_index):
    for i in range(start_index,len(num_list)):
        if num_list[i] < num_list[start_index]:
            start_index = i
    return start_index

def selection_sort(num_list):
    for i in range(len(num_list)):
        small_data = find_next_min(num_list, i)
        swap(num_list,i,small_data)

#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)