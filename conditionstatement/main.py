# x=20
# y=20
# # print(x>y)

# if x>y:
#     print("x is greater than y")
# elif x==y:
#     print("x is equal to y")
# else:
#     print("y is greater than x")


# a=10
# b=20
# c=30

# if a>b and a>c:
#     print("a is greater than b and c")
# elif b>a and b>c:
#     print("b is greater than a and c")
# else:
#     print("c is greater than a and b")

# WAP to enter five subject make and calculate the percentage 
# and print the grade
# 35-45 D
# 45-60 C
# 60-75 B
# 75-100 A
# <35 F

# nep = int(input("Enter the marks of Nepali: "))
# eng = int(input("Enter the marks of English: "))
# math = int(input("Enter the marks of Math: "))
# sci = int(input("Enter the marks of Science: "))
# comp = int(input("Enter the marks of Computer: "))
# total = nep+eng+math+sci+comp
# per = total/5

# if per>35 and per<=45:
#     print("Grade D")
# elif per>45 and per<=60:
#     print("Grade C")
# elif per>60 and per<=75:
#     print("Grade B")
# elif per>75 and per<=100:
#     print("Grade A")
# else:
    # print("Grade F")


# mark=36

# if mark>35:
#     if mark>90:
#         print("A+")
#     elif mark>80:
#         print("A")

# else:
#     print("Fail")

# WAP to enter age and check if the person is 
# eligible to vote or not
# criteria 18 < you are child
# 18-60 you are eligible
# >60 you are old

# AMT
# pin
# 1234
# withdraw
# balance inquiry
# total_amount=10000

# bank ="bank of kathmandu"
# name = input("Enter your name: ")
# address = input("Enter your address: ")
# document = input("Enter your document: ")

# if document=="citizenship" or document=="passport":
#     print("You are eligible to open account")

# else:
#     print("Invalid document")

# WAP to enter any number and check it is
#  divisible by 3 and 5
# is,is not
# in , not in


# x=5
# y=6
# z=x

# print(x is z)
# print(x is not y)

# name ='sophia'
# print('s' in name)
# print('s' not in name)
# print('z' in name)

# data =['ram','shyam','hari','sita','gita']

# if 'gita' in data:
#     print(" in the list")
# else:
#     print("is not in the list")

# data=[
#     {'username':'ram','password':'ram123'},
#     {'username':'sophia','password':'sophia123'},
# ]

# print(data[0]['username'])
# WAP to enter username and password and check if the user is valid or not

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if data[0]['username']==username and data[0]['password']==password:
#     print("Welcome to the system")
# elif data[1]['username']==username and data[1]['password']==password:
#     print("Welcome to the system")
# else:
#     print("Invalid username or password")

# x=90
# y=30
# z=40

# if x>y and x>z:
#     if y>z:
#         print(x,y,z)
#     else:
#         print(x,z,y)
# elif y>x and y>z:
#     if x>z:
#         print(y,x,z)
#     else:
#         print(y,z,x)
# else:
#     if x>y:
#         print(z,x,y)
#     else:
#         print(z,y,x)

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if username=='admin':
#     if password=='admin':
#         print("Welcome to the system")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid username")

# party: 18-40
#  18-25 -> beer
#  25-30 -> whiskey
#  30-40 -> wine


# language ='nep'

# match language:
#     case 'nep':
#         print("Nepali")
#     case 'eng':
#         print("English")
#     case 'hin':
#         print("Hindi")
#     case 'chi':
#         print("Chinese")
#     case _:
#         print("Invalid language")
