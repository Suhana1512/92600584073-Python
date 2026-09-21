#WAP to create dictionary and demonstrate dictionary methods and iteration.

student = {"name": "Alice", "age": 20, "course": "Python"}
print("Dictionary:", student)
print("Name: ", student["name"])
print("Age : ", student.get("age"))

#Methods
student.update({"age" : 21, "city": "New York"})
print("After update : ", student)

remove=student.pop("course")            # Remove a specific key
print(f"Popped '{remove}' : ", student)

print("Keys : ", student.keys())
print("Values : ", student.values())

# 3. Iteration
print("\nIterating through keys and values:")
for key, value in student.items():
    print(f"{key} : {value}")
