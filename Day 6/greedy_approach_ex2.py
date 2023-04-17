#lex_auth_0127667363417702403454
def find_number_of_platforms(arrival_time_list,departure_time_list):
    arrival_time_list.sort()
    departure_time_list.sort()
    
    # Step 2: Initialize variables
    i = j = 0
    max_trains = curr_trains = 0

    # Step 5: Loop through the lists
    while i < len (arrival_time_list):
        if arrival_time_list [i] <= departure_time_list [j]:
            curr_trains += 1
            i += 1
        else:
            curr_trains -= 1
            j += 1
        max_trains = max(max_trains, curr_trains)

    # Step 6: Return the result
    return max_trains

#Pass different values to the function and test your program
arrival_time_list = [800,810]
departure_time_list = [2300,2000]
print("The arrival time of the trains:", arrival_time_list)
print("The departure time of the trains:",departure_time_list)
print("Minimum number of platforms required :",find_number_of_platforms(arrival_time_list,departure_time_list))