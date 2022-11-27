a=complex(input("Please enter  a complex number like a+bj: "))
b=complex(input("Please enter  a complex number like a+bj: "))
print(a,"+",b,"=",(a+b))
print(a,"-",b,"=",(a-b))
print(a,"*",b,"=",(a*b))
print(a,"/",b,"=",(a/b),"\n\n")

c=str(input("Enter a value: "))
print(int(c,2))
print(int(c,8))
print(int(c,10),"\n\n")

d=int(input("Enter an integer value: "))
print(isinstance(d,float),"\n\n")


e=int(input())
print(hex(e))
print(oct(e))
print(bin(e),"\n\n")


f=int(input("Enter integer: "))
g=int(input("Enter integer: "))
print(f,"//",g,"=",f//g)
print(f,"/",g,"=",f/g)
print(f,"%",g,"=",f%g,"\n")