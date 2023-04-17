#lex_auth_0127667342200995843410

def make_change(denomination_list, amount):
    count_coins = 0 
    rem = amount # remainder
    temp = amount
    if amount in denomination_list:
        return 1 
    #the actual calculation 
    # sort the denom list 
    copy_list = denomination_list.copy()
    copy_list.sort()
    i = -1    # start from the back 
    while rem > 0 and i >= -len(copy_list):
        if copy_list[i] <= temp:
            ind = copy_list[i]    #otherwise continue
            temp = temp - ind
            count_coins+=1
            rem = temp
        else:
                i = i - 1     # keep subtracting 
    if count_coins>0 :
        return count_coins 
    else:
        return -1 

#Pass different values to the function and test your program
amount= 20
denomination_list = [1,15,10]
make_change(denomination_list, amount)
