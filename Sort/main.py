# sort() method     = method used with lists
# sort() function   = used with iterable

#students= ["Squidward","Spongebob","Sandy","Patrick","Mr. Krabs" ]

#To sort list in alphabetical order
#students.sort()

#There is another way to print the reversed list
#students.sort(reverse=True)

#Since sort method is only available for lists
#if we were to work with tuples we will use the sort function
# as the sort method doesn't work with other iterables.

#students= ("Squidward","Spongebob","Sandy","Patrick","Mr. Krabs" )

#sorted_students = sorted(student) #sorted students is a list

#sorted_students = sorted(students,reverse=True) #will print the sorted tuple in reverse



#This will print the sorted list
#for i in sorted_students:
#    print(i)

#Here we have a list of tuples
#A name, A letter grade and their mark for the course
#Now if we want to sort by either the student name, the grade or the mark
#We make use of the key word argument

students = [("Squidward","F",60),
            ("Sandy","A",33),
            ("Patrick","D",36),
            ("Spongebob","B",20),
            ("Mr.Krabs","C",78)]

#To sort alphabetically
#students.sort()

#To sort by grade letter
#grade= lambda grades: grades[1]# The one index sorts them by the grade letter
#students.sort(key=grade, reverse=True)

#To print by age , with the sorted function
age = lambda ages: ages[2]
sorted_students= sorted(students,key=age)

for i in sorted_students:
    print(i)


