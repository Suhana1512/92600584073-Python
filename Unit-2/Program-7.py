#7. Write a program to demonstrate list dictionary and set comprehensions.
print("----------List comprehension----------")
list1 = [1, 2, 3]
print([x * 2 for x in list1])

print("----------Dictionary comprehension----------")
print({x: x * 2 for x in list1})

print("----------Set comprehension----------")
print({x * 2 for x in list1})
