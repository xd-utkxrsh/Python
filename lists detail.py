'''data=input("data: ")
lis1=data.split(",")
print("list: ",lis1)
print("type  of list:",lis1)

a=[1,2,3,4,5,6,7,8,9]
print(a*0)

da=input("data: ")
list1=da.split(",")
print("list:",list1)
index=int(input("index: "))
if index<len(list1) and index>=-(len(list1)):
    print("element:",list1[index])
else:
    print("invalid")

a=(input())
li1=(a.split(","))
for i in range(0,len(li1)):
    li1[i]=int(li1[i])
if int(li1[0])==3 or int(li1[-1]==3):
    print("True")
else:
    print("False")
print(li1)

a=input("data: ")
li=a.split(",")
if li[0]==li[-1]:
    print("Equal")
else:
    print("Not Equal")

a=[1,2,3,4,5,6]
a[0:0]=[100,200,300]
print(a)

b=list(int(i) for i in (input().split()))
print(sum(b))'''

'''n=int(input("size: "))
l=[]
for i in range(1,n+1):
    i=input("element: ")
    l.append(i)
print(l)

data=(int(i) for i in (input("data: ").split()))
sum=0
data=list(data)
for j in data:
    sum=sum+j
print("sum:",sum)'''

