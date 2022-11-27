def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

num1=int(input("Enter the number: "))
print("The factorial of the",num1,"is",factorial(num1),"\n\n")


def fib(p):
    if p==0:
        return 1
    if p==1:
        return 1
    else:
        return fib(p-1)+fib(p-2)

num2=int(input())
print(fib(num2))