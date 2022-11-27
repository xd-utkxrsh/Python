import random
seq="abcdefghijklmnopqrstuvwxyz"
print(random.choice(seq))
print("\n")

L1=[10,20,23,2,3,1,5]
random.shuffle(L1)
print(L1)
print("\n")

for i in range(5):
    print(random.randint(1,100))
print("\n")

for i in range(5):
    random.seed(82)
    print(random.randint(1,100))
print("\n")

print(random.random())
print("\n")

print(random.randrange(2,20,2))
print("\n")

print("min value:",min(1,2,3,4,5,6,7,8,9,60,51,32,))
print("max value: ",max(2,21,5,6,7,8,9,22))
print("power: ",pow(3,2))
print("absolute: ",abs(-32.8))
print("round off: ",round(2.8))
print("round off: ",round(2.2))
print("floor value: ",math.floor(12.8))
print("ceil value: ",math.ceil(12.8))
print()
print("\n")