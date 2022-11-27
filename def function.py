def area(rad):
    if rad<0:
        return
    else:
        ar=3.141*rad*rad
        return ar

rad=float(input("Enter the radius of the circle: "))
final=area(rad)
print("The area of the circle is",final)

def sayhello(username):
    print("Hello",username)

users=['Imtiaz','Utkarsh','Aman','Himanshu','Abhijeet','Chetan','Vanshika']
for i in users:
    sayhello(i)


def demo(num):
    return num**2,num**3

num=int(input("Enter the number: "))
r1,r2=demo(num)
print("The square of",num,"is",r1)
print("The cube of",num,"is",r2)


def circle(rad,pi):
    return (pi*rad*rad),(2*pi*rad)

rad=float(input("Enter the radius if the circle: "))
r3,r4=circle(rad,pi=3.141)
print("The area of the circle is",r3)
print("The circumference of the circle is",r4)

def count(name):
    return len(name)

name=input("Enter the name: ")
r5=count(name)
print("The length of the name is:",r5)
