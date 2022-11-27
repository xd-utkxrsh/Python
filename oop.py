#classes and objects
'''class car:
    name=None
    color=None
    def get_speed(self):
        name="Breeza"
        color="Black"
        return name+" is available in "+color+" color."
Honda=car()
print(Honda.get_speed())




class person():
    name=" "
    age=" "
    def showself(self):
        name=input("name: ")
        print("your name is",name)
        age=input("age: ")
        print("your age is",age)

d1=person()
d1.showself()
d2=person()
d2.showself()




class test():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def out(self):
        print(name,age)

name=input("name: ")
age=input("age: ")
a=test(name,age)
a.out()




class Des():
    def __init__(self):
        print("welcome")
    def __del__(self):
        print("destructor called")

ob1=Des()
ob2=Des()
print(id(ob1))
print(id(ob2))
del ob1
del ob2'''


num=[[[24,6],[8,10]],[[9,18],[12,20]]]
def ct(a):
    b=a[0][0]
    for i in a:
        for j in i:
            if b<j : b=j
    return b
print(ct(num[1]))
