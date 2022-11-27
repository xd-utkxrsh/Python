'''a=[1,2,2]
b=[2,5,8]
c=list(zip(a,b))
print(c)

list1=list(input("data1: ").split(","))
list2=list(input("data2: ").split(","))
dict1=dict(zip(data1,data2))
print(list1)
key1=(input("key: "))
if key1 in dict1:
    print("value:",dict1[key1])
else:
    print("value: None")    #print("value:",dict1.get(key,"None"))

data1=input("data1: ")
data2=input("data2: ")
list1=list(data1.split(","))
list2=list(data2.split(","))
dict1=dict(zip(list1,list2))
for i in dict1:             #for key,value in sorted(dict1.items()):
    print(i,dict1[i])           #print(key,value)

data1=input("data1: ")
data2=input("data2: ")
list1=list(data1.split(","))
list2=list(data2.split(","))
dict1=dict(zip(list1,list2))
l3=[]
for i in dict1:
    l3.append(int(dict1[i]))
l3.sort()
print("max:",l3[-1])
print("min:",l3[0])

data1=input("data1: ")
data2=input("data2: ")
list1=list(data1.split(","))
list2=list(data2.split(","))
dict1=dict(zip(list1,list2))
key1=input("Key: ")
if key1 in dict1:
    val=input("Value: ")
    dict1[key1] = val
    print("sorted dict:",sorted(dict1.items()))
else:
    print("Index out of range")

data1=[int(i) for i in input("data1: ").split(",")]
cube1=[i**3 for i in data1 if i>10]
print(cube1)

data2=[int(i) for i in input("data2: ").split(",")]
odd1=[i for i in data2 if i%2!=0]
print(odd1)

data3=[int(i) for i in input("data3: ").split(",")]
if len(data3)<10:
    print("please enter 10 values")
else:
    add10=[i+10 for i in data3]
    print(add10)'''


