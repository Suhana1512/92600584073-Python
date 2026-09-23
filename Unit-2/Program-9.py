#9. Write a program to demonstrate iterators and iterables in Python.
# Iterable
numbers = [1, 2, 3]

# Iterator
a = iter(numbers)

print("First iterator : ",next(a))
print("Second iterator : ",next(a))
print("Third iterator : ",next(a))
