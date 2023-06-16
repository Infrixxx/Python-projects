# zip(*iterables)=  aggregate elements from two or more iterables( list, tuples,sets,etc.)
#                   creates a zip object with paired elements stored in tuples for each element.

usernames = ["Dude", "Bro" , "Mister"]
passwords= ("p@ssword","abc123","guest")

#users= list(zip(usernames,passwords)) # we can cast our zip object to a list
users= dict(zip(usernames,passwords))

print(type(users))      #Now users is a zip object

#for i in users:
#    print(i)

#since we printing from a dictionary

for key,value in users.items(): #we use the items() to print items in the dictionary
    #print(key,value)
    print(key+" : "+ value)   #seperate with a colon to make it more readable

#When we zip two iterables, we make them into one , we not limited to just two,we can zip even more.
usernames = ["Dude", "Bro" , "Mister"]
passwords= ("p@ssword","abc123","guest")
login_date= ["1/1/2021","1/2/2021","1/3/2021"]

users= zip(usernames,passwords,login_date)
print("\n")
for i in users :
    print(i)