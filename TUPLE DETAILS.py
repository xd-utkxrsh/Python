'''data=input("data: ")
list1=data.split()
tuple1=tuple(list1)
val=int(input("value: "))
print("tuple *",val,"=",tuple1*val)

data2=input("data: ")
list2=data2.split()
tuple2=tuple(list2)
print("concatenation:",tuple1+tuple2)

data1=input("data:")
list1=data1.split(",")
for j in range(len(list1)):
    list1[j]=int(list1[j])
tuple1=tuple(list1)
print(min(tuple1))

data=input("data:")
list1=data.split()
for i in range(len(list1)):
    list1[i]=int(list1[i])
tuple1=tuple(list1)
print("tuple:",tuple1)
print("sum:",sum(tuple1))

data=input("data: ")
#list1=data.split()
tuple1=tuple(data.split())
print("length:",len(tuple1))

month={'jan':1,'feb':2,'mar':3}
print(month)
print(type(month))

d=dict([('one',1),('two',2),('three',3)])
print(d)
print(type(d))
print(d['three'])
capitals={"use":"dc","india":"new delhi","nepal":"kathmandu"}
print(capitals.get("india"))
print(capitals.get("america"))
print(capitals["india"])
fru={1:'apple',2:'mango',3:'guava'}
for i in fru:
    print(fru[i],end=" ")

fru={1:'apple',2:'mango',3:'guava'}
print(fru.items(),'\n\n')
for key,value in sorted(fru.items()):
    print(key,value)
fru={1:'apple',2:'mango',3:'guava'}
print(fru.pop(2))
print(fru)
fr={1:'apple',2:'mango',3:'guava'}
print(fr.popitem())
print(fr)
ru={1:'apple',2:'mango',3:'guava'}
del ru[2]
print(ru)
u={1:'apple',2:'mango',3:'guava'}
u.clear()
print(u)
ur={1:'apple',2:'mango',3:'guava'}
del ur

fru={1:'apple',2:'mango',3:'guava'}
print(all(fru))
fru={1:'',2:'mango','':'guava'}
print(all(fru))
fru={1:'',2:'mango','':'guava'}
print(any(fru))
fru={1:'apple',2:'mango',3:'guava'}
print(len(fru))
fru={1:'apple',3:'mango',2:'guava'}
print(sorted(fru))

col={1:'red',2:'yellow',3:'green',6:'blue',5:'pink',4:'magenta',8:'black',7:'white',10:'cyan',9:'grey'}
print(col[5])
print(sorted(col))
col[1]='blue'
print(col)'''
