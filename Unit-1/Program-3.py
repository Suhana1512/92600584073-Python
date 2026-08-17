#WAP to perform arithmatic , relational and logical using python operators.
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))

#Arithmatic Operations
print("\n--- Arithmetic Operations ---")
print("Addition is : ",a+b)
print("Subtraction is : ",a-b)
print("Multiplication is : ",a*b)
print("Division is : ",a/b)
print("Module is : ",a%b)

#Relational Operations
print("\n--- Relational Operations ---")
print("Is a==b : ",a==b)
print("Is a!=b : ",a!=b)
print("Is a>b : ",a>b)
print("Is a<b : ",a<b)
print("Is a>=b : ",a>=b)
print("Is a<=b : ",a<=b)

#Logical Operations
print("\n--- Logical Operations ---")
print("True if both are positive : ",a>0 and b>0)
print("True if at least one is positive : ", a>0 or b>0)
print("not (a>b) : ", not (a>b))
