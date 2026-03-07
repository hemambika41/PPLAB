a = list(input("Enter list of elements: "))
print("Display original list:", a)
b = []
for i in a:
    if i not in b:
        b.append(i)
print("list after removing duplicates:", b)
