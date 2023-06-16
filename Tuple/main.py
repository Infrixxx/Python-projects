# Tuple=    collection which is ordered and unchangeable
#           used to group together related data

#Example of a tuple
student=('Tumi',22,'male')

#This will count the amount of times, Tumi appears in the tupple
print(student.count("Tumi"))

#This will print the index of the element in the tuple
print(student.index("Tumi"))

#You can display all the contents of the tuple, using for loop
for x in student:
    print(x)

if "Tumi" in student:
    print('Tumi is here!')