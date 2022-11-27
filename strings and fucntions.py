'''a=input()
if a.startswith("Python"):
    print(a)
else:
    print("str after adding \'Python\':","Python "+a)
import string as s
print(s.punctuation)
print(s.digits)
print(s.printable)
import string
a=input("str1: ")
b=input("str2: ")
print("count:",a.count(b))
a=input()
b=""
b=len(a)
c=b/2
d=int(b/2)
if b%2==0:
    print("First half of str of even length:",a[0:d])
else:
    print("Second half of str of odd length:",a[d:])

a=input("str: ")
if len(a)==0:
    print("Null")
print("First:",a[0::2])
print("Second:",a[1::2])
print("original:",a)

str=input("str: ")
fstr=""
sstr=""
if len(str)==0:
    print("null")
else:
    if len(str)==1:
        print(str)
for i in range(0,len(str)):
    if i%2==0:
        fstr=fstr+str[i]
    else:
        sstr=sstr+str[i]

print("first:",fstr)
print("second:",sstr)
print("original:",str)

s=input("str: ")
for i in range(len(s)):
    print(s[a]*i,end="")'''
