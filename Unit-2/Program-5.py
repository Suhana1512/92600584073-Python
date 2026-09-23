#5. Write a program to demonstrate the use of break continue and pass statements.
print("-------Using Break-------")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("-------Using Continue-------")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("-------Using Pass-------")
for i in range(1, 4):
    if i == 2:
        pass
    print(i)
