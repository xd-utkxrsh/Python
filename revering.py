num=int(input())
sum=0                #rev=()
rem=0
while (num>0):
    rem=num%10
    num=num//10
    sum=sum+rem     #rev=rev*10+rem
print(sum)          #print(rev)


num=int(input())
rev=0
rem=0
while (num>0):
    rem=num%10
    num=num//10
    rev=rev*10+rem
print(rev)
