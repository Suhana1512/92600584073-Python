#WAP to demonstrate recursion using factorial and fibonacci series.

#1.Recursion for Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)


#2.Recursion for Fibonacci Series
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


#Factorial
n1=int(input("Enter a number for factorial and fibonacci : "))
print(f"Factorial of {n1} is: {factorial(n1)}")

#Fibonacci
print(f"Fibonacci series up to {n1} terms:")
for i in range(n1):
    print(fibonacci(i), end=" ")
