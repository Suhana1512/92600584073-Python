#WAP to create and manipulatelists using indexing, slicing and list comprehension.

fruits = ["apple", "banana", "cherry"]
print("Original : ",fruits)
print("First fruit : ",fruits[0])

#Slicing
print("First two fruits : ", fruits[0:2])

fruits[1]="kiwi"
print("After updating :",fruits)

#List Comprehension(making all fruits uppercase)
upper_fruits = [f.upper() for f in fruits]
print("Uppercase fruits : ",upper_fruits)
