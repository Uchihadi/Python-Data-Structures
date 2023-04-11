def find_it(num,element_list):
    #Remove pass and write the logic to search num in element_list using binary search algorithm
    #Return the total number of guesses made
    low=0
    high=len(element_list)-1
    no_of_guesses=0
    while(low<=high):
        no_of_guesses+=1
        mid=(low+high)//2
        if(num==element_list[mid]):
            return no_of_guesses
        elif(num<element_list[mid]):
            high=mid-1
        else:
            low=mid+1
            
    return 0