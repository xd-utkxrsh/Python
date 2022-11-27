'''str=input()
if len(str)<2:
    print(str)
else:
    print((str[0:3])*3)

s=input("Enter the string: ")
n=int(input("Enter the number of time: "))
print(s*n)


a=input("Enter the string: ")
n=int(input("Enter the index: "))
if n<0 and n<len(a):
    print("Invalid")
else:
    print((a[:n])*n)

w="pyhton"
print(w.upper())

a=input("Enter: ")
print(a.upper())
print(a.title())
print(a.split())
print(a.capitalize())
print(a.lower())
b=input("Enter1: ")
print(b.join(a))
print(a.capitalize())
c=input("Enter: ")
print(c.upper())
print(c.title())
print(c.split())
print(c.center(50,"%"))
print(c.lower())
d=input("Enter1: ")
print(d.join(c))
print(c.replace("Strings","Tuple"))

a=input("Enter1: ")
b=input("Enter2: ")
print((a*3)+b)

print("Python provides built-in libraries\nUsing Python we can implement more and more application\n\tPyhton is Robust")

a=input("str1: ")
b=input("str2: ")
if len(a)>len(b):
    print(b+a+b)
elif len(a)<len(b):
    print(a+b+a)
else:
    print("equal length")'''

a=input("Enter: ")
print(a.startswith("P"))
print("Character with minimum value: ",min(a))
print("Character with maximum value: ",max(a))