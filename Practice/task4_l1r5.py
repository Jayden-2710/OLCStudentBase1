def getgradepoint(mark):
    if mark >= 75:
        return 1
    elif mark >= 70:
        return 2
    elif mark >= 65:
        return 3
    elif mark >= 60:
        return 4
    elif mark >= 55:
        return 5
    elif mark >= 50:
        return 6
    elif mark >= 45:
        return 7
    elif mark >= 40:
        return 8
    else:
        return 9
    
def calL1R5(result):
    r5 = 0
    l1 = 0
    eng_grade = result['English']
    hcl_grade = result['Higher Chinese']
    for subject,score in result.items():
        if subject != 'English' and subject != 'Higher Chinese':
            r5 += getgradepoint(score)
    if eng_grade > hcl_grade or eng_grade == hcl_grade:
        l1 = getgradepoint(eng_grade)
    elif hcl_grade > eng_grade:
        l1 = getgradepoint(hcl_grade)
    print(f"l1 : {l1}")
    print(f"r5 : {r5}")  
    total_l1r5= l1 + r5 
    return total_l1r5

# test = {"English":1, "Higher Chinese":8, "Chemistry":65, "Geography":82, 
#         "Mathematics":74, "Physics":100,"Computing":0} 
# print(calL1R5(test))

score_temp = {"English":0 ,"Higher Chinese":0 ,"Chemistry":0 ,"Geography":0 ,"Mathematics":0 ,"Physics":0 ,"Computing":0 }

for subject in score_temp:
    score = input(f'how much did you get for {subject}.')
    score_temp[subject] = int(score)

tallied_score = calL1R5(score_temp)
print(tallied_score)

with open('resultslip.txt', 'w') as x:
    for subject, score in score_temp.items():
        x.write(f'{subject:<15}  {score:>8}\n')
    x.write(f'Computed L1R5: {tallied_score}')






        
      
    