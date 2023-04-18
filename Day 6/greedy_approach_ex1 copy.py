def make_change(denomination_list,index, amount):
    if(amount==0):
       return 1
    if(amount <0):
       return 0
    if(amount > 0 and index==len(denomination_list)):
       return 0
    return make_change(denomination_list,index,amount-denomination_list[index]) + make_change(denomination_list,index+1,amount) # Include case + Exclude case

#Pass different values to the function and test your program
amount= 7
denomination_list = [2,3,5]
print(make_change(denomination_list,0, amount))