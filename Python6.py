# Data Algorithums 
# List 
# a=[12,13,14,15,16,34.5,]

# list way using index 
# for i in range(len(a)):
#     print(a[i])

# 2nd way directly on values

# for i in a:
#     print(i)

#  Modify the value at index 1

# a[1]=90
# print(a)


# l=[1,2,3,4,5,8,10,12]

# l.append(6)
# l.append(7)
# l.insert(1,3)
# l.remove(2)
# l.extend([20,25,30])
# l.sort()
# l.reverse()
# new_l=l.copy()
# print(new_l)
# print(l)
# Questions
#  Q1 Print positive and negative elements of an List?
# l=[-45,65,12,-68,-69,34]
# print("Postive elements are")
# for i in l:
#     if i >=0:
#         print(i)
# print("Negative elemnts are")
# for i in l:
#     if i<0:
#         print(i)
# Q2 Mean of list elements 
# l=[12,435,67,89,23,25,69]

# sum =0
# avg=0
# for i in l:
#     sum=sum+i
#     avg=sum/len(l)
# print(avg)

# Q3 Find the greatest element and print its index 

# l=[12,567,43,235,347,568,45,7]
# largest=l[0]

# for i in range(len(l)):
#     if l[i] >largest:
#         largest=l[i]
#         index=i

# print(f"your largest number is {largest} at index {index}")

# Q4 Find the second greatest element 
# l=[20.30,40,50,125,800,565,700]
# largest=l[0]
# secondlargest=l[0]

# for i in l:
#         if i>largest:
#                 secondlargest= largest
#                 largest =i
#         elif i> secondlargest:
#                 secondlargest=i
# print(secondlargest,largest)

#  Q5 Check if List is sorted or not  
# a=[12,13,14,15,16,31,20]

# for i in range(len(a)-1):
#     if a[i]<a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")

#  Tuple 

# a=(1,2,3,4,5,5,5,5)
# print(type(a))
# a[0]=12    Tupple is immutable 
# print(a[0]) Tupple is ordered and also Heterogeneous

# for i in a:
#     print(i)
# count=a.count(5)
# print(count)

# index=a.index(5)
# print(index)

# a,b,c,d=(1,2,3)
# print(b)


# Set

# s={1,2,3,4,5,5,4} 
# print(s)
#  Sets are mutable 
# Sets cannot have duplicates
# sets have unordered list and cannot access them through index values

# b=hash("Hello")
# print(b)

# a={1,2,3,"hello",4,5}

# for i in a:
#     print(i)
# a={1,2,3,4}
# a.remove(2)
# a.pop()
# print(a)

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# s=a^b
# print(s)

#  Dictionary
# d={10:100,20:200,30:300,40:400}
# d[10]=1000
# d.update({50:500})
# d[50]=500
# print(d)
# d.clear()
# for i in d.values():
#     print(i)
# print(type(d))
# a=[1,2,3,4,5]
# b=a.copy
# b[0]=100
# print(a)
# d2=d.copy()
# print(d2)
# d2=d.get(20)
# print(d2)
# print(d.items())
# Questions
# Q1 Write a python code to merge two Python dictionaries

# d1={10:100,20:200,30:300}
# d2={40:400,50:500,60:600}

# for i in d2:
#     d1[i]=d2[i]
# print(d1)
#  Q2 Write a python program to sum all the values
# d1={10:100,20:200,30:300}
# sum=0
# for i in d1:
#      sum=sum+d1[i]
# print(sum)

# Q3 Count the frequency element in list
# a=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]


# d= {}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# Q4  Write a Python program to combine two dictionary by adding
# values for common keys.

# d1={10:100,20:200,40:300}
# d2={40:400,50:500,60:600}
# for i in d2:
#     if i in d1.keys():
#         d1[i]+=d2[i]
#     else:
#         d1[i]=d2[i]

# print(i)

