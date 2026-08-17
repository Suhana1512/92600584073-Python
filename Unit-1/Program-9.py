#WAP to define and use of user-defined functions with different types of arguments.
#NO arguments and NO return value
def greet():
    print("Hello, welcome to Python functions!")


#REQUIRED(Positional) arguments
def add(a, b):
    return a + b


#DEFAULT argument
def introduce(name, age=18):
    print(f"My name is {name} and I am {age} years old.")


# --- Calling the Functions ---

print("--- 1. No Arguments ---")
greet()

print("\n--- 2. Required Arguments ---")
result = add(5, 3)
print(f"Sum: {result}")

print("\n--- 3. Default Arguments ---")
introduce("Emily", 25)  #Uses the provided age (25)
introduce("Noa")  #Uses the default age (18)
