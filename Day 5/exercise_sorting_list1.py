#lex_auth_0127667319794565123439
def order_heights(student_list,height_list):
    # Combine the students and their heights on to a list of tuples by use of zip
    student_height = list(zip(student_list, height_list))
    sorted_student_height = sorted(student_height, key = lambda x: x[1]) # Sorting by the second element height
    sorted_student, sorted_height = zip(*sorted_student_height) # Unzips sorted list to get separate list of students and their height
    return [list(sorted_student), list(sorted_height)]

#Pass different values to the function and test your program
student_list=["Santa","Tris","Arun","Rachel","John"]
height_list=[132.7,129.2,135,130.6,140]
print("Initial student details :")
print("The students:",student_list)
print("Their heights:",height_list)
print()
result=order_heights(student_list,height_list)
print("After arranging the students in the order of their height:")
print("The students :",result[0])
print("Their heights:",result[1])