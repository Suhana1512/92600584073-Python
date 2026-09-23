#6. Write a program to iterate over lists strings and dictionaries using loops.
print("----------List----------")
fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)

print("----------String----------")
name = "Python"

for letter in name:
    print(letter)

print("----------Dictionary----------")
student = {"Name": "Suhana", "Age": 20, "Marks": 80}

for key, value in student.items():
    print(key, value)
