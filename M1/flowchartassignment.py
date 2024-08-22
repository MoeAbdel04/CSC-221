

student_num = int(input("Enter number of students: "))

def get_stu_info(student_num):
    names = []
    scores = []
    
    for i in range(student_num):  
        get_name = input(f"Enter name for student: ")
        names.append(get_name)
        get_score = input(f"Enter student score: ")
        scores.append(get_score)
    

    return names, scores

def dis_stu_info(name_list, score_list):
    print (f'{"Student":<10}{"Score"}')
    for x in range (len(name_list)):
        print (f'{name_list[x]:<10}{score_list[x]}')
name_list, score_list = get_stu_info(student_num)

dis_stu_info(name_list, score_list)
        

