def interst(p,r,t):
    si=p*r*t
    final=si/100
    print(final,"\n\n")
a=int(input("p: "))
b=float(input("r: "))
c=int(input("t: "))
interst(a,b,c)

def interst1(p1,t1,r1=7.2): #r is  already given
    si1=p1*r1*t1
    final1=si1/100
    print(final1,"\n\n")
d=int(input("p: "))
e=int(input("t: "))
interst1(d,e)


def fun1(name="padma",age=12):
    print(name,"is",age,"years old.\n\n")
fun1()
fun1("aruna",16)
fun1(age=16,name="arjuna")
fun1("utkarsh",18)

def add(u,v):
    c=u+v
    return c
def sub(u,v):
    return u-v
def mul(u,v):
    return u*v

x=int(input("a:"))
y=int(input("b: "))
r1=add(x,y)
print("result of addition is",r1)
r2=sub(x,y)
print("result of sub is",r2)
print("result of mul is", mul(x,y),"\n\n")