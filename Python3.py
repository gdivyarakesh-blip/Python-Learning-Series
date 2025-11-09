#if else
# a=8

# if a>10:
#     print("I will do Task A")
# else:
#     print("I will do Task B")
# money=int(input("please provide money"))

# if money==10:
#     print('I will eat choclate')
# elif money==20:
#     print("I will eat icecream")
# elif money==30:
#     print("I will eat sweet ")
# else:
#     print("I will eat burger")  
# Q1 which no is greater
# a=int(input("enter a first no"))
# b=int(input("enter a second no"))

# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")
# Q2 Morning message 
# a = input("Enter a gender: ")

# if a == 'M' or a == 'm':
#     print("Good morning sir")
# elif a == 'F' or a == 'f':
#     print("Good morning mam")
# else:
#     print("Wrong input")
# Q3 check no is even or odd
# a=int(input("Enter a number"))

# if a%2==0:
#     print(f"{a} is even no")
# else :
#     print(f"{a} is odd no")
# Q4 chech person is eligible to vote or not
# name=input("Enter a name")
# age=int(input("Enter a age"))

# if age>=18:
#     print(f"{name} is {age}years old and eligible to vote")
# else :
#     print (f"{name} is {age}years old and not eligible to vote")

# Q5 check year is leap year or not 
# year=int(input("Enter a year"))

# if year%100 ==0 and year%400 ==0 :
#     print("Its a leap year")
# elif year%4 ==0 :
#     print("Its a leap year")
# else:
#      print("Its not a leap year")

# if -elif ladder 
temp=float(input("Enter a temperature"))
if temp<0:
    print("Freezing cold")
elif temp>=0 and temp< 10:
    print("very Cold")
elif temp>=10 and temp< 20 :
    print("cold")
elif temp>=20 and temp< 30 :
    print("Pleasant")
elif temp >=30 and temp <40 :
    print("Hot")
else : 
    print("Very Hot")


