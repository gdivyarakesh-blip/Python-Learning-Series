# Classes

# class Factory:
#     a=12 #attribute
#     def hello(self):
#         print("how are you")

#     print("Hello how are you I am getting initialized")

# # print(Factory().a)

# # Factory().hello()
# obj=Factory()   #Object

# print(obj.a)

# class Factory:
#     def __init__(self, material, zips, pockets):
#         self.material=material
#         self.zips=zips
#         self.pockets=pockets
#     def show(self):
#         print(f"Your materials are {self.material}, {self.pockets},{self.zips}  ")

# Factory("leather",3,2)

# reebok=Factory("leather",3,2)


# campus=Factory("nylon",3,3)

# # print(reebok.pockets)
# # print(campus.pockets)
# reebok.show()
# # campus.show()

# class Animal:
#     name="Lion"   #class attribute


#     def __init__(self,age):
#         self.age=age # instance attribute
#     def show(self):
#         print("How are you")

#     @classmethod
#     def hello(cls):
#         print("How are you broher")

#     @staticmethod
#     def static():
#         print("How are you")

# obj = Animal(12)


# obj.hello()


# class Factory1: #parent class
#     a="I am attribute mentioned inside factory"
#     def hello(self):
#         print("hello I am a method mentioned inside factory")

# class Factory2(Factory1):  #child class 
#                  pass

# obj =Factory1()

# obj2=Factory2()
# print(obj2.hello())


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"Hello your name is {self.name}, {self.age}")


# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age


# person1 = Human("Divya", 23)
# person1.show()


# class Animal:
#     name1="lion"

# class Human:
#     name2="harsh"
# class Robots(Animal,Human):
#     name3="charli123"
# obj=Robots()


# class Factory:
#     def __init__(self,material,zips):
#         self.material=material
#         self.zips=zips

# class BhopalFactory(Factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color=color

# class  PuneFactory(BhopalFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pockets=pockets


# class Animal:
#     def show():
#         print("Hello I am Divya")

# class Human(Animal):
#     def show(self):
#         print("How are you")

# obj=Human()

# obj.show()

# class Animal:
#     def show():
#         print("I am showing")
# class human:
#     def show():
#         print("Hello I am also showing")
# obj=Animal()
# obj2=Human()

# obj.show()
# obj2.show()

# class Factory:
#     __a="pune"

#     def show(self):
#         print("hello I am a pune factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super().__a)

# obj=Bhopal()
# obj.show2()

# from abc import ABC ,abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass





# class Square(abstract):
#     def __init__(self,side):
#         self.side=side

# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius=radius

#     def perimeter(self):
#         print("I have created")

#     def area(self):
#         print("I have created this")
# obj=Circle(7)

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age   # <-- ye line add karo

#     def __str__(self):
#         return f"Hello how are you and your name is {self.name}"
    
#     def __add__(self, other):
#         return f"Your sum of ages are {self.age + other.age}"

# obj = Animal("lion", 12)
# obj2 = Animal("dolphin", 14)

# print(obj + obj2)



# def addition(*args):
#     sum=0
#     for i in args:
#         sum=sum+i

#     print(sum)


# addition(12,12,23,50)


# def information(**kwargs):
#     print("your information is \n\n")
#     for i in kwargs:
#         print(f"{i}:{kwargs[i]}")
    


# information(name="Divya",age=20,designation="AI/ML")

# l=[i for i in range(1,21) if i %2==0]


# print(l)

# addition=lambda a,b:a+b

# print(addition(12,13))


# a=[1,2,3,4,5]

# result=map(lambda x:x*2,a)

# print(list(result))


# a=[1,2,3,4,5,6,7,8,9]

# result=filter(lambda x:True if x%2==0 else False,a)

# print(list(result))

