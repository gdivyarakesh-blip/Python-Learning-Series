# Loops
# range()  range(S S S) S=start s =stop s=steps
# for loops
# a= range(1,20,1)
# for i in a :
#     print(i)

# for i in range(-5,-16,-1):
#     print(i)

# print a table of 5

# for i in range(5,51,5):
#     print(i)
#  Print a table from user input 

# n=int(input())
# for i in range(n,n*10+1,n):
#     print(i)

# a= "DivyaRakesh"

# for i in range(len(a)):
#     print(a[i])

# a= "Divya Rakesh Gandhi is cool"
# for i in a:
#     print(i)
#  break and continue
# for i in range(1,21):
#     if i== 15:
#         break
#     else:
#         print(i)
# for i in range(1,21):
#     if i== 15:
#         continue
#     else:
#         print(i)

#  for loops questions 
# Q1 Accept an integer and Print hello world n times

# n=int(input('Tell your no'))

# for i in range(n):
#     print("Hello World")

# Q2 Print natural no up to n

# n=int(input("Enter a no"))

# for i in range(1,n+1):
#     print(i) 

#  Q3 Reverse for loop print n to 1

# n= int(input("Enter a no"))

# for i in range(n,0,-1):
#     print(i)

#  Q4 Take a number as input and print its table
# n= int(input(" Enter a no"))

# for i in range(n,n*10+1,n):
#     print(i)
#  Q5 Sum up to n terms

# n =int(input("enter your input"))

# sum=0

# for i in range(1,n+1):
#     sum=sum+i
# print(f" your sum is{sum}")

# Q6 Factorial of a number

# n=int(input("Enter a no "))
# product=1
# for i in range(1,n+1):
#     product=product*i
# print(f"Factorial is{product}")

# Q7 Print the sum of all even and odd numbers in a range separately

# n=int(input("Enter a number:-"))
# even =0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even=even+i
#     else:
#         odd=odd+i
# print(f"your even and odd sum are {even}, {odd }")

# Q8 Print all the factors of a number.
# n=int(input("Enter your no"))

# for i in range(1,n+1):
#     if n%i==0 :
#         print(i)

# Q9 Accept a number and check if it is a perfect no or not

# n= int(input("Enter a number"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i

# if sum==n:
#     print("your number is perfect")

# else:
#     print("Not a perfect number")

# Q10 Check whether the number is prime or not
# n= int(input("Enter a number:-"))
# count =0

# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("Your no is prime")
# else:
#     print("Your no is not prime")

# Q11 Reverse a string 

# a= "Cricket catalyst"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# print(b)


# Q12 Check string is pallindrome or not
# a="NAMAN"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b + a[i]
# if b == a:
#     print("this string is a pallindrome")
# else: 
#     print("This string is not a pallindrome")


#  Q13 Count all letters digits and special symbols from a given string 
# a="sdfsogn12413@#$%^&U"
# char=0
# dig=0
# spchar=0

# for i in a:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchar+=1
# print(f"your digits are{dig}\n your alphabet are{char}\n your spchar is{spchar}")

# While loops Questions 

# Q1 Seperate each digit of a number and print it on the new line 
# a=int(input("Enter a number "))
# while a>0:
#     print(a %10)
#     a=a//10

# Q2 Accept a no and print reverse a no

# a=int(input("Enter a number "))
# rev =0
# while a>0:
#     rev=rev*10+a %10
#     a=a//10
# print(rev)

# Q3 Accept a no and check if it is a pallindromic number
# a=int(input("Enter a number "))
# copy=a
# rev =0
# while a>0:
#     rev=rev*10+a %10
#     a=a//10
# if copy == rev:
#     print("pallindrome")
# else:
#     print("Not a palindrome no ")
#  Q4 Create a random number guessing game with python.

# import random 
# num=random.randint(1,100)
# tries=0
# while True:
#     guess=int(input("Guess your number:"))
#     if num==guess:
#               print("you are right")
#               tries+=1
#               break
#     elif num <guess:
#          print("go a little lower")
#          tries+=1
#     elif num>guess:
#          print("go a little higher")
#          tries+=1 
#     else:
      
#       print("sorry you are wrong")
#       tries+=1
# print(tries)
