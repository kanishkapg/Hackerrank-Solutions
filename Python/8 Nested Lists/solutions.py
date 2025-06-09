if __name__ == '__main__':
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])
    
    score_list = []
    for i in student_list:
        score_list.append(i[1])
    
    score_list = sorted(list(set(score_list)))
    
    name_list = []
    for i in student_list:
        if i[1] == score_list[1]:
            name_list.append(i[0])
            
    name_list.sort()
    for j in name_list:
        print(j)