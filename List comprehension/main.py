# List comprehension=   a way to create a new list with less syntax
#                       can mimic crertain lambda functions, easier to read.
#                       list=[expression for an item or iterable]

#squares=[] #empty list
#for i in range (1,11):  #We create a for loop
#    squares.append(i*i) #define what each iteration should do and add that to the list
#print(squares)

#To write the similar code with less syntax

#squares = [i*i for i in range (1,11)]
#print(squares)

#This can also be used to mimic lambda functions

students=[100,90,80,70,60,50,40,30,0]

passed_students= list(filter(lambda marks: marks>=60,students))

print(passed_students)

#list=[expression for item in iterable if conditional]

passed_students=[i for i in students if i>=60]
print(passed_students)

# To print the passed marks and fail for the rest we say
passed_students=[i if i>=60 else "FAIL" for i in students]

print(passed_students)