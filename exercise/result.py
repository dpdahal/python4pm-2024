# num_student=int(input("Enter the number of students: "))
# students_marks=[]

# x=1

# while x<=num_student:
#     print(f"============Student Id {x}============")
#     for i in range(1):
#         nep =int(input("Enter the marks of Nepali: "))
#         eng =int(input("Enter the marks of English: "))
#         math =int(input("Enter the marks of Math: "))
#         sci =int(input("Enter the marks of Science: "))
#         pop =int(input("Enter the marks of Population: "))
#         total=nep+eng+math+sci+pop
#         students_marks.append(total)
#     x+=1



# for total in students_marks:
#     per = total/5
#     grade =""
#     if per>=80:
#         grade="A"
#     elif per>=60:
#         grade="B"
#     elif per>=40:
#         grade="C"
#     else:
#         grade="D"

#     print(f"Total Marks: {total} Percentage: {per} Grade: {grade}")


# data=['ram','sita','ram','hari','laxmi','laxmi']


students=[
    {'name':'ram','gender':'male','status':True},
    {'name':'sita','gender':'female','status':True},
    {'name':'hari','gender':'male','status':False},
    {'name':'laxmi','gender':'female','status':False},
    {'name':'gopal','gender':'male','status':True},
]

total_users=len(students)
total_active_user=0
total_inactive_user=0
total_male=0
total_female=0
total_active_male=0
total_active_female=0
total_inactive_male=0
total_inactive_female=0

for student in students:
    if student['status']==True:
        total_active_user+=1
    else:
        total_inactive_user+=1

    if student['gender']=='male':
        total_male+=1
    else:
        total_female+=1