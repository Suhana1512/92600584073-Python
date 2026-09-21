#WAP to demonstrate string operations including slicing formatting and built-in string function.

n="  Hello, Python World!  "

#Built-in String Functions
print("Original string : ",n)
print("String in uppercase : ",n.upper())
print("Stripped the space: ",n.strip())
print("Replaced the word in string: ",n.replace("Python", "Coding"))
print("Length of the string: ",len(n))

#String Slicing [start:end:step]
n1 = n.strip()
print("First 5 characters : ",n1[:5])
print("Last 6 characters : ",n1[-6:])
print("Reversed string : ",n1[::-1])

#String Formatting (f-string)
lang = "Python"
ver = 3.12
print(f"Learning {lang} version {ver} is fun!")
