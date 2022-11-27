s="abc"
l1=list(s)
print(l1)
s1="hello world"
print(s1.split())
data=input("str1: ")    #inout being "19,20,21,31"
data=data.split(",")
print(data)
for i in range(0,len(data)):
    data[i]=int(data[i])
    print(data[i])
print(f'max of data = (max(data))')
print(f'min of data = (min(data))')
print(f'sum of data = (sum(data))')