a=100
b=10
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)
print(a**b)

num=int(input())
for i in range(num,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print("\n\n\n")
