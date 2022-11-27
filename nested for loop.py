num=int(input("Enter the numbr of lines: "))

for i in range(0,num):
    for j in range(0,i+1):
        print(j+1,end=" ")
    print()
print("\n")
"""the output if input=5
1
1 2
1 2 3 
1 2 3 4 
1 2 3 4 5"""

for i in range(0,num):
    for j in range(0,i+1):
        print(i+1,end=" ")
    print()
print("\n")
"""the output if input=5
1
2 2
3 3 3
4 4 4 4 
5 5 5 5 5"""

for i  in range(1,11,1):
    for j in range(1,6,1):
        print(i*j,end=" ")
    print()
print("\n")
"""the output will be 
1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25
6   12  18  24  30
7   14  21  28  35
8   16  24  32  40
9   18  27  36  45
10  20  30  40  50"""

for i in range(num,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print("\n")
"""the output will be  
*   *   *   *   *
*   *   *   *   
*   *   *   
*   *   
*"""

for i in range(0,num,1):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
print("\n")
"""the output will be
*
*   *
*   *   *
*   *   *   *
*   *   *   *   *"""