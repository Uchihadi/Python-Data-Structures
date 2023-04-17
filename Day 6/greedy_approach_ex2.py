#lex_auth_0127667392950599683407
def find_maximum_activities(activity_list, start_time_list, finish_time_list):
    n = len(activity_list)
    activities = []
    for i in range(n):
        activities.append((activity_list[i], start_time_list[i], finish_time_list[i]))

    # sort the activities based on their finish times in ascending order
    activities.sort(key=lambda x: x[2])

    result = []
    last_finish_time = -1
    for activity in activities:
        if activity[1] > last_finish_time:
            result.append(activity[0])
            last_finish_time = activity[2]

    return result

#Pass different values to the function and test your program
activity_list=[1,2,3,4,5,6]
start_time_list=[1, 3, 0, 5, 8, 5]
finish_time_list= [2, 4, 6, 7, 9, 9]
print("Activities:",activity_list)
print("Start time of the activities:",start_time_list)
print("Finishing time of the activities:", finish_time_list)

result=find_maximum_activities(activity_list,start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:",result)