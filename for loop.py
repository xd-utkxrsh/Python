#to check whether a number is prime or not
num=int(input("Enter number tobe checked: "))
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break
if (flag==0):
    print("Number is prime")
else:
    print("Number is not prime")


#armstrong number
