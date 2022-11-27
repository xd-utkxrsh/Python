#resume
'''name=input("Enter your name here: ")
uni_name=input("Enter your university name here: ")
father=input("Enter your Father's name here: ")
mother=input("Enter your Mothe's name here: ")
course=input("Enter your course here: ")
location=input("Enter your location here: ")

print("Resume",name,uni_name,father,mother,course,location,sep="\n",end="\n\n\n")


print("The length of",name,"is",len(name))
print("The minimum character in",name,"is",min(name))
print("The maximum character in",name,"is",max(name))'''


#vowel  in name
s=str("india")
count=0
for ch in s:
    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
        print(ch,sep=" ")
        count=count+1
print("\n\nthe number of vowels in string is",count)