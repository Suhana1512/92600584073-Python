#WAP to illustrate the use of tuples and sets with basic operations.
#TUPLES
colors = ("red", "green", "blue", "red")
print("Tuple : ", colors)
#indexing and counting
print("First color : ",colors[0])
print("Count of 'red' : ",colors.count("red"))

#SETS
fruits = {"apple", "banana", "cherry", "apple"}
print("\nSet (duplicates removed):", fruits)

#Add and remove elements
fruits.add("orange")
fruits.discard("banana")
print("Updated Set:", fruits)

#Set operations(Union and Intersection)
a = {1, 2, 3}
b = {3, 4, 5}
print("Union (Combine):",a | b)
print("Intersection (Common):",a & b)
