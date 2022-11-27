import sys

value1=10
value2=20
str="Hello World"

print(value1,value2,sep="|",end="END",flush=False,file=sys.stdout)
print("Total number of votes: %7d,women votes: %5d" %(480,70))
#string format
print("The value value1={},value2={},str{}".format(value1,value2,str))
#integer format
print("This uses integer format{0:10d}".format(value1))
#floating point format
print("this uses floating point format {0:10f}".format(value1))
#hexadecimal format
print("this uses hexadecimal format {0:x}".format(value1))
print("this uses hexadecimal format {0:x}".format(value1))
#octal format
print("this uses octal format {0:o}".format(value1))